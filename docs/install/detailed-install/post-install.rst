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

            amdgpu/6.14.14-2222715.24.04, 6.14.0-32-generic, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2222715``: amdgpu driver build number
        - ``24.04``: distro version
        - ``6.14.0-32-generic``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Debian

        .. code-block:: bash

            sudo dkms status

        **Sample output for Debian 12:**

        .. code-block:: bash

            amdgpu/6.14.14-2222715.22.04, 6.1.0-40-amd64, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2222715``: amdgpu driver build number
        - ``6.1.0-40-amd64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: RHEL

        .. code-block:: bash

            sudo dkms status

        **Sample output for RHEL 10.0:**

        .. code-block:: bash

            amdgpu/6.14.14-2222715.el10, 6.12.0-55.34.1.el10_0.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2222715``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-55.34.1.el10_0.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: OL

        .. code-block:: bash

            sudo dkms status

        **Sample output for OL 10.0:**

        .. code-block:: bash

            amdgpu/6.14.14-2222715.el10, 6.12.0-103.40.4.3.el10uek.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2222715``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-103.40.4.3.el10uek.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Rocky

        .. code-block:: bash

            sudo dkms status

        **Sample output for Rocky 9.6:**

        .. code-block:: bash

            amdgpu/6.14.14-2222715.el9, 5.14.0-570.42.2.el9_6.x86_64, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2222715``: amdgpu driver build number
        - ``el9``: distro version
        - ``5.14.0-570.42.2.el9_6.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: SLES

        .. code-block:: bash

            sudo dkms status

        **Sample output for SLES 15.7:**

        .. code-block:: bash

            amdgpu/6.14.14-2222715, 6.4.0-150700.53.16-default, x86_64: installed (original_module exists)

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2222715``: amdgpu driver build number
        - ``6.4.0-150700.53.16-default``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: AZL

        .. code-block:: bash

            modinfo amdgpu | grep -w "version:"

        **Sample output for AZL 3.0:**

        .. code-block:: bash

            version:        6.8.5

        - ``6.8.5``: amdgpu driver version

.. _other_resources:

Additional software for user space
=========================================================================

The AMD ROCm platform provides a comprehensive set of user space software components for GPU-accelerated computing. See the following resources:

- `ROCm components <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>`_
- `ROCm installation guide (Linux) <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/>`_
- `HIP documentation <https://rocm.docs.amd.com/projects/HIP/en/latest/index.html>`_
