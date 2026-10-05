.. meta::
  :description: Post-installation instructions
  :keywords: AMDGPU driver post install, installation instructions, AMD, AMDGPU, driver

*************************************************************************
Post-installation instructions
*************************************************************************

.. _verfify_amdgpu:

Verify kernel-mode driver installation
=========================================================================

Use the following command to check the installation of the AMD GPU Driver (amdgpu):

.. tab-set::

    .. tab-item:: Ubuntu

        .. code-block:: bash

            sudo dkms status

        **Sample output for Ubuntu 26.04:**

        .. code-block:: bash

            amdgpu/7.1.9-2407772.26.04, 7.0.0-30-generic, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``7.1.9``: amdgpu driver version
        - ``2407772``: amdgpu driver build number
        - ``26.04``: distro version
        - ``7.0.0-30-generic``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Debian

        .. code-block:: bash

            sudo dkms status

        **Sample output for Debian 13:**

        .. code-block:: bash

            amdgpu/7.1.9-2407772.24.04, 6.12.107+deb13-amd64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``7.1.9``: amdgpu driver version
        - ``2407772``: amdgpu driver build number
        - ``24.04``: distro version
        - ``6.12.107+deb13-amd64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: RHEL

        .. code-block:: bash

            sudo dkms status

        **Sample output for RHEL 10.2:**

        .. code-block:: bash

            amdgpu/7.1.9-2407772.el10, 6.12.0-211.61.1.el10_2.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``7.1.9``: amdgpu driver version
        - ``2407772``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-211.61.1.el10_2.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: OL

        .. code-block:: bash

            sudo dkms status

        **Sample output for OL 10.2:**

        .. code-block:: bash

            amdgpu/7.1.9-2407772.el10, 6.12.0-206.104.4.4.el10uek.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``7.1.9``: amdgpu driver version
        - ``2407772``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-206.104.4.4.el10uek.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Rocky

        .. code-block:: bash

            sudo dkms status

        **Sample output for Rocky 9.8:**

        .. code-block:: bash

            amdgpu/7.1.9-2407772.el9, 5.14.0-687.52.1.el9_8.x86_64, x86_64: installed

        - ``amdgpu``: dkms module name
        - ``7.1.9``: amdgpu driver version
        - ``2407772``: amdgpu driver build number
        - ``el9``: distro version
        - ``5.14.0-687.52.1.el9_8.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: SLES

        .. code-block:: bash

            sudo dkms status

        **Sample output for SLES 16.0:**

        .. code-block:: bash

            amdgpu/7.1.9-2407772, 6.12.0-160000.37-default, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``7.1.9``: amdgpu driver version
        - ``2407772``: amdgpu driver build number
        - ``6.12.0-160000.37-default``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

.. _other_resources:

Additional software for user space
=========================================================================

The AMD ROCm platform provides a comprehensive set of user space software components for GPU-accelerated computing. See the following resources:

- `ROCm installation guide <https://rocm.docs.amd.com/en/latest/install/rocm.html>`_
- `HIP documentation <https://rocm.docs.amd.com/projects/HIP/en/latest/index.html>`_

.. _disable-ais:

AIS (AMD Infinity Storage)
==========================

When the AMD GPU driver initializes `AIS (AMD Infinity Storage) <https://rocm.docs.amd.com/en/latest/components/storage-libs.html>`_, it registers the GPU's VRAM with the P2PDMA kernel subsystem. This generates about 1GB of metadata for every 64GB of VRAM. This metadata is stored in the host's DRAM.

If you don't need AIS, you can reclaim this memory by disabling AIS from being initialized by the GPU driver.

To disable AIS until next reboot:

.. code:: shell

   sudo modprobe -r amdgpu
   sudo modprobe amdgpu ais_disabled=1

To disable AIS persistently across reboots:

.. code:: shell

   sudo bash -c 'echo "options amdgpu ais_disabled=1" > /etc/modprobe.d/amdgpu-ais.conf'
   sudo update-initramfs -c -k all
   sudo systemctl reboot

To re-enable AIS until next reboot:

.. code:: shell

   sudo modprobe -r amdgpu
   sudo modprobe amdgpu ais_disabled=0

To re-enable AIS persistently across reboots:

.. code:: shell

   sudo rm /etc/modprobe.d/amdgpu-ais.conf
   sudo update-initramfs -c -k all
   sudo systemctl reboot
