.. meta::
   :description: Learn how to partition AMD GPUs/APUs.
   :keywords: AMD, GPU, APU, partitioning, ROCm, MI300X, MI300A

**************************
AMD GPU/APU Partitioning
**************************

Partitioning Overview
^^^^^^^^^^^^^^^^^^^^^^

Modern large-scale AI and HPC workloads demand fine-grained control over GPU resource allocation, memory isolation, and multi-tenant scheduling. AMD's Instinct™ MI300 series accelerators — including the MI300X GPU and MI300A APU — support flexible partitioning schemes that allow users to logically subdivide a single device into multiple independent partitions optimized for different workloads.

This documentation portal serves as a centralized index for navigating the complete GPU partitioning workflow on AMD platforms. It links to detailed technical guides for each supported accelerator, including:

- **Architecture deep dives** to understand partitioning capabilities.
- **Quick start instructions** to apply compute and memory partition modes using `amd-smi`.
- **Guide to run vLLM workload** for inference benchmarking.
- **Troubleshooting resources** for resolving partitioning issues in production environments.

Compatibility Matrix
^^^^^^^^^^^^^^^^^^^^^^

To streamline deployment planning and reduce configuration friction, we include below a **GPU Partitioning Schemes Compatibility Matrix**. This matrix outlines which combinations of **Compute Partitioning Modes** (e.g., SPX, CPX) and **Memory Partitioning Modes** (e.g., NPS1, NPS4) are validated for each supported device. It also notes any **minimum ROCm driver version requirements** necessary to enable specific configurations.

.. important::
   **New to partitioning modes?** Before using the compatibility matrix, it's essential to understand the core concepts of **Compute Partitioning Modes** (SPX, CPX, TPX) and **Memory Partitioning Modes** (NPS1, NPS4). These modes determine how compute and memory resources are logically divided across a single device.

   See our detailed overview here: 
    - :ref:`MI300X Compute Partitioning <mi300x_compute-partitioning>` / :ref:`MI300A Compute Partitioning <mi300a_compute-partitioning>`
    - :ref:`MI300X Memory Partitioning <mi300x_memory-partitioning>` / :ref:`MI300A Memory Partitioning <mi300a_memory-partitioning>`

By consolidating this matrix on the index page, users can quickly evaluate platform capabilities and navigate to device-specific documentation with full awareness of what is supported on their hardware and software stack.

.. list-table:: GPU Partitioning Schemes Compatibility Matrix
  :header-rows: 1
  :widths: 20 20 20 20 20

  * - Instinct GPUs
    - SPX + NPS1
    - TPX + NPS1
    - CPX + NPS1
    - CPX + NPS4
  * - MI300X
    - ✅
    - NA
    - 
    - ✅ (ROCm 6.4)
  * - MI300A
    - ✅
    - ✅ (ROCm 6.3)
    - ✅ (ROCm 6.4)
    - NA

.. note::
    The compatibility matrix is a living document and will be updated as new ROCm releases and device capabilities are validated. Users are encouraged to check back frequently for the latest information.

Device Documentation
^^^^^^^^^^^^^^^^^^^^^

- :doc:`AMD Instinct MI300X GPU <mi300x/index>` — Includes guidance for MI300X GPU-specific partitioning, architecture, System compatibility, and running vLLM inference.
- :doc:`AMD Instinct MI300A APU <mi300a/index>` — Includes guidance for APU-specific partitioning, architecture, System compatibility, and running vLLM inference.

We recommend users start with this index page to assess compatibility, then follow device-specific documentation to implement and validate GPU partitioning configurations in their own clusters or platforms.
