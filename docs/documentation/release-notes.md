# AMD GPU Driver (amdgpu) 31.20.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (31.10.0).

## Release highlights

This release includes over 2,200 driver-level improvements across display, compute, power management, video processing, and memory management. The kernel base advances from Linux 6.18 to Linux 6.19, and the DKMS package version moves from 6.18.4 to 6.19.0.

The following are notable new features and improvements in AMD GPU Driver 31.10.0.

### Operating system and hardware support changes

This release introduces support for the following new hardware IP blocks:

- **DCN 4.2** display engine, enabling advanced display features for upcoming GPU platforms.

- **GFX 12.1** compute engine, with queue management, interrupt handling, shared virtual memory, and expert scheduling for next-generation GPUs.

- **SMU 15** system management unit, providing updated power and thermal management.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

### Compute and AI workload improvements

Hardened user-mode queue input validation and error handling.

### Memory and system improvements

General improvements to VRAM allocation, page table management, and DMA buffer handling.

### Power management improvements

Introduced asynchronous SMU messaging across all SMU generations (v11 through v15) for improved power management responsiveness.

## Resolved issues

The following previously known issues have been resolved in this release:

### Power management

- Resolved a null pointer crash in the power management subsystem during certain SMU operations.

- Resolved a race condition in power state checking that could report incorrect GPU power states.

- Resolved incorrect clock frequency settings on SMU v13 and SMU v14 platforms when using software clock limits.

### Reliability

Resolved a memory leak in the RAS (Reliability, Availability, Serviceability) initialization path.

## Known issues

The following are known issues in this release:

- VESA Auxiliary Backlight control via DMUB has been temporarily reverted due to compatibility issues on certain eDP panels. Standard backlight control continues to work normally.

- Some RHEL 7.9 and Oracle Linux 8.x configurations may require additional DKMS build adjustments. See the [Compatibility matrix](../compatibility/compatibility-matrix.rst) for supported OS versions.