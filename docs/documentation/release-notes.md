# AMD GPU Driver (amdgpu) 31.20.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (31.10.0).

## Release highlights

The following are notable new features and improvements in AMD GPU Driver 31.20.0.

### Operating system and hardware support changes

This release introduces support for a new hardware IP block: SMU 15, a system management unit that provides updated power and thermal management.

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