.. meta::
   :description: DirectPath I/O passthrough concepts and requirements for AMD Instinct MI350P GPUs on VMware ESXi.
   :keywords: AMD, MI350P, ESXi, passthrough, DirectPath I/O, PCI passthrough, IOMMU, VFIO, virtualization

MI350P ESXi passthrough overview
=================================

About DirectPath I/O passthrough
---------------------------------

DirectPath I/O (also known as PCI passthrough) is VMware ESXi's native technology for providing virtual machines with direct access to physical PCI or PCIe devices. This feature allows guest operating systems to directly control and communicate with PCI devices, bypassing the ESXi hypervisor's involvement in I/O operations.

For MI350P GPU passthrough on ESXi, DirectPath I/O is the fundamental mechanism. It requires hardware support through Intel VT-d or AMD IOMMU (AMD-Vi) and proper BIOS or UEFI configuration.

The passthrough implementation in ESXi differs from VFIO in Linux because it is integrated directly into the hypervisor architecture. This integration offers device assignment while maintaining ESXi's security and isolation model. Direct assignment provides near-native performance for GPU workloads, which suits compute-intensive applications that require full GPU access.

This guide targets **VMware ESXi 9.1**. The procedures also apply to other releases in the ESXi 9.x family, but ESXi 9.1 is the version used and validated throughout this document.

DirectPath I/O requirements
----------------------------

DirectPath I/O requires the following:

- **CPU support for I/O virtualization:** Intel VT-d or AMD-Vi (AMD IOMMU).
- **Motherboard or BIOS support for IOMMU:** You must enable IOMMU in the system firmware.
- **ESXi version compatible with the target GPU:** This guide validates ESXi 9.1. Other ESXi 9.x releases may work with similar procedures.
- **Proper GPU driver support in the guest operating system:** The guest must run a supported Linux distribution with the AMDGPU driver and ROCm stack. This guide uses Ubuntu 24.04.

.. important::
   For background on IOMMU and how it enables safe device assignment, see :doc:`Input-Output Memory Management Unit (IOMMU) <../../../conceptual/iommu>`.

Passthrough workflow
--------------------

The remaining sections of this guide follow the order of operations for a successful MI350P passthrough deployment:

#. **ESXi host setup:** Prepare the hypervisor by enabling SSH access and toggling passthrough mode for MI350P GPUs under PCI Devices.
#. **Ubuntu 24.04 guest setup:** Create the virtual machine, configure MMIO passthrough parameters, assign PCI devices, and prepare the guest operating system before driver installation.
#. **Install ROCm and the AMD GPU driver:** Install the AMDGPU driver and ROCm components in the guest after the GPU is detected with ``lspci``.

Each step includes command examples, configuration parameters, and validation checkpoints to confirm successful completion before you proceed.
