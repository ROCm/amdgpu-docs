# AMD GPU Driver (amdgpu) 31.30.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (31.20.0, a preview release).

## Release highlights

The following are notable new features and improvements in AMD GPU Driver 31.30.0.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

### Broader hardware enablement

- New SMU power-management generation v15.0.8 with full clock, thermal, power-limit, and metrics reporting on next-generation AMD platforms.

- New system-DMA (LSDMA v7.1) and PSP 13.0.15 support for upcoming products.

- APU + dGPU (A+A) platform enablement on GMC 12.x with correct VRAM sizing, aperture layout, and page tables for unified-memory systems.

### Compute and AI workload improvements

Hardened user-mode queues (userq) with stronger validation, safer doorbell handling, and cleaner create/teardown to reduce hang and resource-leak risk under heavy AI/ML submission.

### Power, thermal, and telemetry

- Per-component temperature reporting (AID, XCD, HBM) plus baseboard and GPU-board metrics for data-center monitoring.

- User-tunable GFX clock ranges, custom FCLK (`OD_FCLK`), and zero-fan OD on SMU v13/v14 for finer control over performance and acoustics.

- NPM (Node Power Management) on SMU v15.0.8 for platform-level power budgeting.

### Stability and security

- Broad NULL-pointer, use-after-free, and race-condition hardening in device init/teardown, VM acquisition, PASID reuse, and RAS paths.

- Bounds checking on MMHUB/GMC client-ID decoders to prevent out-of-range reads when decoding page-fault sources.

## Resolved issues

The following previously known issues have been resolved in this release:

- Resolved KFD/ROCm workload startup failures on hosts with non-4K page sizes.

- Resolved a GPU idle power consumption regression on the latest GFX v12 discrete GPUs.
