# AMD GPU Driver (amdgpu) 30.30.0 release notes

The release notes provide release highlights and resolved issues since the previous AMD GPU Driver release (30.20.1).

## Release highlights

The following are notable new features and improvements in AMD GPU Driver 30.30.0.

### Operating system and hardware support changes

This release doesn't introduce operating system or hardware support changes.

For compatibility between AMD GPU Driver, ROCm, GPUs, and operating systems, see the [Compatibility matrix](../compatibility/compatibility-matrix.rst).

## Resolved issues

The following previously known issues have been resolved in this release:

- Resolved an issue where several GDB unit tests were timing out because the test application sent a `kill` command to the kernel while it was still shutting down VM entities, and the VM release work queue was active.

- Resolved an issue where `MEM_USAGE` showed values in exabytes during KFD tests.

- Resolved errors that occurred during the execution of the `mem_leak_hip_samples` test.
