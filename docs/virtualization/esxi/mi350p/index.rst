.. meta::
   :description: AMD Instinct MI350P GPU passthrough on VMware ESXi
   :keywords: AMD, MI350P, ESXi, passthrough, DirectPath, virtualization, Ubuntu

*******************************************
AMD Instinct MI350P on VMware ESXi
*******************************************

The AMD Instinct MI350P GPU supports high-performance AI and HPC workloads in data center environments. When you deploy MI350P GPUs under VMware ESXi, you can assign them to guest virtual machines using **DirectPath I/O** (PCI passthrough), giving the guest operating system direct control over the GPU.

This guide documents the validated workflow for MI350P passthrough on **VMware ESXi 9.1**. The procedures also apply to other releases in the ESXi 9.x family, but ESXi 9.1 is the version used and validated throughout this documentation. The guest operating system used in this guide is **Ubuntu 24.04**.

The documentation covers the complete lifecycle from hypervisor preparation through guest VM configuration and ROCm stack installation:

- :doc:`Passthrough overview <overview>`: DirectPath I/O concepts, requirements, and how ESXi passthrough differs from Linux VFIO.
- :doc:`ESXi host setup <host-setup>`: Access the ESXi web UI, enable SSH, and toggle passthrough for MI350P GPUs.
- :doc:`Ubuntu 24.04 guest setup <ubuntu-guest-setup>`: Create the VM, size the MMIO aperture, assign GPUs, and pre-configure the guest.
- :doc:`Install ROCm and the AMD GPU driver <install-rocm>`: Install ROCm and the AMDGPU driver in the guest, and resolve Secure Boot issues.
- :doc:`External resources <external-resources>`: Related documentation and support sites cited in this guide.

Whether you are standing up a single-GPU development VM or assigning multiple MI350P devices to a multi-GPU compute guest, this guide is your reference for validated ESXi passthrough configuration on MI350P hardware.
