.. meta::
  :description: Rocky Linux native installation
  :keywords: AMDGPU driver install, AMDGPU driver, driver installation instructions, Rocky Linux, Rocky Linux native installation, AMD

**********************************************************************************************
Rocky Linux native installation
**********************************************************************************************

.. caution::

    Ensure that the :doc:`../prerequisites` are met before installing.

.. _rl-register-repo:

Registering ROCm repositories
=====================================================

Register kernel-mode driver
----------------------------------------------------------------------------------------------------------

.. datatemplate:nodata::

    .. tab-set::
        {% for os_version in config.html_context['rl_version_numbers'] %}
        {% set os_major, _  = os_version.split('.') %}
        .. tab-item:: Rocky {{ os_version }}
            :sync: rl-{{ os_version }} rl-{{ os_major }}

            .. code-block:: bash
                :substitutions:

                sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
                [amdgpu]
                name=amdgpu
                baseurl=https://repo.radeon.com/amdgpu/|amdgpu_url_version|/el/{{ os_version }}/main/x86_64/
                enabled=1
                priority=50
                gpgcheck=1
                gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
                EOF
                sudo dnf clean all
        {% endfor %}

.. _rl-install:

Installing
=====================================================

Install kernel driver
----------------------------------------------------------------------------------------------------------

.. code-block:: bash

    sudo dnf install amdgpu-dkms

.. Important::

    To apply all settings, reboot your system.


.. _rl-package-manager-uninstall-driver:

Uninstalling
=====================================================

Uninstall kernel-mode driver
---------------------------------------------------------------------------

.. code-block:: bash

    sudo dnf remove amdgpu-dkms

Remove AMDGPU repositories
---------------------------------------------------------------------------

.. code-block:: bash

    # Remove the repositories
    sudo rm /etc/yum.repos.d/amdgpu.repo*
    
    # Clear the cache and clean the system
    sudo rm -rf /var/cache/dnf
    sudo dnf clean all

.. Important::

    To apply all settings, reboot your system.
