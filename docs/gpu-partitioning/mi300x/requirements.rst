**************************************
Requirements to partition MI300X GPUs
**************************************

Partitioning AMD Instinct™ MI300X GPUs is a critical enabler for modern heterogeneous computing environments where isolation, resource sharing, and workload-specific optimization are paramount. By dividing a single physical GPU into multiple logical partitions, developers and system administrators can tailor computational resources to meet the unique performance, memory, and security demands of diverse applications—including large-scale AI inference, training, HPC simulations, and cloud-native deployments.

This document provides a comprehensive overview of the system, software, and firmware requirements needed to successfully configure and operate GPU partitioning on MI300X devices. Partitioning support for the MI300X platform is tightly integrated with the ROCm software stack and relies on both hardware-level and OS-level infrastructure. As such, careful attention must be given to platform readiness, including validated driver versions, kernel support, supported memory modes, and compatibility with partitioning utilities such as ``amd-smi``.

Users should ensure their system environment meets all listed prerequisites prior to attempting partition configuration. Failure to do so may result in incomplete GPU enumeration, missing partitioning capabilities, or instability during execution.

This guide is intended for system integrators, developers, platform architects, and IT administrators tasked with deploying MI300X-based platforms in bare-metal, production-grade environments. All configurations, tools, and commands referenced herein have been validated on supported operating systems and are based on ROCm version 6.4 or newer.

Prerequisites
-------------

- AMD Instinct MI300X GPUs must be installed and recognized by the system.
- ROCm software stack must be correctly installed.
- Firmware and kernel must support partitioning (latest recommended).
- ``amd-smi`` tool is required for runtime management.
- Bare-metal OS installation—no virtualization layer.

System requirements
-------------------

To ensure successful partitioning with MI300X GPUs, confirm the following system requirements:

Hardware requirements
~~~~~~~~~~~~~~~~~~~~~

- **GPU**: AMD Instinct MI300X

Operating system requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following Linux distributions are recommended:

- Ubuntu 22.04+, 24.04+
- Oracle Linux Server 8.8+

To check the operating system version, run the following command.

.. tab-set::

   .. tab-item:: Command

      .. code-block:: shell

         uname -m && cat /etc/*release

   .. tab-item:: Shell output

      .. code-block:: shell-session

         x86_64
         DISTRIB_ID=Ubuntu
         DISTRIB_RELEASE=24.04
         DISTRIB_CODENAME=noble
         DISTRIB_DESCRIPTION="Ubuntu 24.04 LTS"
         PRETTY_NAME="Ubuntu 24.04 LTS"
         NAME="Ubuntu"
         VERSION_ID="24.04"
         VERSION="24.04 LTS (Noble Numbat)"
         VERSION_CODENAME=noble
         ID=ubuntu
         ID_LIKE=debian

         ... [output truncated]

Software requirements
~~~~~~~~~~~~~~~~~~~~~

- **Linux kernel**: version 5.15 or newer

  To find the kernel version, run the following command.

  .. tab-set::

     .. tab-item:: Command

        .. code-block:: shell

           # Check Linux kernel version
           uname -srmv

     .. tab-item:: Shell output

        .. code-block:: shell-session

           Linux 6.8.0-31-generic #31-Ubuntu SMP PREEMPT_DYNAMIC Sat Apr 20 00:40:06 UTC 2024 x86_64

- ``amd-smi`` **CLI**: version 25.3.0 or newer

- **ROCm**: version 6.4 or newer

- **AMD GPU Driver (amdgpu)**: version 6.12.12 (amdgpu-build 2120656) or newer

  To find the AMD SMI, ROCm, and amdgpu driver versions, run ``amd-smi`` or ``amd-smi version``.

  .. tab-set::

     .. tab-item:: Command

        .. code-block:: shell-session

           amd-smi

     .. tab-item:: Shell output

        .. code-block:: shell-session

           +------------------------------------------------------------------------------+
           | AMD-SMI 26.0.0+37d158ab      amdgpu version: 6.14.14  ROCm version: 7.0.1    |
           | Platform: Linux Baremetal                                                    |
           |-------------------------------------+----------------------------------------|

           ... [output truncated]


Firmware requirements
~~~~~~~~~~~~~~~~~~~~~

- **VBIOS**: version 022.040.003.043.000001

  To find the VBIOS version, run the following command.

  .. tab-set::

     .. tab-item:: Command

        .. code-block:: shell

           amd-smi static --vbios

     .. tab-item:: Shell output

        .. code-block:: shell-session

           GPU: 0
               VBIOS:
                   NAME: AMD MI300X_HW_SRIOV_CVS_1VF
                   BUILD_DATE: 2024/10/17 16:32
                   PART_NUMBER: 113-M3000100-103
                   VERSION: 022.040.003.043.000001
