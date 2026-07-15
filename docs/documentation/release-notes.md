# AMD GPU Driver (amdgpu) 31.40.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (31.30.0, a preview release).

## Release highlights

The AMD GPU Driver 31.40.0 builds on 31.30.0 with a wide range of enhancements in compute performance, power management, and overall reliability. It is compatible with ROCm 7.14.0 and Radeon™ Software for Linux (RSL) 26.13.

This release introduces more resilient handling of AI and compute workloads, expanded monitoring capabilities, and numerous stability improvements to reduce hangs, crashes, and memory-related issues. It also includes targeted improvements for Instinct MI300-series platforms and newer compute GPUs.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

The following are notable new features and improvements in AMD GPU Driver 31.40.0.

### Compute and Instinct improvements

- **Improved compute trap-handler memory placement:** Compute trap-handler data is now stored in GPU device memory instead of system memory on supported Instinct platforms. This enhancement improves reliability for AI and HPC workloads that depend on stable compute error handling.

- **Finer-grained queue recovery:** Added compute user queue reset and pipe reset for AMD Radeon™ RX 7000 and RX 9000 Series GPUs. This enables recovery from compute-related faults without requiring a full GPU reset, improving overall stability and fault tolerance.

- **Enhanced user-mode queue handling:** Additional validation, hang detection, and reset logic for user-mode queues reduces the risk of stalled AI/ML jobs and prevents resource leaks under heavy submissions.

- **Expanded HBM queue descriptor support:** Optimized placement and management of compute queue metadata on high-memory Instinct platforms.

- **AMD Infinity Storage (AIS) enablement:** Introduces AMD Infinity Storage (AIS) enablement together with HipFile support, enabling direct data transfers between AMD GPUs and storage. AIS allows data to move directly between GPU VRAM and storage devices, including local NVMe, NVMe-oF RDMA, and NFSoRDMA, without staging data through host memory and delivers high-bandwidth, low-overhead storage I/O for GPU compute workloads.

### Power, thermal, and telemetry

- **SMU 15.0.5 support:** Introduces updated power management features for upcoming platforms.

- **Enhanced SMU v15 metrics:** Adds support for monitoring memory temperature, partition-level metrics, and thermal alerts, offering improved data-center monitoring and diagnostics capabilities.

- **Improved driver unload on APU platforms:** Refines power management processes when the driver is removed or during system shutdown on SMU v15 APUs.

### Reliability, serviceability, and RAS

- **Enhanced UniRAS and bad-page management:** Adds EEPROM-backed reliability data, poison-error handling, and improved bad-page tracking, enabling easier serviceability and diagnostics.

- **System stability improvements:** Implements extensive memory safety, locking, and validation enhancements across device setup, GPU memory management, user queues, and error-reporting paths.

## Resolved issues

The following previously known issues have been resolved in this release:

### Driver security

- Resolved multiple memory safety vulnerabilities, including null-pointer access, use-after-free, buffer overflows, and out-of-bounds access, which could lead to system instability under fault or stress conditions.

- Resolved incorrect video memory mapping behavior on systems using non-4 KB memory page sizes.

- Resolved issues with user-mode queue creation, waiting, and path reset operations that could cause system hangs or resource leaks.

- Resolved module unload issues to ensure pending cleanup processes complete reliably when the driver is removed.

### Compute and power

- Resolved issues with compute scheduling and reset paths on newer GPU generations, including MES queue removal and pipe reset handling.

- Resolved power-management reporting and overdrive table handling on select SMU v14/v15 platforms, addressing memory leaks and incorrect limit calculations.

- Resolved incorrect SDMA queue counter reporting affected platforms.

### Reliability and RAS

Resolved RAS reservation and EEPROM synchronization issues that caused incorrect reporting of available bad-page capacity.
