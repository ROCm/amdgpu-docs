.. meta::
   :description: Known issue where the amdgpu driver fails to detect PCIe AtomicOp support on ESXi DirectPath I/O guests.
   :keywords: AMD, MI350P, ESXi, DirectPath I/O, PCIe atomics, AtomicOp, known issue, Ubuntu, kernel regression

Known issues
============

PCIe atomics not detected on ESXi DirectPath I/O
------------------------------------------------

On ESXi DirectPath I/O (passthrough) guests, the amdgpu driver may fail to detect Peripheral Component Interconnect Express (PCIe) AtomicOp support even when the hardware provides it. ROCm and HIP workloads that depend on CPU to GPU atomics or fine-grained synchronization over system memory can then fall back to slower paths or fail.

For background on how ROCm uses PCIe atomics, see :doc:`How ROCm uses PCIe atomics <../../../conceptual/pcie-atomics>`.

Affected kernels
----------------

This is a Linux kernel regression in ``pci_enable_atomic_ops_to_root()``. On Ubuntu it first appears in the ``6.8.0-135-generic`` ABI update and is present in later 6.8 kernels (for example, ``6.8.0-138-generic``). Because it arrived as an ABI update, the same change is also in newer kernel series that picked up that update. Kernels older than the ``-135`` ABI (for example, ``6.8.0-100-generic``) are not affected.

How to check
------------

To check the running kernel, load ``amdgpu`` and run the following command:

.. tab-set::

   .. tab-item:: Command

      .. code-block:: shell-session

         sudo dmesg | grep atomic

   .. tab-item:: Affected output

      ::

         PCIE atomic ops is not supported

If the log contains ``PCIE atomic ops is not supported``, the issue is present.

Status and workaround
---------------------

A fix is accepted upstream and awaiting merge and backport. See the patch series `PCI: Accept AtomicOps already enabled by the hypervisor <https://patchew.org/linux/20260921111903.978687-1-nikprica@amd.com/>`_.

Until a kernel with that fix is available, boot a kernel older than the ``-135`` ABI.
