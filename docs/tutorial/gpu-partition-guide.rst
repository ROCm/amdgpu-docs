GPU Partitioning Guide for SPX and CPX on Bare-Metal OS for MI300X
===================================================================

1. Overview
-----------

a. Introduction
^^^^^^^^^^^^^^^^

The AMD Instinct™ MI300X GPU represents a significant step forward in the design of modular, scalable GPU compute platforms. With its innovative architecture and ROCm software ecosystem, MI300X supports dynamic compute and memory partitioning. This capability enables developers and system administrators to treat a single GPU as multiple logical devices, allowing for efficient workload management, resource isolation, and performance tuning.

The MI300X GPU introduces advanced support for compute and memory partitioning, enabling high-performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads to achieve fine-grained resource allocation and isolation.

Partitioning exposes internal GPU hardware components, specifically Compute Complexes (XCDs) and memory stacks (HBM) as discrete logical devices. This allows users to optimize system utilization, achieve better scheduling control, and tailor compute and memory resources to workload-specific requirements.

This guide provides a detailed overview of GPU partitioning modes, primarily CPX and NPS4 on bare-metal operating systems. It includes architectural background, partitioning use cases, configuration methods, and validation steps to ensure users can fully leverage MI300X's capabilities.

2. GPU Architecture Summary
---------------------------

The MI300X GPU is composed of modular chiplets, each optimized for compute or I/O tasks to achieve scalability and high-throughput performance.
Key architectural components include:

- **XCD (Accelerator Complex Die):** Compute element of the GPU, each XCD contains 38 Compute Units (CUs), responsible for executing parallel workloads.
- **IOD (I/O Die):** Manages interconnects, memory, and data routing across the chiplets.
- **3D Stacking**: Each pair of XCDs is 3D-stacked on a single IOD allowing for tight integration and low-latency interconnects.
- **HBM (High-Bandwidth Memory):** MI300X includes 8 stacks of HBM, offering 192GB of unified memory.
- **Total GPU Configuration**:
  - 8 XCDs per GPU → 304 total CUs
  - 4 IODs per GPU
  - 8 HBM (High Bandwidth Memory) stacks (2 per IOD)
  - 192GB of unified HBM capacity

This layout provides the foundation for partitioning, allowing resources to be split and exposed logically to the operating system and applications.

3. Partitioning Concepts
------------------------

a. Compute Partitioning (SPX, CPX)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compute partitioning (also referred to as MCP – Modular Chiplet Platform) is the division of the GPU's compute and memory resources into smaller logical units, which can then be addressed as independent devices by applications. This is implemented in the driver layer and can be dynamically adjusted at runtime using command-line tools like ``amd-smi``.

There are two key compute partitioning modes:

- **SPX (Single Partition X-celerator):** Treats the entire GPU as a single device.
- **CPX (Core Partitioned X-celerator):** Exposes each XCD as an individual logical GPU.

**Key Benefits of Partitioning:**

- Supports workload isolation and parallelism.
- Enables better scheduling granularity and performance tuning.
- Facilitates resource sharing across users or processes in multi-tenant environments.

**Partitioning Rules:**

- Partitions must include an even number of XCDs (e.g., 2, 4, 6, 8).
- Partitioning is spatial: each partition is composed of physically grouped XCDs.
- Compute partitioning is configured via the driver and hardware level, no VM (virtualization) or hypervisor required.

**Partition Modes Comparison**

+--------+------------------+----------------+-------------------+-------------------------+
| Mode   | Logical Devices  | CUs per Device | Memory per Device | Best For                |
+========+==================+================+===================+=========================+
| SPX    | 1                | 304            | 192GB             | Unified workloads       |
+--------+------------------+----------------+-------------------+-------------------------+
| CPX    | 8                | 38             | 24GB              | Isolation, fine-grained |
|        |                  |                |                   | scheduling              |
+--------+------------------+----------------+-------------------+-------------------------+

