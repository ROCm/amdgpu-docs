.. meta::
  :description: SUSE Enterprise Linux native installation
  :keywords: ROCm install, installation instructions, SUSE, SUSE Linux Enterprise native installation,
    AMD, ROCm

*********************************************************************************************
SUSE Linux Enterprise native installation
*********************************************************************************************

.. caution::

    Ensure that the :doc:`../prerequisites` are met before installing.

.. _sles-addtional-package:

Additional package repositories
===============================================

.. datatemplate:nodata::

    .. tab-set::

        {% for os_version in config.html_context['sles_version_numbers'] %}
        {% set os_release, os_sp  = os_version.split('.') %}

        .. tab-item:: SLES {{ os_version }}

            .. code-block:: shell

                sudo SUSEConnect -p sle-module-desktop-applications/{{ os_version }}/x86_64
                sudo SUSEConnect -p sle-module-development-tools/{{ os_version }}/x86_64
                sudo SUSEConnect -p PackageHub/{{ os_version }}/x86_64
                sudo zypper install zypper

.. _sles-register-rocm:

Registering ROCm repositories
===============================================

.. _sles-register-driver:

Register kernel-mode driver
--------------------------------------------------------------------------------------


.. datatemplate:nodata::

    .. tab-set::
        {% for os_version in config.html_context['sles_version_numbers'] %}
        .. tab-item:: SLES {{ os_version }}

            .. code-block:: bash
                :substitutions:

                sudo tee /etc/zypp/repos.d/amdgpu.repo <<EOF
                [amdgpu]
                name=amdgpu
                baseurl=https://repo.radeon.com/amdgpu/|rocm_version|/sle/{{ os_version }}/main/x86_64/
                enabled=1
                gpgcheck=1
                gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
                EOF

                sudo zypper refresh

        {% endfor %}

.. _sles-install:

Installing
===============================================

Install kernel driver
--------------------------------------------------------------------------------------

.. code-block:: bash

    sudo zypper --gpg-auto-import-keys install amdgpu-dkms
    sudo reboot

.. _sles-package-manager-uninstall-driver:

Uninstalling
================================================

Uninstall kernel-mode driver
---------------------------------------------------------------------------

.. code-block:: bash

    sudo zypper remove amdgpu-dkms amdgpu-core

Remove AMDGPU repositories
---------------------------------------------------------------------------

.. code-block:: bash
    :substitutions:

    # Remove the repositories
    sudo zypper removerepo "amdgpu"
    
    # Clear cache and clean system
    sudo zypper clean --all
    sudo zypper refresh
    
    # Restart the system
    sudo reboot

