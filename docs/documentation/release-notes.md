# AMD GPU Driver (amdgpu) 31.50.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (31.40.1).

## Release highlights

AMD GPU Driver 31.50.0 moves the driver from the previous 6.19-based line onto the new Linux 7.x kernel base, folding in a full development cycle of amdgpu changes rather than a single point release. This release is aimed at customers using the latest AMD Instinct™ compute platforms on supported Linux distributions.

Compared with the previous release, AMD GPU Driver 31.50.0 delivers more resilient AI and compute job handling through a reworked user-mode queue path, richer power and telemetry data on the new SMU generation, and enablement for newer compute silicon (SMU 15, GFX 12.1, and PSP 15.0.5). It also adds stability and memory-safety fixes that reduce hangs, crashes, and resource leaks.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

### Documentation updates

Added the [AMD Instinct MI350P on VMware ESXi](../virtualization/esxi/mi350p/index.rst) guide, which documents GPU passthrough on ESXi 9.x with an Ubuntu 24.04 guest.

## Operating system and hardware support changes

The following are notable new features and improvements in AMD GPU Driver 31.50.0.

### Compute and Instinct improvements

* **New GFX 12.1 compute IP:** Enables 57-bit watch-address and queue-reset support for the newer compute engine used by upcoming products.

* **Kernel Fusion Driver (KFD) queue and topology hardening:** Adds GFX12 queue-reset support in topology, bounds checking on system-topology (CRAT) parsing, and additional shared virtual memory (SVM) range validation for more stable compute sessions.

### Power, thermal, and telemetry

* **SMU 15.0.x support:** Brings up the new SMU 15.0.0 / 15.0.8 power-management firmware interface for upcoming platforms.

* **Mode2 reset enablement:** Enables mode2 reset paths for SMU IP 15.0.0 and 15.0.5, improving recovery behavior on new silicon.

### Broader hardware enablement

* **PSP 15.0.5 security processor:** Enables the new platform security processor required on new compute platforms.

* **LSDMA 7.1 system DMA:** Enables the updated system Direct Memory Access (DMA) engine block for newer silicon.

### Reliability, Availability, and Serviceability (RAS)

* **Unified RAS (UniRAS) enhancements:** Adds address sanity checks and a debug mask to suppress correctable-error log noise for easier service and diagnostics.

## Resolved issues

The following previously known issues have been resolved in this release:

### Compute and power

* Resolved an indefinite fence wait in user-queue submission during a GPU reset that could hang compute workloads.

* Resolved a memory leak of Dynamic Power Management (DPM) power policies on SMU 15 that could grow over repeated power-state changes.

* Resolved a kernel deadlock in the KFD SVM path that could hang the system when multiple processes over-commit GPU VRAM while concurrently calling mmap under memory pressure.

* Resolved user-mode queue handling issues by adding accurate reset accounting, guilty-queue identification, and automatic GPU recovery when a hung queue fails to unmap, reducing the risk of stuck AI/ML jobs and resource leaks under heavy submission.

* Resolved end-of-pipe (EOP) and error-interrupt routing for both kernel and user queues on GFX11 and GFX12, improving submission robustness.
