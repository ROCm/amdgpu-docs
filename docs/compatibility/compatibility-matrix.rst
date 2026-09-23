.. meta::
    :description: DC GPU Driver compatibility matrix
    :keywords: GPU, architecture, hardware, compatibility, system, requirements, components, libraries

**************************************************************************************
Compatibility matrix
**************************************************************************************

The AMD GPU Driver (amdgpu) is distributed separately from the ROCm software stack and is stored under in its own location ``/amdgpu/`` in the package repository at `repo.radeon.com <https://repo.radeon.com/amdgpu/>`_. Starting from ROCm 6.4.0, forward and backward compatibility between the AMD GPU Driver (amdgpu) and ROCm is provided up to a year apart (assuming hardware support is available in both). For earlier ROCm releases, the compatibility is provided for +/- 2 releases. This table shows the compatibility combinations that are currently supported.

.. note ::

  The supported ROCm versions in the following table are accurate as of the time of publication. For the most up-to-date information about AMD GPU Driver (amdgpu) and supported user space versions, see the latest version of this table at `Compatibility matrix <https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/compatibility/compatibility-matrix.html>`_.

.. csv-table::
  :widths: 30, 70
  :header: "AMD GPU Driver (amdgpu)", "Supported ROCm versions"

    "31.50.x", "7.0.x, 7.1.x, 7.2.x, 7.14.x, 10.0.0"
    "31.40.x", "7.0.x, 7.1.x, 7.2.x, 7.14.x, 10.0.0"
    "30.30.x", "6.3.x, 6.4.x, 7.0.x, 7.1.x, 7.2.x, 7.14.x, 10.0.0"
    "30.20.x", "6.3.x, 6.4.x, 7.0.x, 7.1.x, 7.2.x, 7.14.x, 10.0.0"
    "30.10.x", "6.2.x, 6.3.x, 6.4.x, 7.0.x, 7.1.x, 7.2.x, 7.14.x, 10.0.0"
    "6.4.x", "6.1.x, 6.2.x, 6.3.x, 6.4.x, 7.0.x, 7.1.x, 7.2.x"
    "6.3.x", "6.1.x, 6.2.x, 6.3.x, 6.4.x, 7.0.x"
    "6.2.x", "6.0.x, 6.1.x, 6.2.x, 6.3.x, 6.4.x, 7.0.x"
    "6.1.x", "5.7.x, 6.0.x, 6.1.x, 6.2.x, 6.3.x, 6.4.x"
    "6.0.x", "5.6.x, 5.7.x, 6.0.x, 6.1.x, 6.2.x"
    "5.7.x", "5.5.x, 5.6.x, 5.7.x, 6.0.x, 6.1.x"
    "5.6.x", "5.4.x, 5.5.x, 5.6.x, 5.7.x, 6.0.x"
    "5.5.x", "5.3.x, 5.4.x, 5.5.x, 5.6.x, 5.7.x"
    "5.4.x", "5.2.x, 5.3.x, 5.4.x, 5.5.x, 5.6.x"
    "5.3.x", "5.1.x, 5.2.x, 5.3.x, 5.4.x, 5.5.x"

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
