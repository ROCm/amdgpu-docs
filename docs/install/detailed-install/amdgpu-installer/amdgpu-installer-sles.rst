.. meta::
  :description: SUSE Enterprise Linux AMDGPU installer installation
  :keywords: installation instructions, AMDGPU, AMDGPU installer, AMD, SUSE Enterprise Linux, SUSE Enterprise Linux AMDGPU installer installation

*************************************************************************************
SUSE Enterprise Linux AMDGPU installer installation
*************************************************************************************

``amdgpu-install`` is a tool that helps you install and update AMDGPU, ROCm, and ROCm components.

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

        {% endfor %}

.. _sles-amdgpu-install-installation:

Installation
=================================================

.. caution::

    Ensure that the :doc:`../prerequisites` are met before installing.

.. datatemplate:nodata::

  .. tab-set::
      {% for os_version in config.html_context['sles_version_numbers'] %}
      .. tab-item:: SLES {{ os_version }}

          .. code-block:: bash
              :substitutions:

              sudo zypper --no-gpg-checks install https://repo.radeon.com/amdgpu-install/|amdgpu_version|/sle/{{ os_version }}/amdgpu-install-|amdgpu_install_version|.noarch.rpm
      {% endfor %}

.. include:: ./amdgpu-installer-common.rst


.. _sles-amdgpu-install-uninstall-driver:

Uninstalling kernel mode driver
=================================================

.. code-block:: bash

    sudo zypper remove amdgpu-dkms amdgpu-dkms-firmware

Uninstalling amdgpu-install
=================================================

After uninstalling the driver, remove the amdgpu-install package from system.

.. code-block:: bash

    sudo zypper remove amdgpu-install

Remove AMDGPU repositories
=================================================

.. code-block:: bash
    
    # Clear the cache and clean the system
    sudo zypper clean --all
    sudo zypper refresh
    
    # Restart the system
    sudo reboot

Additional options
=================================================

* Unattended installation.

  Adding ``-y`` as a parameter to ``amdgpu-install`` skips user prompts (for automation). For example:

  .. code-block:: bash

      amdgpu-install -y --usecase=dkms
