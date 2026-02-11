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

            amdgpu/6.18.4-2286447.24.04, 6.17.0-14-generic, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.18.4``: amdgpu driver version
        - ``2286447``: amdgpu driver build number
        - ``24.04``: distro version
        - ``6.17.0-14-generic``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Debian

        .. code-block:: bash

            sudo dkms status

        **Sample output for Debian 13:**

        .. code-block:: bash

            amdgpu/6.18.4-2286447.24.04, 6.12.57+deb13-amd64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name 
        - ``6.18.4``: amdgpu driver version
        - ``2286447``: amdgpu driver build number
        - ``6.12.57+deb13-amd64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: RHEL

        .. code-block:: bash

            sudo dkms status

        **Sample output for RHEL 10.1:**

        .. code-block:: bash

            amdgpu/6.18.4-2286447.el10, 6.12.0-124.8.1.el10_1.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name 
        - ``6.18.4``: amdgpu driver version
        - ``2286447``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-124.8.1.el10_1.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: OL

        .. code-block:: bash

            sudo dkms status

        **Sample output for OL 10.1:**

        .. code-block:: bash

            amdgpu/6.18.4-2286447.el10, 6.12.0-105.51.5.el10uek.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name 
        - ``6.18.4``: amdgpu driver version
        - ``2286447``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-105.51.5.el10uek.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Rocky

        .. code-block:: bash

            sudo dkms status

        **Sample output for Rocky 9.7:**

        .. code-block:: bash

            amdgpu/6.18.4-2286447.el9, 5.14.0-611.5.1.el9_7.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name 
        - ``6.18.4``: amdgpu driver version
        - ``2286447``: amdgpu driver build number
        - ``el9``: distro version
        - ``5.14.0-611.5.1.el9_7.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: SLES

        .. code-block:: bash

            sudo dkms status

        **Sample output for SLES 16.0:**

        .. code-block:: bash

            amdgpu/6.18.4-2286447, 6.12.0-160000.9-default, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name 
        - ``6.18.4``: amdgpu driver version
        - ``2286447``: amdgpu driver build number
        - ``6.12.0-160000.9-default``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

.. _other_resources:

Additional software for user space
=========================================================================

The AMD ROCm platform provides a comprehensive set of user space software components for GPU-accelerated computing. See the following resources:

- `ROCm components <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>`_
- `ROCm installation guide (Linux) <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/>`_
- `HIP documentation <https://rocm.docs.amd.com/projects/HIP/en/latest/index.html>`_
