.. meta::
  :description: Azure Linux native installation
  :keywords: AMDGPU driver install, AMDGPU driver, driver installation instructions, Azure Linux, Azure Linux native installation, AMD

**********************************************************************************************
Azure Linux native installation
**********************************************************************************************

.. caution::

    Ensure that the :doc:`../prerequisites` are met before installing.

.. _azl-install:

Installing
=====================================================

Install kernel driver
----------------------------------------------------------------------------------------------------------

.. datatemplate:nodata::

    .. tab-set::
        .. tab-item:: Standard install 

            Updates the kernel and installs the latest version of amdgpu to ensure full compatibility.

            .. code-block:: bash

                sudo tdnf install azurelinux-repos-amd
                sudo tdnf repolist --refresh
                sudo tdnf install amdgpu

        .. tab-item:: Safe install

            Keeps your current kernel, but may install an older version of amdgpu.

            .. code-block:: bash

                sudo tdnf install azurelinux-repos-amd 
                sudo tdnf repolist --refresh 
                kernel_version=$(uname -r | tr '-' '.') 
                package_info=$(sudo tdnf list available "amdgpu" | grep "amdgpu" | grep $kernel_version) 
                sudo tdnf install amdgpu-$(echo $package_info | awk '{print $2}') 
                sudo modprobe amdgpu 

.. Important::

    To apply all settings, reboot your system.

For specific amdgpu versions and kernel compatibility, refer to the available packages at `Index of /azurelinux/3.0/prod/amd/x86_64/Packages/a/ <https://packages.microsoft.com/azurelinux/3.0/prod/amd/x86_64/Packages/a/>`_

.. _azl-package-manager-uninstall-driver:

Uninstalling
=====================================================

Uninstall kernel-mode driver
---------------------------------------------------------------------------

.. code-block:: bash

    sudo tdnf remove amdgpu amdgpu-firmware kernel-drivers-gpu

Remove amdgpu repositories
---------------------------------------------------------------------------

.. code-block:: bash

    # Remove the repositories
    sudo tdnf remove azurelinux-repos-amd
    sudo rm /etc/yum.repos.d/amdgpu.repo*

    # Clear the cache and clean the system
    sudo rm -rf /var/cache/tdnf
    sudo tdnf clean all

.. Important::

    To apply all settings, reboot your system.
