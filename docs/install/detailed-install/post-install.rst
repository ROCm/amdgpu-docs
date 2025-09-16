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

    .. tab-item:: Debian

        .. code-block:: bash

            sudo dkms status

    .. tab-item:: RHEL

        .. code-block:: bash

            sudo dkms status

    .. tab-item:: OL

        .. code-block:: bash

            sudo dkms status

    .. tab-item:: Rocky

        .. code-block:: bash

            sudo dkms status

    .. tab-item:: SLES

        .. code-block:: bash

            sudo dkms status

    .. tab-item:: AZL

        .. code-block:: bash

            modinfo amdgpu | grep -w "version:"

**Sample output for Ubuntu 24.04:**

.. code-block:: bash

    amdgpu/6.14.14-2204008.24.04, 6.14.0-29-generic, x86_64: installed

- ``amdgpu``: dkms module name 
- ``6.14.14``: amdgpu driver version
- ``2204008``: amdgpu driver build number
- ``24.04``: distro version
- ``6.14.0-29-generic``: kernel version of dkms build
- ``installed``: dkms status; ``installed`` indicates successful installation of the amdgpu driver

.. _other_resources:

Additional software for user space
=========================================================================

The AMD ROCm platform provides a comprehensive set of user space software components for GPU-accelerated computing. See the following resources:

- `ROCm components <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>`_
- `ROCm installation guide (Linux) <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/>`_
- `HIP documentation <https://rocm.docs.amd.com/projects/HIP/en/latest/index.html>`_
