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

.. code-block:: bash

    sudo tdnf install azurelinux-repos-amd
    sudo tdnf repolist --refresh
    sudo tdnf install amdgpu
    sudo reboot

.. _azl-package-manager-uninstall-driver:

Uninstalling
=====================================================

Uninstall kernel-mode driver
---------------------------------------------------------------------------

.. code-block:: bash

    sudo tdnf remove amdgpu amdgpu-firmware kernel-drivers-gpu

Remove AMDGPU repositories
---------------------------------------------------------------------------

.. code-block:: bash

    # Remove the repositories
    sudo tdnf remove azurelinux-repos-amd
    sudo rm /etc/yum.repos.d/amdgpu.repo*

    # Clear the cache and clean the system
    sudo rm -rf /var/cache/tdnf
    sudo tdnf clean all

    # Restart the system
    sudo reboot
