---
myst:
  html_meta:
    "description": "Learn about the features, capabilities, and ways to optimize the AMD GPU drivers"
    "keywords": "Instinct, GPU, how to, conceptual, PCIe, IOMMU, install"
---

# AMD GPU Driver (amdgpu)

The AMD GPU driver (amdgpu) is an open-source software. It is a key element in
the software ecosystems (ROCm user space, AMD GPU virtualization and
frameworks) that allows powerful AMD GPUs in data centers to function optimally
for AI & HPC applications workloads.

This site documents the features and capabilities of the AMD GPU driver, installation, and compatibility information.

The AMD Instinct documentation is organized into the following categories:

::::{grid} 1 2 2 2
:gutter: 3
:class-container: rocm-doc-grid

:::{grid-item-card} Install AMD GPU driver
:class-body: rocm-card-banner rocm-hue-16

* [Prerequisites](./install/detailed-install/prerequisites.rst)
* [Installation via native package manager](./install/package-manager-index.rst)
* [Post-install instructions](./install/detailed-install/post-install.rst)
:::

:::{grid-item-card} How to
:class-body: rocm-card-banner rocm-hue-12

* [System optimization](./system-optimization/index.rst)
* [GPU Partitioning](./gpu-partitioning/index.rst)

:::

:::{grid-item-card} Conceptual
:class-body: rocm-card-banner rocm-hue-8

* [Input-Output Memory Management Unit (IOMMU)](./conceptual/iommu.rst)
* [PCIe atomics in ROCm](./conceptual/pcie-atomics.rst)
* [Oversubscription of hardware resources](./conceptual/oversubscription.rst)
:::

::::
