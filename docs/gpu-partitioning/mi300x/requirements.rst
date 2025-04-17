Requirements to Partition MI300X GPUs
======================================

Partitioning AMD Instinct™ MI300X GPUs is a critical enabler for modern heterogeneous computing environments where isolation, resource sharing, and workload-specific optimization are paramount. By dividing a single physical GPU into multiple logical partitions, developers and system administrators can tailor computational resources to meet the unique performance, memory, and security demands of diverse applications—including large-scale AI inference, training, HPC simulations, and cloud-native deployments.

This document provides a comprehensive overview of the system, software, and firmware requirements needed to successfully configure and operate GPU partitioning on MI300X devices. Partitioning support for the MI300X platform is tightly integrated with the ROCm software stack and relies on both hardware-level and OS-level infrastructure. As such, careful attention must be given to platform readiness, including validated driver versions, kernel support, supported memory modes, and compatibility with partitioning utilities such as `amd-smi`.

Users should ensure their system environment meets all listed prerequisites prior to attempting partition configuration. Failure to do so may result in incomplete GPU enumeration, missing partitioning capabilities, or instability during execution.

This guide is intended for system integrators, developers, platform architects, and IT administrators tasked with deploying MI300X-based platforms in bare-metal, production-grade environments. All configurations, tools, and commands referenced herein have been validated on supported operating systems and are based on ROCm version 6.4 or newer.

1. Prerequisites
-----------------

- MI300X GPUs must be installed and recognized by the system.
- ROCm stack must be correctly installed.
- Firmware and kernel must support partitioning (latest recommended).
- `amd-smi` tool is required for runtime management.
- Bare-metal OS installation—no virtualization layer.

2. System Requirements
----------------------

To ensure a successful partitioning experience with MI300X GPUs, confirm the following system requirements:

a. Hardware Requirements
~~~~~~~~~~~~~~~~~~~~~~~~

- **GPU**: AMD MI300X

b. Software Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Linux Kernel**: Version 5.15 or newer

  #. to find the kernel version, run the following command 

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check Linux kernel version
            hostnamectl | grep 'Kernel'

      .. tab-item:: Shell output

         ::

            Kernel: Linux 5.15.0-134-generic

- **AMDSMI Tool Library**: Version 25.3.0 or newer

  #. to find the amdsmi version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check AMD-SMI version
            amd-smi version | grep -o 'AMDSMI [^|]*'

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
            amd-smi version | grep -o 'amdgpu version: [^|]*'

      .. tab-item:: Shell output

         ::

            amdgpu version: 6.12.12


c. Firmware Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

- **VBIOS Version**:  022.040.003.043.000001

  #. to find the VBIOS version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check VBIOS version
            amd-smi static | grep -A 4 -m 1 'VBIOS'

      .. tab-item:: Shell output

         ::

            VBIOS:
              NAME: AMD MI300X_HW_SRIOV_CVS_1VF
              BUILD_DATE: 2024/09/25 10:52
              PART_NUMBER: 113-M3000100-102
              VERSION: 022.040.003.042.000001

d. Operating System Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Ubuntu 22.04+, 24.04+
- Oracle Linux Server 8.8+

  #. to check the operating system version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check Operating System version
            hostnamectl | grep 'Operating System'

      .. tab-item:: Shell output

         ::

            Operating System: Ubuntu 22.04.5 LTS

e. Driver Requirements
~~~~~~~~~~~~~~~~~~~~~~~

- **ROCm**: Version 6.4 or newer

  #. to find the ROCm version, run the following command

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check ROCm version
            amd-smi version | grep -o 'ROCm version: [^|]*'

      .. tab-item:: Shell output

         ::

            ROCm version: 6.4.0
