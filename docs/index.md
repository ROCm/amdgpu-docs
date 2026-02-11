---
myst:
  html_meta:
    "description": "Learn about the features, capabilities, and ways to optimize the AMD GPU drivers"
    "keywords": "Instinct, GPU, how to, conceptual, PCIe, IOMMU, install"
---

# AMD GPU Driver (amdgpu)

The AMD GPU driver (amdgpu) is open source software. It’s a key element in the software ecosystems (ROCm user space, AMD GPU virtualization, and frameworks) that enables powerful AMD GPUs in data centers to function optimally for AI and HPC applications workloads.

```{note}
This is the AMD GPU Driver (amdgpu) 31.10.0 technology preview release, intended for use only with the [ROCm 7.11.0 technology preview release](https://rocm.docs.amd.com/en/7.11.0-preview/index.html). For the latest production stream release, refer to [AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/).
```

This documentation describes AMD GPU driver features and capabilities, installation instructions, and compatibility information.

The AMD GPU Driver documentation is organized into the following categories:

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
