.. meta::
  :description: Enable or disable AMD Infinity Storage (AIS)
  :keywords: AIS, AMD Infinity Storage, ais_disabled, amdgpu, P2PDMA, VRAM

.. _disable-ais:

***********
Disable AIS
***********

When the AMD GPU driver initializes `AIS (AMD Infinity Storage) <https://rocm.docs.amd.com/projects/hipFile/en/latest/conceptual/amd-infinity-storage.html>`_, it registers the GPU's VRAM with the P2PDMA kernel
subsystem. This generates about 1GB of metadata for every 64GB of VRAM. This metadata is stored in the host’s DRAM.

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
