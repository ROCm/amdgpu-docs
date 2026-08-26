.. meta::
    :description: DC GPU Driver compatibility matrix
    :keywords: GPU, architecture, hardware, compatibility, system, requirements, components, libraries

**************************************************************************************
Compatibility matrix
**************************************************************************************

The AMD GPU Driver (amdgpu) 31.50.0 is compatible with ROCm 10.0.0. For more information, see `ROCm 10.0.0 compatibility matrix
<https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html>`__.

====================================
Operating system and kernel version
====================================

See `Operating system support <https://rocm.docs.amd.com/en/latest/about/release-notes.html#operating-system-support>`_ for ROCm supported operating systems and their kernel versions.

============
GPU support
============

See `Hardware support <https://rocm.docs.amd.com/en/latest/about/release-notes.html#amd-hardware-support>`_ for the list of supported AMD Instinct™, Radeon™ PRO, Radeon, and Ryzen™ AI GPUs.

===============
Virtualization
===============

GPU passthrough on VMware ESXi is documented for AMD Instinct MI350P GPUs. The validated stack includes VMware ESXi 9.x (validated on ESXi 9.1), an Ubuntu 24.04 guest, and the AMDGPU driver and ROCm software stack installed in the guest after passthrough.

For setup instructions, see :doc:`AMD Instinct MI350P on VMware ESXi <../virtualization/esxi/mi350p/index>`.

For bare-metal GPU partitioning, see :doc:`GPU Partitioning <../gpu-partitioning/index>`.
