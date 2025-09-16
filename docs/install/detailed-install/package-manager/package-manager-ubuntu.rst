.. meta::
  :description: Ubuntu native installation
  :keywords: AMDGPU driver install, AMDGPU driver, driver installation instructions, Ubuntu, Ubuntu native installation, AMD

****************************************************************************
Ubuntu native installation
****************************************************************************

.. caution::

    Ensure that the :doc:`../prerequisites` are met before installing.

.. _ubuntu-register-repo:

Registering ROCm repositories
=================================================

.. _ubuntu-package-key:

Package signing key
---------------------------------------------------------------------------

Download and convert the package signing key.

.. code-block:: bash

    # Make the directory if it doesn't exist yet.
    # This location is recommended by the distribution maintainers.
    sudo mkdir --parents --mode=0755 /etc/apt/keyrings

    # Download the key, convert the signing-key to a full
    # keyring required by apt and store in the keyring directory
    wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | \
        gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null

.. _ubuntu-register-driver:

.. note::

    The GPG key may change; ensure it is updated when installing a new release.
    If the key signature verification fails while updating,
    re-add the key from the ROCm to the apt repository as mentioned above.

Register kernel-mode driver
---------------------------------------------------------------------------

Add the amdgpu repository for the driver.

.. datatemplate:nodata::

    .. tab-set::
        {% for (os_version, os_release) in config.html_context['ubuntu_version_numbers'] %}
        .. tab-item:: Ubuntu {{ os_version }}
            :sync: ubuntu-{{ os_version}}

            .. code-block:: bash
                :substitutions:

                sudo tee /etc/apt/sources.list.d/amdgpu.list << EOF
                deb [arch=amd64,i386 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/|amdgpu_url_version|/ubuntu {{ os_release }} main
                EOF
                sudo apt update
        {% endfor %}

.. _ubuntu-install:

Installing
================================================

Install kernel driver
---------------------------------------------------------------------------

.. code-block:: bash

    sudo apt install amdgpu-dkms

.. Important::

    To apply all settings, reboot your system.


.. _ubuntu-package-manager-uninstall-driver:

Uninstalling
================================================

Uninstall kernel-mode driver
---------------------------------------------------------------------------

.. code-block:: bash

    sudo apt autoremove amdgpu-dkms

Remove amdgpu repositories
---------------------------------------------------------------------------

.. code-block:: bash

    # Remove the repositories
    sudo rm /etc/apt/sources.list.d/amdgpu.list

    # Clear the cache and clean the system
    sudo rm -rf /var/cache/apt/*
    sudo apt clean all
    sudo apt update

.. Important::

    To apply all settings, reboot your system.
