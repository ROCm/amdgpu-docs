.. meta::
  :description: Post-installation instructions
  :keywords: AMDGPU driver install, installation instructions, AMD, AMDGPU, driver

*************************************************************************
Post-installation instructions
*************************************************************************

.. _verfify_amdgpu:

Verify kernel-mode driver installation
=========================================================================

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

    .. tab-item:: SLES

        .. code-block:: bash

            sudo dkms status

    .. tab-item:: AZL

        .. code-block:: bash

            modinfo amdgpu | grep -w "version:"

Sample output:
-------------------------------------------------------------------------

.. code-block:: bash

    amdgpu/6.12.12-2133686.22.04, 6.8.0-52-generic, x86_64: installed

- ``amdgpu``: dkms module name \
- ``6.12.12``: amdgpu driver version
- ``2133686``: amdgpu build number
- ``22.04``: distro version
- ``6.8.0-52-generic``: kernel version of dkms build
- ``installed``: dkms status; "installed" indicates successful installation of amdgpu driver

.. _other_resources:

Additional software for userspace
=========================================================================

The following resources provide information about user space software:

- `ROCm components <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>`_
- `ROCm installation guide (Linux) <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/>`_
- `ROCm installation guide (Windows) <https://rocm.docs.amd.com/projects/install-on-windows/en/latest/>`_
- `HIP documentation <https://rocm.docs.amd.com/projects/HIP/en/latest/index.html>`_
