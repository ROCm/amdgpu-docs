.. meta::
  :description: Red Hat Enterprise Linux native installation
  :keywords: AMDGPU driver install, AMDGPU driver, driver installation instructions, Red Hat Enterprise Linux, RHEL, RHEL native installation, AMD

**********************************************************************************************
Red Hat Enterprise Linux native installation
**********************************************************************************************

.. caution::

    Ensure that the :doc:`../prerequisites` are met before installing.

.. _rhel-register-repo:

Registering ROCm repositories
=====================================================

Register kernel-mode driver
----------------------------------------------------------------------------------------------------------

.. datatemplate:nodata::

    .. tab-set::
        {% for os_version in config.html_context['rhel_version_numbers'] %}
        {% set os_major, _  = os_version.split('.') %}
        .. tab-item:: RHEL {{ os_version }}
            :sync: rhel-{{ os_version }} rhel-{{ os_major }}

            .. code-block:: bash
                :substitutions:

                sudo tee /etc/yum.repos.d/amdgpu.repo <<EOF
                [amdgpu]
                name=amdgpu
                baseurl=https://repo.radeon.com/amdgpu/|rocm_version|/el/{{ os_version }}/main/x86_64/
                enabled=1
                priority=50
                gpgcheck=1
                gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
                EOF
                sudo dnf clean all
        {% endfor %}

.. _rhel-install:

Installing
=====================================================

Install kernel driver
----------------------------------------------------------------------------------------------------------

.. code-block:: bash

    sudo dnf install amdgpu-dkms
    sudo reboot

.. _rhel-package-manager-uninstall-driver:

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

    # Restart the system
    sudo reboot
