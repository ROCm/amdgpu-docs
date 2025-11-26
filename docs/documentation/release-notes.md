# AMD GPU Driver (amdgpu) 30.20.1 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (30.20.0).

## Release highlights

The following are notable new features and improvements in AMD GPU Driver 30.20.1.

### Operating system and hardware support changes

The AMD GPU Driver 30.20.1 introduces support for RHEL 9.7 and RHEL 10.1.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

#### GPU resiliency

AMD GPU Driver now supports Multimedia Engine Reset for AMD Instinct MI355X GPUs. This finer-grain GPU resiliency feature enables recovery from faults related to VCN or JPEG without requiring a full GPU reset, thereby improving system stability and fault tolerance. Note that VCN queue reset functionality requires PLDM bundle 01.25.16.03 (or later) firmware.

## Resolved issues

[ROCm Runtime (ROCr)](https://rocm.docs.amd.com/projects/ROCR-Runtime/en/latest/) now returns `OUT_OF_RESOURCES` when it can't create an interrupt signal, rather than incorrectly reporting success. This fix prevents misleading errors such as “malformed packet” or “illegal opcode”, avoids downstream GPU faults, and enables applications to detect and handle the condition safely.
