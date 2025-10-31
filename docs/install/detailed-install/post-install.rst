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

            amdgpu/6.14.14-2212064.24.04, 6.14.0-29-generic, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2212064``: amdgpu driver build number
        - ``24.04``: distro version
        - ``6.14.0-29-generic``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Debian

        .. code-block:: bash

            sudo dkms status

        **Sample output for Debian 12:**

        .. code-block:: bash

            amdgpu/6.14.14-2212064.22.04, 6.1.0-39-amd64, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2212064``: amdgpu driver build number
        - ``6.1.0-39-amd64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: RHEL

        .. code-block:: bash

            sudo dkms status

        **Sample output for RHEL 9.6:**

        .. code-block:: bash

            amdgpu/6.14.14-2212064.el9, 5.14.0-570.44.1.el9_6.x86_64, x86_64: installed (original_module exists)

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2212064``: amdgpu driver build number
        - ``el9``: distro version
        - ``5.14.0-570.44.1.el9_6.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: OL

        .. code-block:: bash

            sudo dkms status

        **Sample output for OL 9.6:**

        .. code-block:: bash

            amdgpu/6.14.14-2212064.el9, 6.12.0-103.40.4.2.el9uek.x86_64, x86_64: installed (original_module exists)

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2212064``: amdgpu driver build number
        - ``el9``: distro version
        - ``6.12.0-103.40.4.2.el9uek.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Rocky

        .. code-block:: bash

            sudo dkms status

        **Sample output for Rocky 9.6:**

        .. code-block:: bash

            amdgpu/6.14.14-2212064.el9, 5.14.0-570.39.1.el9_6.x86_64, x86_64: installed

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2212064``: amdgpu driver build number
        - ``el9``: distro version
        - ``5.14.0-570.39.1.el9_6.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: SLES

        .. code-block:: bash

            sudo dkms status

        **Sample output for SLES 15.7:**

        .. code-block:: bash

            amdgpu/6.14.14-2212064, 6.4.0-150700.53.11-default, x86_64: installed (original_module exists)

        - ``amdgpu``: dkms module name 
        - ``6.14.14``: amdgpu driver version
        - ``2212064``: amdgpu driver build number
        - ``6.4.0-150700.53.11-default``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

.. _other_resources:

Additional software for user space
=========================================================================

The AMD ROCm platform provides a comprehensive set of user space software components for GPU-accelerated computing. See the following resources:

- `ROCm components <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>`_
- `ROCm installation guide (Linux) <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/>`_
- `HIP documentation <https://rocm.docs.amd.com/projects/HIP/en/latest/index.html>`_
