# AMD GPU Driver (amdgpu) 30.30.2 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (30.30.1).

## Release highlights

The following are notable improvements and updates in AMD GPU Driver 30.30.2.

### Operating system and hardware support changes

This release doesn’t introduce operating system or hardware support changes.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

### RAS and memory reliability improvements

The AMD GPU Driver 30.30.2 improves the Reliability, Availability, and Serviceability (RAS) subsystem with enhanced Bad Page Retirement handling on AMD Instinct MI300 Series GPUs. The driver now correctly identifies and retires all bad pages within a physical memory row, and properly recovers from invalid EEPROM table states.

## Resolved issues

The following previously known issues have been resolved in this release:

- Resolved an issue on AMD Instinct MI300 Series GPUs where the RAS EEPROM bad page table could become invalid, preventing the Bad Page Retirement feature from functioning correctly. The driver now detects and resets invalid EEPROM tables, restoring proper bad page tracking.

- Resolved an issue where VRAM type information was not being queried from firmware, causing incorrect memory type handling that affected the algorithm used to identify all bad pages within the same physical row. The driver now retrieves VRAM information directly from firmware for accurate bad page identification on AMD Instinct MI300 Series GPUs.
