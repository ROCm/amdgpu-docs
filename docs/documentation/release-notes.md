# AMD GPU Driver (amdgpu) 30.20.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (30.10.2).

## Release highlights

The following are notable new features and improvements in AMD GPU Driver 30.20.0.

### Operating system and hardware support changes

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

### Partitioning

AMD GPU Driver 30.20.0 adds NPS2 + CPX partitioning support for AMD Instinct MI355X and MI350X. NPS2 splits the GPU’s memory into two NUMA domains. CPX (Core Partitioned X-celerator) is a compute partitioning mode that divides the GPU’s compute complexes (XCDs) into eight isolated logical devices. Each partition operates independently, enabling multi-tenant usage, workload isolation, and fine-grained resource control. This feature requires PLDM bundle (firmware) 01.25.15.04.

### Power management

AMD GPU Driver 30.20.0 introduces support for Node Power Management (NPM) on AMD Instinct MI355X and MI350X GPUs. This driver-level feature enables centralized control of power distribution across multiple GPUs within a compute node, allowing the system to:

* Query and set power limits for the entire node.
* Dynamically redistribute power among GPUs based on workload demands and thermal headroom.
* Normalize GPU performance by compensating for manufacturing variability across devices.

## Resolved issues

Resolved an issue where the GPU failed to recover after RAS (Reliability, Availability, and Serviceability) poison consumption. The fix applies to all AMD Instinct MI300 and MI350 Series GPUs.
