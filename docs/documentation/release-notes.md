# AMD GPU Driver (amdgpu) 30.10.2 release notes

The release notes provide release highlights and known issues since the previous AMD GPU Driver release (30.10.1).

## Release highlights

The following are notable new features and improvements in AMD GPU Driver 30.10.2.

### Operating system and hardware support changes

The AMD GPU Driver 30.10.2 introduces support for the following operating systems:

* Debian 13 (kernel: 6.12)
* Oracle Linux 10 (kernel: 6.12.0 [UEK])
* RHEL 10.0 (kernel: 6.12.0-55)

For the compatibility between AMD GPU Driver, ROCm, GPUs, and OS, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

### GPU resiliency

Multimedia Engine Reset is now supported in AMD GPU Driver (amdgpu) 30.10.2 for AMD Instinct MI300X GPUs. This finer-grain GPU resiliency feature allows recovery from faults related to VCN or JPEG without requiring a full GPU reset, thereby improving system stability and fault tolerance. Note that VCN queue reset functionality requires PLDM bundle 01.25.05.00 (or later) firmware.

### PCIe error recovery

Downstream Port Containment (DPC) and Advanced Error Reporting (AER) are PCIe mechanisms that work together to detect and recover from hardware errors. Enabling DPC for AER allows the system to isolate faulty PCIe devices and recover gracefully without crashing. This feature is supported on the AMD Instinct MI300X, MI300A, and MI325X GPUs.

## Known issues

ROCm 7.0.2 and AMD GPU Driver (amdgpu) 30.10.2 have known multimedia issue with AMD Instinct MI300A GPUs when paired with BKC 26. As a result, subsequent multimedia jobs might become unstable after the multimedia engine reset is reset to recover a VCN related fault. As a workaround, continue using BKC 25 or older firmware until it is fixed in an upcoming release.
