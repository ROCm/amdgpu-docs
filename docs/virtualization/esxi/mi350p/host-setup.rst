.. meta::
   :description: Configure the VMware ESXi host for MI350P GPU passthrough, including SSH access and PCI passthrough enablement.
   :keywords: AMD, MI350P, ESXi, host setup, SSH, PCI passthrough, DirectPath I/O, VMware Host Client

ESXi host setup for MI350P passthrough
=======================================

This section describes the ESXi host configuration required before you create a virtual machine with MI350P GPU passthrough. A prerequisite for this setup is an ESXi installation on the host machine. This guide uses ESXi 9.1, but the procedure should be similar for other ESXi versions in the 9.x family.

Access the ESXi host web UI
----------------------------

You need access to the host web UI. You can obtain the link from the system initial boot page after the ESXi host starts.

.. figure:: ../../images/mi350p-esxi-host-web-ui-address.png
   :alt: ESXi Direct Console User Interface showing the host management URL on the initial boot page
   :align: center
   :width: 800px
   :name: mi350p-esxi-host-web-ui-address

   ESXi host web UI address from the initial boot page. The Direct Console User Interface (DCUI) displays the HTTPS management URL (for example, ``https://10.216.113.142/``) that you use to open the VMware Host Client in a browser.

After a successful login, the ESXi host welcome screen confirms that the installation is healthy and the host is ready for configuration.

.. figure:: ../../images/mi350p-esxi-host-welcome-screen.png
   :alt: VMware Host Client Summary page for the ESXi host after login
   :align: center
   :width: 800px
   :name: mi350p-esxi-host-welcome-screen

   ESXi host welcome screen after login. The **Summary** tab shows host details, capacity and usage, and any active alarms (such as SSH enabled or license expiration notices).

Enable SSH on the ESXi host
---------------------------

You use SSH access during VM installation, for example, to download the Ubuntu installer ISO to a datastore. Enable SSH as follows:

#. Navigate to **Configure → Services**.
#. Select **SSH** from the Services list.
#. Click **Start**.

Optionally, use **Edit Startup Policy** to set SSH to **Start and stop with host** so it remains available after a reboot.

.. figure:: ../../images/mi350p-esxi-enable-ssh.jpeg
   :alt: ESXi Configure Services page with SSH selected and running
   :align: center
   :width: 800px
   :name: mi350p-esxi-enable-ssh

   Enable SSH under **Configure → Services**. Select **SSH** from the Services list, confirm the daemon status is **Running**, and click **Start**. Use **Edit Startup Policy** to keep SSH available after a host reboot.

Enable passthrough for MI350P GPUs
-----------------------------------

Toggle passthrough mode for the MI350P GPUs before you assign them to a virtual machine:

#. Navigate to **Configure → Hardware → PCI Devices**.
#. Type **Processing accelerators** in the search bar to filter the list to MI350P GPUs. This label appears in the ESXi UI for the MI350P device class.
#. Select the device, or all devices if you are assigning more than one, by ticking the checkbox.
#. Click **Toggle passthrough**.

.. figure:: ../../images/mi350p-esxi-enable-passthrough.jpeg
   :alt: ESXi PCI Devices page showing MI350P GPUs before passthrough is enabled
   :align: center
   :width: 800px
   :name: mi350p-esxi-enable-passthrough

   Enable passthrough for MI350P GPUs under **Configure → Hardware → PCI Devices**. Filter by **Processing accelerators**, select the target device or devices, and click **Toggle passthrough**. Before toggling, the **Passthrough** column shows **Disabled**.

After the operation completes, refresh the PCI Devices page. The **Passthrough** column should show **Active** for each selected MI350P device.

.. figure:: ../../images/mi350p-esxi-passthrough-active.jpeg
   :alt: ESXi PCI Devices page showing passthrough status Active for the MI350P GPU
   :align: center
   :width: 800px
   :name: mi350p-esxi-passthrough-active

   Passthrough status **Active** after refresh. Each selected MI350P GPU should show **Passthrough: Active** before you proceed to VM creation.

.. note::
   Passthrough must be enabled at the host level before you can add a GPU to a VM as a **Fixed DirectPath IO** PCI device.

Continue to guest setup
-----------------------

After SSH is enabled and passthrough is active for all target MI350P GPUs, proceed to :doc:`Ubuntu 24.04 guest setup <ubuntu-guest-setup>` to create and configure the virtual machine.
