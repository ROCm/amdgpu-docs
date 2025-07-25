# Compatiblity Matrix for Instinct GPU + Board BIOS, Instinct Driver and ROCm

## Defintions


 * Instinct GPU + Board BIOS is a collection of software running on the GPU and PCB board hosting the GPUs socket.  The PCB board is either the PCIe card, or a UBB standard board, or the system motherboard for APUs. From the system administration purposes, this software collection is flashed onto ROM via OS utilities or the BMC. AMD previously referred to this software collection as the BKC.
 * Instinct Driver is the driver loaded by the operating system to expose the GPU capabilities to the userspace. The driver includes a set of runtime loaded firmware that runs on the GPU. AMD previously referred to this software collection as the ROCm driver.
 * ROCm is the userspace software collection including runtimes, libraries and prebuilt binaries to run user applications on the GPU.

## Compatiblity matrixes

:::::{tab-set}

::::{tab-item} MI300X

:::{dropdown} Valid Instinct GPU + Board BIOS and Instinct Driver Combinations

|PLDM Version|Instinct Driver Version|
|-------|-------|
|25.02|6.4.0, 6.4.1|
|25.04|30.10.0|
|25.05|30.10.1|

:::

:::{dropdown}  Valid Instinct Driver Combinations and ROCm

|Instinct Driver Version|ROCm Version|
|-------|-------|
|6.4.0, 6.4.1|6.4.0|
|30.10.0|7.0.0|
|30.10.1|7.0.1|
:::

:::{dropdown} Complete compatiblity matrix

|PLDM Version|Instinct Driver Version|ROCm Version|
|25.02|6.4.0, 6.4.1|6.4.0|
|-------|-----|-----------|
|25.04|30.10.0|7.0.0|
|25.05|30.10.1|7.0.1|
:::

::::

::::{tab-item} MI325X
Content 2
::::

::::{tab-item} MI355X
Content 2
::::

:::::
