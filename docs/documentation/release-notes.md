# AMD GPU Driver (amdgpu) 31.60.0 release notes

The release notes provide  release highlights and resolved issues since the previous AMD GPU Driver release (31.50.0).

## Release highlights

AMD GPU Driver 31.60 is an incremental update on the Linux 7.x amdgpu line. It is aimed at customers using the latest AMD Instinct™ compute platforms on supported Linux distributions.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

Notable new features and improvements in AMD GPU Driver 31.60.0 include:

### Compute and Instinct improvements

- **Memory partitions (NPS) on gfx12.1**: Exposes supported NPS modes and partition switching so multi-partition Instinct configurations can be selected and validated.

- **Dispatch-log profiling**: Adds the kernel driver dispatch-log stream for gfx9.5 and gfx12, enabling queue-armed traces, firmware-notification polling, and reads in documented record formats.

- **AIS**: When the AMD GPU driver initializes AIS, it registers the GPU's VRAM with the P2PDMA kernel subsystem, generating `MEMORY_DEVICE_PCI_P2PDMA` metadata pages stored in host DRAM. A new `amdgpu` module parameter, `ais_disabled`, is added to allow non-AIS deployments to skip VRAM registration and reclaim the associated host memory.
  - `ais_disabled=0` (default): AIS is initialized by default.
  - `ais_disabled=1`: AIS initialization is skipped.
  
  Check current state at `/sys/module/amdgpu/parameters/ais_disabled`. For more information, see {ref}`disable-ais`.

### Broader hardware enablement

- **Harvested IP discovery**: Reads LSDMA/MMHUB harvest and reserved-memory tables so partially populated or partitioned parts enumerate correctly.

- **SOC 1.0 reset**: Adds a platform reset handler and revision identification from IP discovery.

### Reliability, Availability, and Serviceability (RAS)

- **ECC-aware compute reset**: Informs the kernel driver when a reset was caused by an ECC event, and extends poison-consumption handling for A+A SR-IOV guests.

- **Bad-page and EEPROM accounting**: Improves bad-page counts/thresholds and records data-source timestamps in EEPROM.

## Resolved issues

The following issues have been resolved in this release:

- Resolved hangs and races when destroying or restoring a user-mode queue, including a restore that could run before all GPU virtual addresses were mapped.

- Resolved hangs and races on queue destroy, restored all mappings before replay, validated ring pointers, and added timeline synchronization-object signaling after preemption or reset.

- Resolved the kernel driver shared-virtual-memory migration for VM ranges with holes, including a leak on the copy-to-RAM error path.

- Resolved CPER error-record retrieval and count reporting, and driver unload failure when UniRAS is enabled.
