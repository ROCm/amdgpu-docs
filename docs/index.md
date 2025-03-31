---
myst:
  html_meta:
    "description": "Learn about the features, capabilities, and ways to optimize the AMD GPU drivers"
    "keywords": "Instinct, GPU, how to, conceptual, PCIe, IOMMU, install"
---

# AMD Instinct Data Center GPU Driver

This site documents the features and capabilities of the AMD GPU driver, amdgpu, along with GPU BIOS compatibility information.

The AMD Instinct documentation is organized into the following categories:

::::{grid} 1 2 2 2
:gutter: 3
:class-container: rocm-doc-grid

:::{grid-item-card} Install AMDGPU driver
:class-body: rocm-card-banner rocm-hue-16

* [Prerequisites](./install/detailed-install/prerequisites.rst)
* [Installation methods](./install/install-overview.rst)
* [Post-install instructions](./install/detailed-install/post-install.rst)
:::

:::{grid-item-card} How to
:class-body: rocm-card-banner rocm-hue-12

* [System optimization](./system-optimization/index.rst)
:::

:::{grid-item-card} Conceptual
:class-body: rocm-card-banner rocm-hue-8

* [Input-Output Memory Management Unit (IOMMU)](./conceptual/iommu.rst)
* [PCIe atomics in ROCm](./conceptual/pcie-atomics.rst)
* [Oversubscription of hardware resources](./conceptual/oversubscription.rst)
:::

::::
