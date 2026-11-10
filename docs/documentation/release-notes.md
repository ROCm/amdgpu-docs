# AMD GPU Driver (amdgpu) 31.70.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (31.60.0).

## Release highlights

AMD GPU Driver 31.70.0 is an incremental update on the Linux 7.x amdgpu line first introduced in 31.50.0 and continued in 31.60.0. It is aimed at customers using the latest AMD Instinct™ compute platforms on supported Linux distributions.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

The following are notable new features and improvements in AMD GPU Driver 31.70.0.

### Compute and Instinct improvements

Adds host-trap-based PC sampling support through the Micro Engine Scheduler (MES), with quirk checks, to help performance engineers understand where GPU time is spent.

### Power, thermal, and telemetry

Adds an RMA-status query path so platform software can surface warranty and RMA-related health state on firmware-supported configurations.

## Resolved issues

The following issues have been resolved in this release:

- Resolved multiple resource leaks (fences, ACPI device references, debugfs/runtime-PM paths, IP-instance objects) that could slowly consume kernel memory during long-running cluster jobs or repeated driver bring-up.
- Resolved user-mode queue issues, including reading the write pointer at a non-zero buffer offset, waiting on fences outside the signaling section, and hang-detect timeout conversion mistakes that could mis-detect hung queues.
- Resolved KFD correctness bugs: VRAM accounting, device-mapping use-after-free, TCP XNACK scoreboard races, integer underflows in EOP ring-size calculations, and NULL restore callbacks during CRIU-style queue restore.
- Resolved SDMA engine reset so kernel queues are always included, and applied a workaround for SDMA DCC corruption on affected configurations.
- Resolved RAS/CPER retrieval and logging edge cases, including incomplete CPER query progress reporting and scrubber bank logging, so error harvest and UniRAS unload/query paths behave more predictably for service workflows and report how far an error harvest progressed, not only that it failed.
- Resolved incomplete per-pipe and user-queue reset recovery that could leave a stuck AI/HPC job requiring a full GPU reset, with kernel rings preserved where possible, hung queues are detected more accurately, and related Micro Engine Scheduler (MES) paths are hardened.
- Resolved AMD Infinity Storage (AIS) transfers that could hang when targeting storage without peer-to-peer DMA support, and improved AIS block-stack discovery so unsupported storage-direct GPU I/O fails cleanly instead of hanging.
- Resolved incorrect power-context allocation on SMU 14 paths, and separated AC/DC PPT limit restore from other power notifications that could cause flaky power-policy behavior after power-source or reset events.
- Resolved inconsistent energy-accumulator reporting on supported SMU generations so monitoring tools see more reliable energy data over time.
- Resolved incomplete IP-discovery table validation that could cause incorrect or fragile bring-up on newer platforms.
- Resolved gaps in PMFW-managed EEPROM and ACA debug-mode handling on supported MP1 generations that could weaken long-term bad-page and health-data tracking on Instinct nodes.
