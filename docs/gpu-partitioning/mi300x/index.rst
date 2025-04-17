.. meta::
   :description: AMD Instinct MI300X GPU
   :keywords: AMD, MI300X, GPU, Overview

*******************************************
AMD Instinct MI300X GPU
*******************************************

The AMD Instinct™ MI300X GPU represents a significant leap in data center GPU design, purpose-built for large-scale AI inference, high-throughput LLM workloads, and advanced HPC deployments. Featuring cutting-edge CDNA™ 3 architecture and industry-leading memory capacity, the MI300X is designed to meet the most demanding compute and memory bandwidth requirements of today’s generative AI era.

This documentation provides a comprehensive guide for users, system integrators, and infrastructure teams working with the MI300X, covering the complete software and runtime configuration lifecycle — from initial bring-up and partitioning to troubleshooting and running real-world workload.

Key technical highlights of the MI300X include:

- Up to **192 GB of HBM3 memory** with ultra-high bandwidth to accelerate large model inference.
- Support for advanced **GPU partitioning modes**, enabling logical GPU segmentation (SPX, CPX) for multi-tenant deployments and workload isolation.
- Fine-grained **memory partitioning** (NPS1, NPS4) for optimizing memory locality and performance in dense compute clusters.
- Full-stack compatibility with **ROCm 6.x**, the open software platform for AMD GPUs, enabling tight integration with PyTorch, Hugging Face, and other AI/ML frameworks.

The sections below provide targeted guidance for each step of working with the MI300X platform:

- :doc:`Overview <overview>` — Architectural deep dive and partitioning model explanation.
- :doc:`Requirements <requirements>` — Platform prerequisites, supported ROCm versions, and kernel/BIOS configurations.
- :doc:`Quick Start Guide <quick-start-guide>` — Step-by-step instructions to configure GPU and memory partitions using `amd-smi`.
- :doc:`Troubleshooting <troubleshooting>` — Common error resolutions and best practices for debugging partitioning-related issues.
- :doc:`Run a VLLM workload <run-vllm>` — Instructions for deploying a high-throughput LLM inference pipeline on MI300X.

Whether you're deploying MI300X at scale in a hyperscaler data center or integrating it into an on-prem AI cluster, this guide is your central reference for maximizing performance, stability, and resource efficiency.
