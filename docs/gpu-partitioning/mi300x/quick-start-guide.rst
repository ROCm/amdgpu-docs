Quick Start Guide to Partitioning MI300X GPUs
==============================================

This guide serves as a practical and technically detailed reference for configuring compute and memory partitioning on AMD Instinct™ MI300X GPUs using the `amd-smi` utility. Partitioning is a key feature that enables system administrators, developers, and data center operators to dynamically subdivide a single MI300X GPU into multiple logical devices—each with its own dedicated compute and memory resources. This empowers users to maximize resource utilization, improve workload isolation, and optimize performance for diverse AI, HPC, and multi-tenant cloud environments.

Partitioning on MI300X involves two dimensions:

- **Compute Partitioning**: Divides the GPU’s compute units (XCDs) into isolated logical devices. For example, CPX mode creates eight independent compute partitions per GPU.
- **Memory Partitioning**: Splits the high-bandwidth memory (HBM) into physically separated addressable regions. NPS4 mode, for instance, creates four memory partitions of 48GB each.

When used together, compute and memory partitioning modes such as CPX/NPS4 enable fine-grained allocation of GPU resources to individual workloads, enhancing security and manageability while maintaining high throughput.

This Quick Start Guide walks through the necessary steps to create, verify, modify, and delete GPU partitions using standard system-level tools. Each step is accompanied by real command-line examples, expected outputs, and actionable notes to help ensure successful execution.

Whether you are deploying MI300X GPUs for large-scale language model inference, cloud-native AI services, or isolated multi-user compute environments, understanding and leveraging GPU partitioning is essential for unlocking the full flexibility and efficiency of the Instinct platform.


1. Creating CPX/NPS4 Partition
-------------------------------
    
    - This section describes how to create a CPX/NPS4 partition on MI300X GPUs using the `amd-smi` tool.
    - The partitioning process involves setting compute and memory partitioning modes to CPX and NPS4, respectively.
    - The example below demonstrates how to set up a CPX/NPS4 partition on all GPUs in the system. 

To create a CPX/NPS4 partition:

a. **Set compute partitioning mode to CPX:**


   .. tab-set::

      .. tab-item:: Compute Partition Command

         .. code-block:: shell-session

            # Set compute partition mode
            sudo amd-smi set --gpu all --compute-partition CPX    

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

.. tip::

   On MI300X, memory partitioning requires that the number of memory partitions not exceed the number of compute partitions. As a result, the **SPX+NPS4** configuration is invalid.

   When switching from **SPX+NPS1** to **CPX+NPS4**, setting the memory partition to **NPS4** will automatically transition the compute partition to **CPX**. You can skip the explicit CPX compute mode step, setting **NPS4** alone is sufficient to configure a valid **CPX+NPS4** partition.

   .. code-block:: shell-session

      sudo amd-smi set --memory-partition NPS4

   This command will internally transition the compute mode from SPX to CPX, followed by the memory mode switch to NPS4 — provided all prerequisites are met and no GPU workloads are active.


b. **Set memory partitioning mode to NPS4:**

   .. tab-set::

      .. tab-item:: Memory Partition Command

         .. code-block:: shell-session

            # Set memory partition mode
            sudo amd-smi set --memory-partition NPS4  

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


2. Verifying Partition Creation
----------------------------------
    
    - After setting the partitioning modes, you can verify the partition creation using the `amd-smi` tool.
    - The command will display the current partitioning status of the GPUs, including compute and memory partitioning modes.

To confirm active partitioning state:

Use `amd-smi` to confirm active partition states:

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check partitioning status
            amd-smi static --partition

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

            GPU: 63
                PARTITION:
                    COMPUTE_PARTITION: CPX
                    MEMORY_PARTITION: NPS4
                    PARTITION_ID: 7

3. Modifying Partitions
------------------------

    - This section describes how to modify the partitioning modes of MI300X GPUs using the `amd-smi` tool.
    - You can switch between compute and memory partitioning modes as needed.
    - The example below demonstrates how to switch between compute and memory partitioning modes.

Use the following commands to switch compute or memory partitioning modes.

**Compute Partition Examples:**

   .. tab-set::

      .. tab-item:: Compute Partition Command

         .. code-block:: shell-session

            # Set compute partition mode
            sudo amd-smi set --gpu all --compute-partition CPX    

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
            sudo amd-smi set --gpu all --compute-partition SPX    

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
            sudo amd-smi set --memory-partition NPS4  

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
            sudo amd-smi set --memory-partition NPS1  

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

4. Deleting Partitions
-----------------------

    - This section describes how to delete or reset the partitioning modes of MI300X GPUs using the `amd-smi` tool.
    - You can revert the partitioning modes to their default settings.
    - The example below demonstrates how to delete or reset the partitioning modes.

To delete or reset partitions, revert both compute and memory partitioning to defaults:

.. code-block:: shell-session

   sudo amd-smi set --gpu all --compute-partition SPX
   sudo amd-smi set --memory-partition NPS1


