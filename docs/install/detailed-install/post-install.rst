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

            amdgpu/6.19.14-2377056.26.04, 7.0.0-27-generic, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``6.19.14``: amdgpu driver version
        - ``2377056``: amdgpu driver build number
        - ``26.04``: distro version
        - ``7.0.0-27-generic``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Debian

        .. code-block:: bash

            sudo dkms status

        **Sample output for Debian 13:**

        .. code-block:: bash

            amdgpu/6.19.14-2377056.24.04, 6.12.95+deb13-amd64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``6.19.14``: amdgpu driver version
        - ``2377056``: amdgpu driver build number
        - ``6.12.95+deb13-amd64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: RHEL

        .. code-block:: bash

            sudo dkms status

        **Sample output for RHEL 10.2:**

        .. code-block:: bash

            amdgpu/6.19.14-2377056.el10, 6.12.0-211.33.1.el10_2.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``6.19.14``: amdgpu driver version
        - ``2377056``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-211.33.1.el10_2.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: OL

        .. code-block:: bash

            sudo dkms status

        **Sample output for OL 10.1:**

        .. code-block:: bash

            amdgpu/6.19.14-2377056.el10, 6.12.0-204.92.4.2.el10uek.x86_64, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``6.19.14``: amdgpu driver version
        - ``2377056``: amdgpu driver build number
        - ``el10``: distro version
        - ``6.12.0-204.92.4.2.el10uek.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: Rocky

        .. code-block:: bash

            sudo dkms status

        **Sample output for Rocky 9.7:**

        .. code-block:: bash

            amdgpu/6.19.14-2377056.el9, 5.14.0-687.24.1.el9_8.x86_64, x86_64: installed

        - ``amdgpu``: dkms module name
        - ``6.19.14``: amdgpu driver version
        - ``2377056``: amdgpu driver build number
        - ``el9``: distro version
        - ``5.14.0-687.24.1.el9_8.x86_64``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

    .. tab-item:: SLES

        .. code-block:: bash

            sudo dkms status

        **Sample output for SLES 16.0:**

        .. code-block:: bash

            amdgpu/6.19.14-2377056, 6.12.0-160000.35-default, x86_64: installed (Original modules exist)

        - ``amdgpu``: dkms module name
        - ``6.19.14``: amdgpu driver version
        - ``2377056``: amdgpu driver build number
        - ``6.12.0-160000.35-default``: kernel version of dkms build
        - ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

.. _other_resources:

Additional software for user space
=========================================================================

The AMD ROCm platform provides a comprehensive set of user space software components for GPU-accelerated computing. See the following resources:

- `ROCm installation guide <https://rocm.docs.amd.com/en/latest/install/rocm.html>`_
- `HIP documentation <https://rocm.docs.amd.com/projects/HIP/en/latest/index.html>`_
