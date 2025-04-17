.. meta::
  :description: Installation prerequisites
  :keywords: installation prerequisites, AMD, AMDGPU, driver

*********************************************************************
Installation prerequisites
*********************************************************************

Before installing the driver, complete the following prerequisites.

1. Confirm the system has a supported Linux version.

   * To obtain the Linux distribution information, use the following command:

     .. code-block:: shell

          uname -m && cat /etc/*release

   * Confirm that your Linux distribution matches a :ref:`supported distribution <supported_distributions>`.

     **Example:** Running the preceding command on an Ubuntu system produces the following output:

     .. code-block:: shell

            x86_64
            DISTRIB_ID=Ubuntu
            DISTRIB_RELEASE=20.04
            DISTRIB_CODENAME=focal
            DISTRIB_DESCRIPTION="Ubuntu 20.04.5 LTS"

.. _verify_kernel_version:

2. Verify the kernel version.

   * To check the kernel version of your Linux system, type the following command:

     .. code-block:: shell

            uname -srmv

     **Example:** The preceding command lists the kernel version in the following format:

     .. code-block:: shell

            Linux 5.15.0-46-generic #44~20.04.5-Ubuntu SMP Fri Jun 24 13:27:29 UTC 2022 x86_64

   * Confirm that your kernel version matches the system requirements, as listed in :ref:`supported_distributions`.

.. _register-enterprise-linux:

Register your Enterprise Linux
==========================================================

If you're using Red Hat Enterprise Linux (RHEL) or SUSE Linux Enterprise Server (SLES), register
your operating system to ensure you're able to download and install packages.

.. tab-set::

  .. tab-item:: Ubuntu
        :sync: ubuntu-tab

        There is no registration required for Ubuntu.

  .. tab-item:: Debian
        :sync: debian-tab

        There is no registration required for Debian.

  .. tab-item:: Red Hat Enterprise Linux
        :sync: rhel-tab

        Typically you can register by following the step-by-step user interface.
        If you need to register by command line, use the following commands:
        
        .. code-block:: shell

            subscription-manager register --username <username> --password <password>
            subscription-manager attach --auto

        More details about `registering for RHEL <https://access.redhat.com/solutions/253273>`_

  .. tab-item:: Oracle Linux
        :sync: ol-tab

        There is no registration required for Oracle Linux.

  .. tab-item:: SUSE Linux Enterprise Server
        :sync: sle-tab

        Typically you can register by following the step-by-step user interface.
        If you need to register by command line, use the following commands:
            
        .. code-block:: shell

            sudo SUSEConnect -r <REGCODE>

        More details about `registering for SLES <https://www.suse.com/support/kb/doc/?id=000018564>`_

  .. tab-item:: Azure Linux
        :sync: azl-tab

        There is no registration required for Azure Linux.

.. _update-enterprise-linux:

Update your Enterprise Linux
==========================================================

If you are using Red Hat Enterprise Linux (RHEL) or SUSE Linux Enterprise Servers (SLES), or Oracle Linux, 
it is recommended that you update your operating system to the latest packages from the Linux distribution.
This is a requirement for newer hardware on older versions of RHEL, SLES or OL.

.. datatemplate:nodata::

    .. tab-set::

        .. tab-item:: Ubuntu
            :sync: ubuntu-tab

            There is no update required for Ubuntu.
        
        .. tab-item:: Debian
            :sync: debian-tab

            There is no update required for Debian.

        .. tab-item:: Red Hat Enterprise Linux
            :sync: rhel-tab

            .. tab-set::

                {% for os_version in config.html_context['rhel_version_numbers'] %}
                {% set os_major, _  = os_version.split('.') %}
                .. tab-item:: {{ os_version }}

                   .. code-block:: bash
                       :substitutions:

                       sudo dnf update --releasever={{ os_version }} --exclude=\*release\*
                {% endfor %}

        .. tab-item:: Oracle Linux
            :sync: ol-tab

            .. tab-set::

                {% for os_version in config.html_context['ol_version_numbers'] %}
                {% set os_major, _  = os_version.split('.') %}
                .. tab-item:: {{ os_version }}

                   .. code-block:: bash
                       :substitutions:

                       sudo dnf update --releasever={{ os_version }} --exclude=\*release\*
                {% endfor %}

        .. tab-item:: SUSE Linux Enterprise Server
            :sync: sle-tab

            .. tab-set::

                {% for os_version in config.html_context['sles_version_numbers'] %}
                .. tab-item:: {{ os_version }}

                   .. code-block:: bash

                        sudo zypper update
                {% endfor %}

        .. tab-item:: Azure Linux
            :sync: azl-tab

            There is no update required for Azure Linux.

.. important::

    To apply all settings, reboot your system.

Kernel headers
================================================================

The driver package uses
`Dynamic Kernel Module Support (DKMS) <https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support>`_
to build the `amdgpu-dkms` module (driver) for the installed kernels. This requires the Linux kernel
headers and modules to be installed for each. Usually these are automatically installed with the kernel,
but if you have multiple kernel versions or you have downloaded the kernel images and not the kernel
meta-packages then they must be manually installed.

To install for the currently active kernel run the command corresponding to your distribution.

.. tab-set::

    .. tab-item:: Ubuntu
        :sync: ubuntu-tab

        .. code-block:: shell

            sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"

    .. tab-item:: Debian
        :sync: debian-tab

        .. code-block:: shell

            sudo apt install "linux-headers-$(uname -r)"

    .. tab-item:: Red Hat Enterprise Linux
        :sync: rhel-tab

        .. datatemplate:nodata::

            .. tab-set::

              {% for os_release in config.html_context['rhel_release_version_numbers']  %}

                  .. tab-item:: RHEL {{ os_release }}

                    .. code-block:: shell

                        {% if os_release == '9' -%}
                        sudo dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)" "kernel-devel-matched-$(uname -r)"
                        {%- else -%}
                        sudo dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)"
                        {%- endif %}

              {% endfor %}

    .. tab-item:: Oracle Linux
        :sync: ol-tab

        .. code-block:: shell

            sudo dnf install "kernel-uek-devel-$(uname -r)"

    .. tab-item:: SUSE Linux Enterprise Server
        :sync: sle-tab

        .. code-block:: shell

            sudo zypper install kernel-default-devel

    .. tab-item:: Azure Linux
        :sync: azl-tab

        .. code-block:: shell

            sudo tdnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)"
