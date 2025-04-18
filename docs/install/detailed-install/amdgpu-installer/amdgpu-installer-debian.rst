.. meta::
  :description: Debian AMDGPU installer installation
  :keywords: installation instructions, AMDGPU, AMDGPU installer, AMD, Debian, Debian AMDGPU installer installation

*************************************************************************************
Debian AMDGPU installer installation
*************************************************************************************

``amdgpu-install`` is a tool that helps you install and update AMDGPU, ROCm, and ROCm components.

.. _debian-amdgpu-install-installation:

Installation
=================================================

.. caution::

    Ensure that the :doc:`../prerequisites` are met before installing.

.. datatemplate:nodata::

  .. tab-set::
      {% for (os_version, os_release) in config.html_context['debian_version_numbers'] %}
      .. tab-item:: Debian {{ os_version }}

          .. code-block:: bash
              :substitutions:

              sudo apt update
              wget https://repo.radeon.com/amdgpu-install/|amdgpu_version|/ubuntu/{{ os_release }}/amdgpu-install_|amdgpu_install_version|_all.deb
              sudo apt install ./amdgpu-install_|amdgpu_install_version|_all.deb
              sudo apt update
      {% endfor %}

.. include:: ./amdgpu-installer-common.rst


.. _debian-amdgpu-install-uninstall-driver:

Uninstalling kernel mode driver
=================================================

.. code-block:: bash

    sudo apt autoremove amdgpu-dkms

Uninstalling amdgpu-install
=================================================

After uninstalling the driver, remove the amdgpu-install package from system.

.. code-block:: bash

    sudo apt purge amdgpu-install
    sudo apt autoremove

Remove AMDGPU repositories
=================================================

.. code-block:: bash
    
    # Clear the cache and clean the system
    sudo rm -rf /var/cache/apt/*
    sudo apt clean all
    sudo apt update
    
    # Restart the system
    sudo reboot

Additional options
=================================================

* Unattended installation.

  Adding ``-y`` as a parameter to ``amdgpu-install`` skips user prompts (for automation). For example:

  .. code-block:: bash

      amdgpu-install -y --usecase=dkms
