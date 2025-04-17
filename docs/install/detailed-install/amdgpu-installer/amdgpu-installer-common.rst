Install amdgpu-dkms
-------------------------------------------------

In order to install only the DKMS, which is a minimal requirement for launching containers with GPU
access, use the ``dkms`` use case:

.. code-block:: bash

   sudo amdgpu-install --usecase=dkms

To verify the kernel installation, use this command:

.. code-block:: shell

   sudo dkms status

If the installation of the kernel module was successful, the command displays the output
in the following format:

.. code-block:: shell

   amdgpu, 4.3-52.el7, 3.10.0-1160.11.1.el7.x86_64, x86_64: installed (original_module exists)
