Steps to Run a vLLM Workload
=============================

Introduction
------------

This document provides a step-by-step guide to executing large language model (LLM) inference workloads using the vLLM engine on AMD Instinct™ MI300X GPUs. vLLM is a high-throughput and memory-efficient inference engine optimized for transformer-based models, capable of achieving near-zero latency and maximum throughput through continuous batching and memory planning.

These instructions assume that your MI300X GPUs have already been correctly partitioned into CPX/NPS4 modes and are accessible to the container runtime via the ROCm software stack. The guide walks through container setup, dependency configuration, and model execution using a real-world benchmark script provided by AMD. Each section provides detailed command examples, expected behavior, and practical configuration tips to help you validate performance, resource allocation, and model compatibility with the underlying hardware.

This document is particularly useful for AI developers, performance engineers, and infrastructure administrators seeking to validate multi-GPU inference performance, confirm partitioning behavior, and optimize GPU resource allocation for LLM workloads in ROCm-based environments.

---

1. One-Time Setup
------------------

Pull the prebuilt AMD container for vLLM workloads. This container includes all necessary ROCm libraries and pre-installed dependencies.

.. code-block:: bash

    # one time setup
    sudo docker pull rocm/vllm:instinct_main

---

2. Launching the Container
---------------------------

Run the container with the required privileges and device mappings to enable GPU access:

.. code-block:: bash

    # run the docker image and open a bash terminal
    sudo docker run -it --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device /dev/kfd --device /dev/dri rocm/vllm:instinct_main /bin/bash

---

3. Cloning the Benchmark Suite
-------------------------------

Inside the container, clone the ROCm/MAD repository and navigate to the vLLM benchmarking script directory:

.. code-block:: bash

    # clone the AMD MAD repo to run vllm workload from inside the docker image
    git clone https://github.com/ROCm/MAD.git
    cd MAD
    # install any dependencies required for the benchmark script including python packages and libraries
    pip install -r requirements.txt
    cd MAD/scripts/vllm

---

4. Authentication - Hugging Face Token
---------------------------------------

To download LLM models such as `Llama-3`, you need a Hugging Face account and an access token.
Create a Hugging Face account and generate a personal access token from your Hugging Face profile. Then export it:

.. code-block:: bash

    # create Hugging Face account and use that token below
    export HF_TOKEN="your_HuggingFace_token"

This token is used to pull LLM models (e.g., Llama-3) from Hugging Face.

---

5. How to Check if an LLM Fits within a CPX GPU?
--------------------------------------------------

Before executing a workload, it is critical to ensure that the selected model can fit entirely within the memory available on a single CPX GPU partition, particularly when using CPX/NPS4 mode (which provides 24GB per partition).

A model will typically fit on a single GPU partition if:

::

   size_of_weights + size_of_KV_cache < available_VRAM

The size of the **Key-Value (KV) cache** is workload-dependent and driven by batch size, sequence length, and model architecture.

**Formula for KV cache size per token (in bytes):**

::

   kv_cache_per_token = 2 × n_layers × hidden_dim × precision_in_bytes

Where:

- `2` accounts for Key and Value caches
- `n_layers` is the number of transformer layers
- `hidden_dim` = n_heads × d_head
- `precision_in_bytes` is 2 for float16 and bfloat16, 4 for float32

**Total KV cache size in bytes:**

::

   total_kv_cache = batch_size × seq_length × kv_cache_per_token

---

**Example 1: Llama-2-7B (FP16)**

::

   Model weights ≈ 2 × 7 = 14 GB
   kv_cache_per_token = 2 × 32 × 4096 × 2 = 524,288 bytes
   total_kv_cache = 1 × 4096 × 524,288 ≈ 2 GB
   Total memory usage = 14 GB + 2 GB = 16 GB

✅ This model fits within a single CPX GPU partition (24 GB VRAM).

---

**Example 2: Llama-2-13B (FP16)**

::

   Model weights ≈ 2 × 13 = 26 GB
   kv_cache_per_token = 2 × 40 × 5120 × 2 = 819,200 bytes
   total_kv_cache = 1 × 4096 × 819,200 ≈ 3.6 GB
   Total memory usage = 26 GB + 3.6 GB ≈ 29.6 GB

❌ This model exceeds a single 24 GB CPX partition and will require multiple partitions or tensor parallelism.

---

How do above partitions affect LLM models?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - With reduced memory in the CPX mode (24GB HBM per XCD), models may not fit within one CPX GPU. So, models have to be partitioned across multiple CPX GPUs using tensor parallelism.
    - With reduced compute in the CPX mode (38CUs per XCD), models may be compute bounded if they run on lesser XCD units compared to SPX mode. As above, using tensor parallelism to split the model across multiple CPX GPUs can take advantage of more compute units.

**Summary:** Always pre-calculate memory needs and compute needs for your selected model and batch size to determine the appropriate number of CPX partitions (i.e., GPUs) to assign.

---

6. GPU Selection (Optional)
----------------------------

If you wish to limit the vLLM workload to a specific set of GPUs (e.g., 8 out of the total available), define the HIP_VISIBLE_DEVICES environment variable. If left unset, all GPUs are utilized.

.. code-block:: bash

    # set the environment variables for the GPUs to be used
    # leave this blank if you want to use all GPUs
    # to use the first 8 GPUs, set the variable to 0,1,2,3,4,5,6,7
    export HIP_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

---

7. Running the vLLM Benchmark
------------------------------

The benchmark script accepts several command-line options to customize the test. Here's an example that runs the meta-llama/Llama-3.1-8B-Instruct model on 8 GPUs in FP16 mode:

.. code-block:: bash

    # from the app/MAD/scripts/vllm directory, run the following command to run the vllm workload
    # -g 1 means to use 1 GPU, -g 8 means to use 8 GPUs, etc.
    # please refer to the README on the ROCm/MAD GitHub repo for more details on the command line options
    ./vllm_benchmark_report.sh -s all -m meta-llama/Llama-3.1-8B-Instruct -g 8 -d float16

---

**Command Breakdown:**

- `-s all`: Run all benchmark tests (latency, throughput, etc.)
- `-m`: Hugging Face model name to use (e.g., `meta-llama/Llama-3.1-8B-Instruct`)
- `-g`: Number of GPUs to use
- `-d`: Precision mode (choose from `float16`, `bfloat16`, `float32`)

For additional options (e.g., batch size, sequence length, tokenizer config), refer to the `MAD/scripts/vllm/README.md` file in the GitHub repository.

.. note::
   Ensure that your container has internet access to pull models from Hugging Face during benchmarking.
