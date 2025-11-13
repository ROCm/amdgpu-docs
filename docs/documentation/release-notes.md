# AMD GPU Driver (amdgpu) 30.10.1 release notes

AMD GPU Driver (amdgpu) 30.10.1 is a quality release that resolves the issue listed in the release highlights.

## Release highlights

The following issue has been resolved in the AMD GPU Driver (amdgpu) 30.10.1 to be used with ROCm 7.0.1.

### Failure to declare out-of-bound CPERs for bad memory page

The issue of failing to declare Out-Of-Band Common Platform Error Records (CPERs) when exceeding bad memory page threshold has been resolved. The fix applies to all AMD Instinct MI300 Series and MI350 Series GPUs.

```{note}
AMD GPU Driver (amdgpu) 30.10.1 doesn't include any other significant changes or feature additions. For comprehensive changes in the previous release, refer to the [AMD GPU Driver (amdgpu) 30.10 release notes](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-30.10/documentation/release-notes.html).
```
