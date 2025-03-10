Use cases
=================================================

Instead of installing individual applications or libraries, the installer script groups packages into specific
use cases that match typical workflows and runtimes.

To display a list of available use cases, run:

.. code-block:: bash

    sudo amdgpu-install --list-usecase

The available use-cases are printed in a format similar to:

.. code-block::

    If --usecase option is not present, the default selection is "graphics,opencl,hip"

    Available use cases:
    dkms            (to only install the kernel mode driver)
      - Kernel mode driver (included in all usecases)
    graphics        (for users of graphics applications)
      - Open source Mesa 3D graphics and multimedia libraries
    multimedia      (for users of open source multimedia)
      - Open source Mesa 3D multimedia libraries
    multimediasdk   (for developers of open source multimedia)
      - Open source Mesa 3D multimedia libraries
      - Development headers for multimedia libraries
    workstation     (for users of legacy WS applications)
      - Open source multimedia libraries
      - Closed source (legacy) OpenGL
    rocm            (for users and developers requiring full ROCm stack)
      - OpenCL (ROCr/KMD based) runtime
      - HIP runtimes
      - Machine learning framework
      - All ROCm libraries and applications
    rocmdev         (for developers requiring ROCm runtime and
                    profiling/debugging tools)
      - HIP runtimes
      - OpenCL runtime
      - Profiler, Tracer and Debugger tools
    rocmdevtools    (for developers requiring ROCm profiling/debugging tools)
      - Profiler, Tracer and Debugger tools
    amf             (for users of AMF based multimedia)
      - AMF closed source multimedia library
    lrt             (for users of applications requiring ROCm runtime)
      - ROCm Compiler and device libraries
      - ROCr runtime and thunk
    opencl          (for users of applications requiring OpenCL on Vega or later
                    products)
      - ROCr based OpenCL
      - ROCm Language runtime
    openclsdk       (for application developers requiring ROCr based OpenCL)
      - ROCr based OpenCL
      - ROCm Language runtime
      - development and SDK files for ROCr based OpenCL
    hip             (for users of HIP runtime on AMD products)
      - HIP runtimes
    hiplibsdk       (for application developers requiring HIP on AMD products)
      - HIP runtimes
      - ROCm math libraries
      - HIP development libraries
    openmpsdk       (for users of openmp/flang on AMD products)
      - OpenMP runtime and devel packages
    mllib           (for users executing machine learning workloads)
      - MIOpen hip/tensile libraries
      - Clang OpenCL
      - MIOpen kernels
    mlsdk           (for developers executing machine learning workloads)
      - MIOpen development libraries
      - Clang OpenCL development libraries
      - MIOpen kernels
    asan            (for users of ASAN enabled ROCm packages)
      - ASAN enabled OpenCL (ROCr/KMD based) runtime
      - ASAN enabled HIP runtimes
      - ASAN enabled Machine learning framework
      - ASAN enabled ROCm libraries

Install amdgpu-dkms
-------------------------------------------------

In order to install only the DKMS, which is a minimal requirement for launching containers with GPU
access, use the ``dkms`` use case:

.. code-block:: bash

   amdgpu-install --usecase=dkms

To verify the kernel installation, use this command:

.. code-block:: shell

   sudo dkms status

If the installation of the kernel module was successful, the command displays the output
in the following format:

.. code-block:: shell

   amdgpu, 4.3-52.el7, 3.10.0-1160.11.1.el7.x86_64, x86_64: installed (original_module exists)
