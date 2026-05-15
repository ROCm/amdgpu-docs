"""Configuration file for the Sphinx documentation builder."""
import os

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "instinct.docs.amd.com")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
project = "AMD GPU Driver (amdgpu)"

version = "31.30.0"
rocm_version = '7.13'
rocm_directory_version = '7.13.0' # in 6.0 rocm was located in /opt/rocm-6.0.0
amdgpu_version = '31.30' # directory in https://repo.radeon.com/rocm/apt/ and https://repo.radeon.com/amdgpu-install/
amdgpu_url_version = '31.30'
release = version
html_title = f"AMD GPU Driver (amdgpu) {version} preview"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2026 Advanced Micro Devices, Inc. All rights reserved."

# Supported linux version numbers
ubuntu_version_numbers = [('26.04', 'resolute'), ('24.04', 'noble'), ('22.04', 'jammy')]
debian_version_numbers = [('13', 'noble'), ('12', 'jammy')]
rhel_release_version_numbers = ['10', '9', '8']
rhel_version_numbers = ['10.1', '10.0', '9.7', '9.6', '9.4', '8.10']
sles_version_numbers = ['16.0', '15.7']
ol_release_version_numbers = ['10', '9', '8']
ol_version_numbers = ['10.1', '9.7', '8.10']
rl_version_numbers = ['9.7']

html_context = {
    "ubuntu_version_numbers" : ubuntu_version_numbers,
    "debian_version_numbers" : debian_version_numbers,
    "sles_version_numbers" : sles_version_numbers,
    "rhel_release_version_numbers" : rhel_release_version_numbers,
    "rhel_version_numbers" : rhel_version_numbers,
    "ol_release_version_numbers" : ol_release_version_numbers,
    "ol_version_numbers" : ol_version_numbers,
    "rl_version_numbers" : rl_version_numbers
}


# Required settings
html_theme = "rocm_docs_theme"
html_theme_options = {
    "announcement": f"AMD GPU Driver {version} is a technology preview intended for use only with <a id='rocm-banner' href='https://rocm.docs.amd.com/en/7.13.0-preview/index.html'>AMD ROCm 7.13.0 technology preview</a>.",
    "flavor": "generic",
    "header_title": f"AMD GPU Driver (amdgpu) {version}-preview",
    "header_link": f"https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/",
    "version_list_link": f"https://instinct.docs.amd.com/projects/amdgpu-docs/en/{version}-preview/release/versions.html",
    "nav_secondary_items": {
        "GitHub": "https://github.com/ROCm/amdgpu",
        "Community": "https://github.com/ROCm/ROCm/discussions",
        "Blogs": "https://rocm.blogs.amd.com/",
        "ROCm&#8482; Docs": "https://rocm.docs.amd.com",
        "ROCm Developer Hub": "https://www.amd.com/en/developer/resources/rocm-hub.html",
        "System and Infra Docs": "https://instinct.docs.amd.com/",
        "Infinity Hub": "https://www.amd.com/en/developer/resources/infinity-hub.html",
        "Support": "https://github.com/ROCm/amdgpu/issues/new/choose",
    },
    "link_main_doc": False,
}

extensions = [
    "rocm_docs",
    "sphinxcontrib.datatemplates",
    "sphinx_substitution_extensions",
]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']

# Add the following replacements to every RST file.
rst_prolog = f"""
.. |rocm_version| replace:: {rocm_version}
.. |amdgpu_version| replace:: {amdgpu_version}
.. |amdgpu_url_version| replace:: {amdgpu_url_version}
.. |rocm_directory_version| replace:: {rocm_directory_version}
"""
