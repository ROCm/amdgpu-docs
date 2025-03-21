.. meta::
  :description: Oracle Linux AMDGPU installer installation
  :keywords: installation instructions, AMDGPU, AMDGPU installer, AMD, Oracle Linux, Oracle Linux AMDGPU installer installation

*************************************************************************************
Oracle Linux AMDGPU installer installation
*************************************************************************************

``amdgpu-install`` is a tool that helps you install and update AMDGPU, ROCm, and ROCm components.

.. _ol-amdgpu-install-installation:

Installation
=================================================

.. caution::

    Ensure that the :doc:`../prerequisites` are met before installing.

.. datatemplate:nodata::

  .. tab-set::
      {% for os_version in config.html_context['ol_version_numbers'] %}
      {% set os_major, _  = os_version.split('.') %}
      .. tab-item:: OL {{ os_major }}

          .. code-block:: bash
              :substitutions:

              sudo dnf install https://repo.radeon.com/amdgpu-install/|amdgpu_version|/el/{{ os_version }}/amdgpu-install-|amdgpu_install_version|.el{{ os_major }}.noarch.rpm
      {% endfor %}

.. include:: ./amdgpu-installer-common.rst


.. _ol-amdgpu-install-uninstall-driver:

Uninstalling kernel mode driver
=================================================

.. code-block:: bash

    sudo dnf remove amdgpu-dkms

Uninstalling amdgpu-install
=================================================

After uninstalling the driver, remove the amdgpu-install package from system.

.. code-block:: bash

    sudo dnf remove amdgpu-install

Remove AMDGPU repositories
=================================================

.. code-block:: bash
    
    # Clear the cache and clean the system
    sudo rm -rf /var/cache/dnf
    sudo dnf clean all

    # Restart the system
    sudo reboot

Additional options
=================================================

* Unattended installation.

  Adding ``-y`` as a parameter to ``amdgpu-install`` skips user prompts (for automation). For example:

  .. code-block:: bash

      amdgpu-install -y --usecase=dkms
