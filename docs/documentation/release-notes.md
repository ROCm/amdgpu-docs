# AMD GPU Driver (amdgpu) 31.40.1 release notes

The release notes provide release highlights since the previous AMD GPU Driver release (31.40.0).

## Release highlights

This release improves system recovery robustness for AMD Instinct MI350X and MI355X under Trusted OS.

### System reliability and fault handling

Improved system recovery robustness during Mode 1 fault-handling sequences by addressing a firmware issue that could prevent successful recovery completion under certain error conditions. Fixes under Trusted OS for AMD Instinct MI350X and MI355X.

## Operating system and hardware support changes

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

## Known issues

During a reset, the driver dumps the device’s core dump data. To determine the total size required for the data dump, the driver depends on a [drm framework change](https://patchwork.freedesktop.org/patch/606834/). Older kernels without this change might result in a crash during reset.
