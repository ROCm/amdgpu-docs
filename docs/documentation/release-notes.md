# AMD GPU Driver (amdgpu) 31.10.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (30.30.0).

## Release highlights

This is the first AMD GPU driver released alongside [TheRock](https://github.com/ROCm/TheRock), the new open build and release system. It also includes general stability and robustness improvements to the VCN (Video Core Next) software through ongoing mainline integration.

The following are notable new features and improvements in AMD GPU Driver 31.10.0.

### Operating system and hardware support changes

This release introduces support for Ubuntu 24.04.4 HWE (Hardware Enablement Stack).

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

## Resolved issues

Addressed a potential VCN5 vulnerability by using DMA copy instead of software copy.
