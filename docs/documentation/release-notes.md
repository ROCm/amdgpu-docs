# AMD GPU Driver (amdgpu) 30.30.1 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (30.30.0).

## Release highlights

The following are notable new features and improvements in AMD GPU Driver 30.30.1.

### Operating system and hardware support changes

The AMD GPU Driver 30.30.1 introduces support for Ubuntu 24.04.4 HWE (Hardware Enablement).

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

## Resolved issues

Resolved an issue on Navi3x platforms where the Kernel Fusion Driver (KFD) could stop functioning if a GPU device was removed at runtime. The driver now supports hot‑unplug scenarios and reports device unavailability when all GPUs are removed. This fix has been validated on MI200-Series GPUs and MI300-Series GPUs.
