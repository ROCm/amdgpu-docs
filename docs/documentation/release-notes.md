# AMD GPU Driver (amdgpu) 31.50.0 release notes

The release notes provide release highlights, fixed bugs, and known issues since the previous AMD GPU Driver release (31.40.0).

AMD GPU Driver 31.50.0 moves the driver from the previous 6.19-based line onto the new Linux 7.x kernel base, folding in a full development cycle of amdgpu changes rather than a single point release. This release is aimed at customers using the latest AMD Instinct™ compute platforms on supported Linux distributions.

Compared with the previous release, this update delivers more resilient AI and compute job handling through a reworked user-mode queue path, richer power and telemetry data on the new SMU generation, and enablement for newer compute silicon (SMU v15, GFX v12.1, and PSP 15.0.5). It also adds many stability and memory-safety fixes that reduce hangs, crashes, and resource leaks.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

## Release highlights

The following are notable new features and improvements in AMD GPU Driver 31.50.0.

### Compute and Instinct improvements

* **Reworked user-mode queue handling:** Adds accurate reset accounting, guilty-queue identification, and automatic GPU recovery when a hung queue fails to unmap, reducing the risk of stuck AI/ML jobs and resource leaks under heavy submission.

* **Correct interrupt routing for compute queues:** Fixes end-of-pipe (EOP) and error-interrupt routing for both kernel and user queues on GFX11 and GFX12, improving submission robustness.

* **New GFX v12.1 compute IP:** Enables 57-bit watch-address and queue-reset support for the newer compute engine used by upcoming products.

* **KFD queue and topology hardening:** Adds GFX12 queue-reset support in topology, bounds checking on system-topology (CRAT) parsing, and additional SVM range validation for more stable compute sessions.

### Power, thermal, and telemetry

* **SMU 15.0.x support:** Brings up the new SMU 15.0.0 / 15.0.5 / 15.0.8 power-management firmware interface for upcoming platforms.

* **Richer SMU v15 metrics:** Adds GPU metrics including engine-busy reporting, NPM support, and thermal-alert reporting for improved data-center monitoring and diagnostics.

* **Mode2 reset enablement:** Enables mode2 reset paths for SMU IP v15.0.0 and v15.0.5, improving recovery behavior on new silicon.

* **Cleaner driver unload on APU platforms:** Restores MC access after PrepareMp1ForUnload on SMU v15 APUs, improving power-management behavior when the driver is removed or the system shuts down.

### Broader hardware enablement

* **PSP 15.0.5 security processor:** Enables the new platform security processor required on new compute platforms.

* **LSDMA v7.1 system DMA:** Enables the updated system DMA engine block for newer silicon.

### Reliability, serviceability, and RAS

* **Unified RAS (UniRAS) enhancements:** Adds address sanity checks and a debug mask to suppress correctable-error log noise for easier service and diagnostics.

* **System stability hardening:** Broad improvements to memory safety, bounds checking, and validation across device setup, GPU memory management, user queues, and error-reporting paths.

## Resolved issues

The following classes of issues were addressed in 31.50.0 compared with 31.40.0:

### General driver security

* Fixed multiple memory-safety issues (null-pointer access, out-of-bounds access, and missing bounds/length validation) across KFD topology, SVM, and RAS paths that could lead to instability under fault or stress conditions.

* Fixed several user-mode queue create, wait, and reset paths that could hang or leak resources.

### Compute and power

* Fixed an indefinite fence wait in user-queue submission during a GPU reset that could hang compute workloads.

* Fixed incorrect reset accounting for user queues so GPU resets triggered by user-mode queues are tracked and recovered reliably.

* Fixed compute scheduling and reset paths on newer GPU generations, including MES doorbell handling for queue suspend and end-of-pipe (EOP) interrupt routing for compute queues.

* Fixed a memory leak of DPM power policies on SMU v15 that could grow over repeated power-state changes.

* Fixed a kernel deadlock in the KFD shared-virtual-memory (SVM) path that could hang the system when multiple processes over-commit GPU VRAM while concurrently calling mmap under memory pressure.

### Reliability and RAS

* Fixed UniRAS address and debug-mode handling, including address sanity checks and correctable-error log masking.