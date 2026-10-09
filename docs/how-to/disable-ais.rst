.. meta::
  :description: Enable or disable AMD Infinity Storage (AIS)
  :keywords: AIS, AMD Infinity Storage, ais_disabled, amdgpu, P2PDMA, VRAM

.. _disable-ais:

***********
Disable AIS
***********

`AIS (AMD Infinity Storage) <https://rocm.docs.amd.com/projects/hipFile/en/latest/conceptual/amd-infinity-storage.html>`_
is an AMD storage technology that enables GPU-accelerated direct access to NVMe storage.
When the AMD GPU driver initializes AIS, it registers the GPU's VRAM with the P2PDMA kernel
subsystem. This generates approximately 1 GB of ``MEMORY_DEVICE_PCI_P2PDMA`` metadata pages
per 64 GB of VRAM, stored in host DRAM.

AIS is enabled by default. If you don’t need AIS, you can reclaim this memory by disabling AIS from being initialized by the GPU driver.

Disable AIS
===========

To disable AIS until next reboot:

.. code:: shell

   sudo modprobe -r amdgpu
   sudo modprobe amdgpu ais_disabled=1

To disable AIS persistently across reboots:

.. code:: shell

   sudo bash -c 'echo "options amdgpu ais_disabled=1" > /etc/modprobe.d/amdgpu-ais.conf'
   sudo update-initramfs -c -k all
   sudo systemctl reboot

Re-enable AIS
=============

To re-enable AIS until next reboot:

.. code:: shell

   sudo modprobe -r amdgpu
   sudo modprobe amdgpu ais_disabled=0

To re-enable AIS persistently across reboots:

.. code:: shell

   sudo rm /etc/modprobe.d/amdgpu-ais.conf
   sudo update-initramfs -c -k all
   sudo systemctl reboot
