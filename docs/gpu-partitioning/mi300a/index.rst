.. meta::
   :description: AMD Instinct MI300A APU
   :keywords: AMD, MI300A, APU, CPU-GPU, Instinct, Overview

*******************************************
AMD Instinct MI300A APU
*******************************************

The AMD Instinct™ MI300A APU (Accelerated Processing Unit) is a groundbreaking compute platform that fuses AMD EPYC™ CPU cores with CDNA™ 3 GPU architecture into a single, unified package. Purpose-built for data-intensive AI, HPC, and scientific computing workloads, the MI300A offers unprecedented levels of memory bandwidth, compute density, and energy efficiency — all through a cohesive CPU-GPU heterogeneous system.

As the world’s first data center APU based on **advanced chiplet packaging**, MI300A breaks traditional boundaries by enabling shared memory between the CPU and GPU, reducing latency and eliminating redundant data transfers. This guide provides an in-depth reference for developers, system architects, and platform integrators working with MI300A systems — from configuration and partitioning to memory access models and workload deployment.

Key technical highlights of the MI300A platform include:

- **24 Zen 4 CPU cores** integrated with **228 CDNA 3 CUs**, all sharing a unified addressable HBM memory pool.
- Up to **128 GB of unified HBM3 memory**, accessible by both CPU and GPU without the need for explicit memory copies.
- **Advanced GPU partitioning** support (SPX, CPX, TPX) enabling workload isolation, fine-grained scheduling, and resource optimization.
- Hardware-accelerated **coherent shared memory**, enabling low-latency CPU-GPU communication for tightly coupled compute models.
- Full compatibility with the **ROCm 6.x software stack**, including HIP, OpenMP offload, and leading AI/ML libraries.

This guide is structured to help users get the most out of MI300A across a wide range of applications:

- :doc:`Overview <overview>` — Deep dive into MI300A architecture, APU topology, and compute/memory partitioning models.
- :doc:`Requirements <requirements>` — Platform setup, BIOS/kernel configuration, ROCm compatibility matrix, and supported distros.
- :doc:`Quick Start Guide <quick-start-guide>` — Walkthrough for bringing up MI300A systems and configuring partitions using `amd-smi`.
- :doc:`Troubleshooting <troubleshooting>` — Diagnosing common errors, partition conflicts, and optimizing workload placement.

Whether you are deploying the MI300A in an exascale supercomputer or using it to accelerate simulation, AI, or analytics workloads, this documentation serves as your go-to reference for maximizing performance, interoperability, and development agility.
