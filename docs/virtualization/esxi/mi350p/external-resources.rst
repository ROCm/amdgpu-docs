.. meta::
   :description: External documentation and support resources for MI350P GPU passthrough on VMware ESXi.
   :keywords: AMD, MI350P, ESXi, external resources, Broadcom, VMware, ROCm installation, documentation

External resources
==================

This page lists external sites and documentation cited in the MI350P ESXi passthrough guide.

Related documentation
---------------------

**Broadcom Support Portal:** https://support.broadcom.com/

Use your entitled account to obtain VMware ESXi installation ISOs and related Broadcom or VMware support content referenced in :doc:`ESXi host setup <host-setup>`.

**ROCm installation for Linux:** :doc:`ROCm installation for Linux <rocm-install-on-linux:install/quick-start>`

Primary guide for installing ROCm on Linux, including quick start, detailed install, and alternative methods such as Docker and Spack. Follow this guide in the guest after the MI350P is exposed through passthrough, as described in :doc:`Install ROCm and the AMD GPU driver <install-rocm>`.

**Ubuntu native installation (AMD GPU driver):** :doc:`Ubuntu native installation <../../../install/detailed-install/package-manager/package-manager-ubuntu>`

Install the AMDGPU kernel-mode driver in the Ubuntu 24.04 guest using the package manager instructions in this documentation set.

Document revision history
-------------------------

The following table summarizes revisions to the source user guide from which this documentation was derived.

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Date
     - Guide version
     - Summary
   * - April 2025
     - 0.1
     - Initial version (source: MI300 Passthrough on ESXi User Manual).
   * - December 2025
     - 0.2
     - Atomic ops parameter and guest configuration update (source manual v0.2).
   * - July 2026
     - 0.3
     - First MI350P passthrough drop: updated host and guest procedures and screenshots for VMware ESXi 9.1, including the two-parameter (``use64bitMMIO`` and ``64bitMMIOSizeGB``) MMIO passthrough configuration with BAR-based sizing.
