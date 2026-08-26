.. meta::
   :description: GPU virtualization and passthrough on AMD Instinct platforms.
   :keywords: AMD, GPU, virtualization, passthrough, ESXi, DirectPath, MI350P

*****************************
AMD GPU virtualization
*****************************

AMD Instinct GPUs can be deployed in virtualized environments where guest operating systems require direct access to GPU hardware. This documentation covers validated procedures for exposing AMD GPUs to virtual machines using hypervisor-native passthrough technologies.

About GPU virtualization
^^^^^^^^^^^^^^^^^^^^^^^^

PCI passthrough (also known as DirectPath I/O on VMware ESXi) allows a virtual machine to control a physical PCI or PCIe device directly. The hypervisor assigns the device to the guest, bypassing hypervisor-mediated I/O for that device. When combined with an input-output memory management unit (IOMMU), passthrough provides near-native GPU performance for compute workloads in the guest.

This section includes guides for the following tasks:

- **ESXi host configuration:** Enable SSH, toggle GPU passthrough, and prepare the hypervisor for device assignment.
- **Guest operating system setup:** Create and configure Ubuntu virtual machines with the memory mapped I/O (MMIO) and PCI parameters required for MI350P passthrough.
- **Install ROCm and the AMD GPU driver:** Install the AMDGPU driver and Radeon Open Compute (ROCm) components in the guest after successful GPU detection.

Device documentation
^^^^^^^^^^^^^^^^^^^^

- :doc:`AMD Instinct MI350P on VMware ESXi <esxi/mi350p/index>`: End-to-end guide for MI350P GPU passthrough on VMware ESXi 9.x with an Ubuntu 24.04 guest.

For bare-metal GPU partitioning on AMD Instinct platforms, see :doc:`GPU Partitioning <../gpu-partitioning/index>`.
