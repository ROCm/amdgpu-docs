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

        **Sample output for Ubuntu 24.04:**

        .. code-block:: bash 

            amdgpu/6.16.6-2238411.24.04, 6.14.0-33-generic, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.16.6``: amdgpu driver version
        - ``2238411``: amdgpu driver build number
        - ``24.04``: distro version
        - ``6.14.0-33-generic``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Debian

        .. code-block:: bash

            sudo dkms status

        **Sample output for Debian 13:**

        .. code-block:: bash

            amdgpu/6.16.6-2238411.24.04, 6.12.48+deb13-amd64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name 
        - ``6.16.6``: amdgpu driver version
        - ``2238411``: amdgpu driver build number
        - ``6.12.48+deb13-amd64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: RHEL

        .. code-block:: bash

            sudo dkms status

        **Sample output for RHEL 10.0:**

        .. code-block:: bash

            amdgpu/6.16.6-2238411.el10, 6.12.0-55.41.1.el10_0.x86_64, x86_64: installed (original_module exists)

        - ``amdgpu``: dkms module name 
        - ``6.16.6``: amdgpu driver version
        - ``2238411``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-55.41.1.el10_0.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: OL

        .. code-block:: bash

            sudo dkms status

        **Sample output for OL 10.0:**

        .. code-block:: bash

            amdgpu/6.16.6-2238411.el10, 6.12.0-104.43.4.3.el10uek.x86_64, x86_64: installed (original_module exists)

        - ``amdgpu``: dkms module name 
        - ``6.16.6``: amdgpu driver version
        - ``2238411``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-104.43.4.3.el10uek.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Rocky

        .. code-block:: bash

            sudo dkms status

        **Sample output for Rocky 9.6:**

        .. code-block:: bash

            amdgpu/6.16.6-2238411.el9, 5.14.0-570.49.1.el9_6.x86_64, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.16.6``: amdgpu driver version
        - ``2238411``: amdgpu driver build number
        - ``el9``: distro version
        - ``5.14.0-570.49.1.el9_6.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: SLES

        .. code-block:: bash

            sudo dkms status

        **Sample output for SLES 15.7:**

        .. code-block:: bash

            amdgpu/6.16.6-2238411, 6.4.0-150700.53.19-default, x86_64: installed (original_module exists)

        - ``amdgpu``: dkms module name 
        - ``6.16.6``: amdgpu driver version
        - ``2238411``: amdgpu driver build number
        - ``6.4.0-150700.53.19-default``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

.. _other_resources:

Additional software for user space
=========================================================================

The AMD ROCm platform provides a comprehensive set of user space software components for GPU-accelerated computing. See the following resources:

- `ROCm components <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>`_
- `ROCm installation guide (Linux) <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/>`_
- `HIP documentation <https://rocm.docs.amd.com/projects/HIP/en/latest/index.html>`_