b. SPX (Single Partition X-celerator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Default Mode** for MI300X.
- Treats all 8 XCDs as a single monolithic GPU.
- All memory and compute resources are visible as one unified device.
- Implicit synchronization across XCDs is handled by the hardware.

**Use Case**: Ideal for large-scale models or applications that require unified compute and memory access without needing explicit control over scheduling.

**Behavior:**

- ``amd-smi`` shows **1 GPU** with **304 CUs** and **192GB HBM**.
- Workgroups are **automatically distributed** across all XCDs (round-robin).

c. CPX (Core Partitioned X-celerator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Each XCD is represented as a **separate logical GPU**.
- Offers granular control—each partition gets 38 CUs and 24GB of HBM.
- **Memory Allocation:**

  - In NPS1, HBM memory is interleaved across all stacks.
  - In NPS4, each XCD gets a dedicated memory quadrant (2 HBM stacks) which can be used to interleave its dedicated 24GB.

- CPX works optimally with memory partitioning (NPS4)

**Use Case**: 

1. **Multi-Tenant Environments:** Allocate separate GPU partitions to different users or tenants in a data center to achieve isolation.
2. **Heterogeneous Workloads:** Run AI training, inference, and HPC workloads simultaneously on different partitions where individual models/data fit within a single XCD's memory.
3. **Resource Oversubscription:** Optimize resource usage by oversubscribing partitions for workloads with varying demands.

**Behavior:**

- ``amd-smi`` shows **8 GPUs**, each with **38 CUs** and **24GB HBM**.
- Workgroups are explicitly launched to a specific XCD (i.e., scheduling can be
  controlled at the application level).
- Peer-to-Peer (P2P) access between XCDs is available and can be enabled.

.. - MALL (Memory Attached Last Level Cache) is shared between two CPX partitions.

.. list-table::
   :header-rows: 1

   * - MI300X SPX
     - MI300X CPX
   * - .. image:: ../images/gpu-partition_SPX.png
     - .. image:: ../images/gpu-partition_CPX.png
   * - **SPX:** All XCDs appear as one logical device.
     - **CPX:** Each XCD appears as one logical device.

**Memory Partitioning (NPS):**

- The memory partitioning modes (known as Non-Uniform Memory Access (NUMA) Per Socket (NPS)) change the number of NUMA domains that a device exposes, which define how HBM (High Bandwidth Memory) is allocated and exposed to logical devices.
- Memory partitioning in the MI300X series involves dividing the total memory, specifically HBM stacks, which are accessible to a compute unit, into partitions.
- This is configured as application memory for XCDs, allowing for more efficient memory management and allocation.
- The memory partitioning is done at the hardware level, and the driver manages the visibility of these partitions to the operating system and applications.
- In MI300X, the number of memory partitions must be less than or equal to the number of compute partitions.
- The MI300X supports two memory partitioning modes:

  - **NPS1 (Unified Memory):**

    - All 8 HBM stacks are viewed as one unified memory pool and is accessible to all XCDs.
    - `amd-smi` will show 1 device with 192GB of HBM.
    - Memory is allocated interleaved across all HBM stacks.
    - Best for workloads requiring unified memory.
    - Compatible mode with SPX and CPX.

  - **NPS4 (Partitioned Memory):**

    - Pairs of HBM stacks forming 48GB each are viewed as separate memory partitions.
    - Each memory quadrant (partition) of the memory is directly visible to the logical devices in its quadrant.
    - An XCD can still access all portions of memory through multi-GPU programming techniques.
    - Best for workloads requiring dedicated memory resources.
    - Only available with CPX mode.
    - In NPS4 mode, the traffic latency to HBM (High Bandwidth Memory) is minimized because it remains on the same AID (Accelerator Interface Domain), leading to shorter latency and faster transitions from idle to full bandwidth
    - Highly performant when paired with CPX mode for workloads that fit within the memory capacity of a single XCD.

..  - `amd-smi` will show 4 devices with 48GB of HBM each.

+--------------+-------------------------------+------------------------------+
| Memory Mode  | Description                     | Compute Mode Compatibility |
+==============+===============================+==============================+
| **NPS1**     | Unified memory pool (192GB)     | SPX, CPX                   |
+--------------+-------------------------------+------------------------------+
| **NPS4**     | 4 memory partitions (48GB each) | CPX only                   |
+--------------+-------------------------------+------------------------------+

.. list-table::
   :header-rows: 1

   * - MI300X NPS1
     - MI300X NPS4
   * - .. image:: ../images/gpu-partition_NPS1.png
     - .. image:: ../images/gpu-partition_NPS4.png
   * - **NPS1:** All HBM stacks appear as a unified memory pool.
     - **NPS4:** HBM stacks are segmented into memory quadrants.

.. note::
   Mixed memory partitioning modes are **not recommended** for single-node configurations.

c. Benefits of Partitioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CPX + NPS4 mode in the MI300X accelerator delivers improved performance for small language models (13B parameters or less) that fit within the memory capacity of a single CPX GPU.
- CPX + NPS4 mode in the MI300X accelerator, benefits significantly to RCCL (Radeon Collective Communication Library) that require high throughput and low latency for collective communication operations.
- Partitioning allows **dynamic resource control**—compute and memory reconfiguration **without requiring reboots**, ensuring high system availability. This is particularly advantageous for maintaining continuous operation in data centers.

d. Prerequisites
^^^^^^^^^^^^^^^^

- ROCm stack must be correctly installed.
- Firmware and kernel must support partitioning (latest recommended).
- `amd-smi` tool is required for runtime management.
- Bare-metal OS installation—no virtualization layer.

e. System Requirements
^^^^^^^^^^^^^^^^^^^^^^

To ensure a successful partitioning experience with MI300X GPUs, confirm the following system requirements:

Hardware Requirements
~~~~~~~~~~~~~~~~~~~~~

- **GPU**: AMD MI300X

Software Requirements
~~~~~~~~~~~~~~~~~~~~~

- **Linux Kernel**: Version 5.15 or newer

  #. to find the kernel version, run the following command 

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check Linux kernel version
            $ hostnamectl | grep 'Kernel'

      .. tab-item:: Shell output

         ::

            Kernel: Linux 5.15.0-134-generic

- **AMDSMI Tool Library**: Version 25.3.0 or newer

  #. to find the amdsmi version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check AMD-SMI version
            $ amd-smi version | grep -o 'AMDSMI [^|]*'

      .. tab-item:: Shell output

         ::

            AMDSMI Tool: 25.2.0+f4ad5ee
            AMDSMI Library version: 25.3.0

- **AMD GPU Driver**: amdgpu-build 2120656 (>= 6.12.12)

  #. to find the amdgpu version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check amd gpu version
            $ amd-smi version | grep -o 'amdgpu version: [^|]*'

      .. tab-item:: Shell output

         ::

            amdgpu version: 6.12.12

2. Hardware Compatibility List
------------------------------

Firmware Requirements
~~~~~~~~~~~~~~~~~~~~~

- **VBIOS Version**:  022.040.003.043.000001

  #. to find the VBIOS version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check VBIOS version
            $ amd-smi static | grep -A 4 -m 1 'VBIOS'

      .. tab-item:: Shell output

         ::

            VBIOS:
              NAME: AMD MI300X_HW_SRIOV_CVS_1VF
              BUILD_DATE: 2024/09/25 10:52
              PART_NUMBER: 113-M3000100-102
              VERSION: 022.040.003.042.000001

Operating System Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Ubuntu 22.04+, 24.04+
- Oracle Linux Server 8.8+

  #. to check the operating system version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check Operating System version
            $ hostnamectl | grep 'Operating System'

      .. tab-item:: Shell output

         ::

            Operating System: Ubuntu 22.04.5 LTS

Driver Requirements
~~~~~~~~~~~~~~~~~~~

- **ROCm**: Version 6.4 or newer

  #. to find the ROCm version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check ROCm version
            $ amd-smi version | grep -o 'ROCm version: [^|]*'

      .. tab-item:: Shell output

         ::

            ROCm version: 6.4.0

3. First Partition / Quick Start
--------------------------------

Creating CPX/NPS4 Partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a CPX/NPS4 partition:

a. **Set compute partitioning mode to CPX:**


   .. tab-set::

      .. tab-item:: Compute Partition Command

         .. code-block:: shell-session

            # Set compute partition mode
            $ sudo amd-smi set --gpu all --compute-partition CPX    

      .. tab-item:: Shell output

         ::

            GPU: 0
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 1
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 2
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 3
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 4
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 5
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 6
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 7
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

b. **Set memory partitioning mode to NPS4:**

   .. tab-set::

      .. tab-item:: Memory Partition Command

         .. code-block:: shell-session

            # Set memory partition mode
            $ sudo amd-smi set --memory-partition NPS4  

      .. tab-item:: Shell output

         ::
            
          ****** WARNING ******

          Setting Dynamic Memory (NPS) partition modes require users to quit all GPU workloads.
          AMD SMI will then attempt to change memory (NPS) partition mode.
          Upon a successful set, AMD SMI will then initiate an action to restart AMD GPU driver.
          This action will change all GPU's in the hive to the requested memory (NPS) partition mode.

          Please use this utility with caution.

          Do you accept these terms? [Y/N] Y

          Trying again - Updating memory partition for gpu 0: [██████████████..........................] 50/140 secs remain

          GPU: 0
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 1
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 2
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 3
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 4
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 5
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 6
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 7
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 8
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 9
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 10
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 11
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 12
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 13
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 14
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          OSError: [Errno 24] Too many open files

.. note::
   The above `amd-smi` command to set the partition mode may not show memory partition status for all GPUs. This is a known tool issue.
   Despite the error, the partition mode will be set correctly across all GPUs.

- The command will set the following:

  - **Compute Partitioning:** CPX mode (8 XCDs → 8 logical GPUs)
  - **Memory Partitioning:** NPS4 mode (4 memory partitions with 2 HBM stacks each)


Verifying Partition Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To confirm active partitioning state:

Use `amd-smi` to confirm active partition states:

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check partitioning status
            $ amd-smi static --partition

      .. tab-item:: Shell output

         ::

            GPU: 0
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 0

            GPU: 1
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 1

            GPU: 2
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 2

            GPU: 3
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 3

            GPU: 4
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 4

            GPU: 5
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 5

            GPU: 6
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 6

            GPU: 7
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 7
            
            GPU: 8
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 0

            GPU: 9
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 1

            GPU: 10
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 2

            GPU: 11
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 3

            GPU: 12
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 4

            GPU: 13
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 5

            GPU: 14
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 6

            GPU: 15
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 7
            
            GPU: 16
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 0

            GPU: 17
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 1

            GPU: 18
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 2

            GPU: 19
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 3

            GPU: 20
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 4

            GPU: 21
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 5

            GPU: 22
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 6

            GPU: 23
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 7
            
            GPU: 24
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 0

            GPU: 25
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 1

            GPU: 26
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 2

            GPU: 27
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 3

            GPU: 28
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 4

            GPU: 29
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 5

            GPU: 30
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 6

            GPU: 31
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 7
            
            GPU: 32
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 0

            GPU: 33
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 1

            GPU: 34
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 2

            GPU: 35
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 3

            GPU: 36
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 4

            GPU: 37
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 5

            GPU: 38
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 6

            GPU: 39
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 7
            
            GPU: 40
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 0

            GPU: 41
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 1

            GPU: 42
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 2

            GPU: 43
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 3

            GPU: 44
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 4

            GPU: 45
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 5

            GPU: 46
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 6

            GPU: 47
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 7
            
            GPU: 48
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 0

            GPU: 49
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 1

            GPU: 50
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 2

            GPU: 51
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 3

            GPU: 52
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 4

            GPU: 53
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 5

            GPU: 54
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 6

            GPU: 55
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 7
            
            GPU: 56
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 0

            GPU: 57
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 1

            GPU: 58
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 2

            GPU: 59
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 3

            GPU: 60
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 4

            GPU: 61
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 5

            GPU: 62
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 6

Modifying Partitions
~~~~~~~~~~~~~~~~~~~~

Use the following commands to switch compute or memory partitioning modes.

**Compute Partition Examples:**

   .. tab-set::

      .. tab-item:: Compute Partition Command

         .. code-block:: shell-session

            # Set compute partition mode
            $ sudo amd-smi set --gpu all --compute-partition CPX    

      .. tab-item:: Shell output

         ::

            GPU: 0
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 1
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 2
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 3
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 4
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 5
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 6
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)

            GPU: 7
                ACCELERATOR_PARTITION: Successfully set accelerator partition to CPX (profile #3)
 
   .. tab-set::

      .. tab-item:: Compute Partition Command

         .. code-block:: shell-session

            # Set compute partition mode
            $ sudo amd-smi set --gpu all --compute-partition SPX    

      .. tab-item:: Shell output

         ::

            GPU: 0
                ACCELERATOR_PARTITION: Successfully set accelerator partition to SPX (profile #0)

            GPU: 1
                ACCELERATOR_PARTITION: Successfully set accelerator partition to SPX (profile #0)

            GPU: 2
                ACCELERATOR_PARTITION: Successfully set accelerator partition to SPX (profile #0)

            GPU: 3
                ACCELERATOR_PARTITION: Successfully set accelerator partition to SPX (profile #0)

            GPU: 4
                ACCELERATOR_PARTITION: Successfully set accelerator partition to SPX (profile #0)

            GPU: 5
                ACCELERATOR_PARTITION: Successfully set accelerator partition to SPX (profile #0)

            GPU: 6
                ACCELERATOR_PARTITION: Successfully set accelerator partition to SPX (profile #0)

            GPU: 7
                ACCELERATOR_PARTITION: Successfully set accelerator partition to SPX (profile #0)

   .. tab-set::

      .. tab-item:: Memory Partition Command

         .. code-block:: shell-session

            # Set memory partition mode
            $ sudo amd-smi set --memory-partition NPS4  

      .. tab-item:: Shell output

         ::
            
          ****** WARNING ******

          Setting Dynamic Memory (NPS) partition modes require users to quit all GPU workloads.
          AMD SMI will then attempt to change memory (NPS) partition mode.
          Upon a successful set, AMD SMI will then initiate an action to restart AMD GPU driver.
          This action will change all GPU's in the hive to the requested memory (NPS) partition mode.

          Please use this utility with caution.

          Do you accept these terms? [Y/N] Y

          Trying again - Updating memory partition for gpu 0: [██████████████..........................] 50/140 secs remain

          GPU: 0
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 1
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 2
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 3
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 4
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 5
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 6
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 7
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 8
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 9
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 10
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 11
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 12
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 13
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          GPU: 14
            MEMORY_PARTITION: Successfully set memory partition to NPS4

          OSError: [Errno 24] Too many open files

   .. tab-set::

      .. tab-item:: Memory Partition Command

         .. code-block:: shell-session

            # Set memory partition mode
            $ sudo amd-smi set --memory-partition NPS1  

      .. tab-item:: Shell output

         ::
            
          ****** WARNING ******

          Setting Dynamic Memory (NPS) partition modes require users to quit all GPU workloads.
          AMD SMI will then attempt to change memory (NPS) partition mode.
          Upon a successful set, AMD SMI will then initiate an action to restart AMD GPU driver.
          This action will change all GPU's in the hive to the requested memory (NPS) partition mode.

          Please use this utility with caution.

          Do you accept these terms? [Y/N] Y

          Trying again - Updating memory partition for gpu 0: [██████████████..........................] 50/140 secs remain


            GPU: 0
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 1
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 2
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 3
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 4
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 5
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 6
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 7
                MEMORY_PARTITION: Successfully set memory partition to NPS1

.. note:
      NPS4 is only compatible with CPX mode. Attempting to set NPS4 with SPX will result in a failure.

Deleting Partitions
~~~~~~~~~~~~~~~~~~~

To delete or reset partitions, revert both compute and memory partitioning to defaults:

.. code-block:: shell-session

   $ sudo amd-smi set --gpu all --compute-partition SPX
   $ sudo amd-smi set --memory-partition NPS1

### Running Basic Tests

You can run basic functional checks using ROCm or HIP sample applications.

**Example:**

.. code-block:: shell-session

   # Placeholder for validation steps

4. Basic Troubleshooting
------------------------

This section outlines common errors that users may encounter during GPU partitioning operations using the `amd-smi` tool, along with suggested solutions and explanations.

a. Error while running amd-smi command for partitioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you receive an error when executing partitioning commands using `amd-smi`, verify that you are running the command with elevated permissions.

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check if the GPU is in use
            $ amd-smi set --gpu all --compute-partition SPX


      .. tab-item:: Shell output

         ::

            amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
            10 | AMDSMI_STATUS_NO_PERM - Permission Denied

            The above exception was the direct cause of the following exception:

            PermissionError: Command requires elevation

**Resolution:**

- Ensure the command is executed with `sudo`.
- Confirm that no applications or system services are currently utilizing the GPU. If so, terminate or stop them before retrying.

b. Error while creating partitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Partitioning operations can fail if the GPU is actively being used by another process.

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # setting memory partition mode
            $ sudo amd-smi set --gpu all --compute-partition SPX

      .. tab-item:: Shell output

         ::

            amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
            30 | AMDSMI_STATUS_BUSY - Device busy

            The above exception was the direct cause of the following exception:

            ValueError: Unable to set accelerator partition to SPX on GPU ID: 0 BDF:0000:11:00.0

**Resolution:**

- Ensure that no compute workloads or system services are using the GPU.
- Use `amd-smi`, `ps -aux`, `top` -like tools to identify running GPU jobs.
- Terminate conflicting jobs before retrying the partition command.           

c. Error while resetting partition to SPX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NPS4 memory mode is only compatible with CPX compute mode. If you attempt to switch to SPX while memory mode is still set to NPS4, the operation will fail.

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Set compute partition mode
            $ sudo amd-smi set --gpu all --compute-partition SPX    

      .. tab-item:: Shell output

         ::

            Attempted to set accelerator partition to SPX (profile #0 on GPU ID: 0 BDF:0000:11:00.0

            [AMDSMI_STATUS_SETTING_UNAVAILABLE] Please check amd-smi partition --memory --accelerator for available profiles.
            Users may need to switch memory partition to another mode in order to enable the desired accelerator partition.

            amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
                    55 | AMDSMI_STATUS_SETTING_UNAVAILABLE - Setting is not available

            The above exception was the direct cause of the following exception:

            ValueError: [AMDSMI_STATUS_SETTING_UNAVAILABLE] Unable to set accelerator partition to SPX on GPU ID: 0 BDF:0000:11:00.0

**Resolution:**

Before switching to SPX mode, first revert the memory partition mode to NPS1:

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Set memory partition mode
            $ sudo amd-smi set --memory-partition NPS1  

      .. tab-item:: Shell output

         ::

            GPU: 0
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 1
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 2
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 3
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 4
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 5
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 6
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 7
                MEMORY_PARTITION: Successfully set memory partition to NPS1

Once complete, you can safely reset compute partitioning to SPX mode.
   
d. All 64 GPUs not visible in `amd-smi` output in CPX mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In CPX mode, the system should expose 64 logical GPUs (8 per physical MI300X device). If you observe fewer GPUs, it may be due to a known Linux kernel issue involving the AST virtual video driver.

**Resolution:**

Unload the AST video driver and reload the AMD GPU kernel modules:

.. code-block:: bash
  
    # Unload the BMC virtual video driver
    sudo modprobe -r ast

    # Unload the amdgpu driver
    sudo modprobe -r amdgpu

    # Load the amdgpu driver
    sudo modprobe amdgpu

After these steps, rerun `amd-smi` to verify that all 64 GPUs are now visible.

.. note::
   If the AST driver cannot be unloaded due to it being in use, consider blacklisting the AST module in `/etc/modprobe.d/blacklist.conf` and rebooting the system.


5. Steps to run a VLLM workloads
--------------------------------

- This section demonstrates how to validate your MI300X GPU partitioning setup by running a real-world inference workload using vLLM, a high-throughput and memory-efficient LLM inference engine.
- The workload is executed inside an AMD-provided ROCm Docker container and uses the ROCm/MAD benchmarking suite.

a. One-Time Setup

Pull the prebuilt AMD container for vLLM workloads. This container includes all necessary ROCm libraries and pre-installed dependencies.

.. code-block:: bash
  
    # one time setup
    docker pull rocm/vllm:instinct_main

b. Launching the Container

Run the container with the required privileges and device mappings to enable GPU access:

.. code-block:: bash

    # run the docker image and open a bash terminal
    docker run -it --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device /dev/kfd --device /dev/dri rocm/vllm:instinct_main /bin/bash

c. Cloning the Benchmark Suite

Inside the container, clone the ROCm/MAD repository and navigate to the vllm benchmarking script directory:

.. code-block:: bash

    # run the vllm workload from inside the docker image
    git clone https://github.com/ROCm/MAD.git
    cd MAD/scripts/vllm

d. Authentication – Hugging Face Token

To download LLM models such as `Llama-3`, you need a Hugging Face account and an access token.
Create a Hugging Face account and generate a personal access token from your Hugging Face profile. Then export it:

.. code-block:: bash

    #create Hugging Face account and use that token below
    export HF_TOKEN="your_HugginFace_token"

This token is used to pull LLM models (e.g., Llama-3) from Hugging Face.

e. GPU Selection (Optional)

If you wish to limit the vLLM workload to a specific set of GPUs (e.g., 8 out of the total available), define the HIP_VISIBLE_DEVICES environment variable. If left unset, all GPUs are utilized.

.. code-block:: bash

    # set the environment variables for the GPUs to be used
    # leave this bvlank if you want to use all GPUs
    # to used the first 8 GPUs, set the variable to 0,1,2,3,4,5,6,7
    export HIP_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

f. Running the vLLM Benchmark

The benchmark script accepts several command-line options to customize the test. Here's an example that runs the meta-llama/Llama-3.1-8B-Instruct model on 8 GPUs in FP16 mode:

.. code-block:: bash

    #from the app/MAD/scripts/vllm directory, run the following command to run the vllm workload
    # -g 1 means to use 1 GPU, -g 8 means to use 8 GPUs, etc.
    # please refer to the README on the ROCm/MAD github repo for more details on the command line options
    ./vllm_benchmark_report.sh -s all -m meta-llama/Llama-3.1-8B-Instruct -g 8 -d float16


**Command Breakdown:**

- `-s all`: Run all benchmark tests (latency, throughput, etc.)
- `-m`: Hugging Face model name to use (e.g., `meta-llama/Llama-3.1-8B-Instruct`)
- `-g`: Number of GPUs to use
- `-d`: Precision mode (choose from `float16`, `bfloat16`, `float32`)

For additional options (e.g., batch size, sequence length, tokenizer config), refer to the `MAD/scripts/vllm/README.md` file in the GitHub repository.

.. note::
   Ensure that your container has internet access to pull models from Hugging Face during benchmarking.