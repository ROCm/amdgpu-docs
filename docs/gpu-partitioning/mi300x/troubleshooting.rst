Troubleshooting
==================

This section provides a comprehensive guide to diagnosing and resolving common issues that may arise during the GPU partitioning and workload execution process on AMD MI300X systems. Given the complexity of managing GPU resources across multiple partitions, users may encounter errors stemming from permission misconfigurations, resource contention, incompatible memory modes, or system-level driver conflicts. 

The troubleshooting guidance here aims to equip system administrators, ML engineers, and HPC practitioners with actionable solutions and detailed context to restore correct system behavior and accelerate productivity. Each issue is presented with relevant command examples, expected error messages, and precise resolution steps to minimize guesswork and enable swift remediation.

Topics covered include:
- Resolving permission-denied errors when invoking `amd-smi` partitioning commands.
- Handling GPU resource conflicts during partition creation or reset.
- Diagnosing partition incompatibilities between memory and compute modes.
- Addressing missing GPU visibility in CPX mode caused by Linux kernel video driver issues.

For optimal system operation, it is recommended to thoroughly read through each scenario and verify all preconditions (e.g., compute mode, memory mode, driver state) before applying corrective actions. In complex environments with multiple GPUs or users, coordination across software stack components — from container runtimes and kernel drivers to benchmarking frameworks — is crucial for sustained platform stability and performance.

1. Error while running amd-smi command for partitioning
--------------------------------------------------------

If you receive an error when executing partitioning commands using `amd-smi`, verify that you are running the command with elevated permissions.

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Check if the GPU is in use
            amd-smi set --gpu all --compute-partition SPX


      .. tab-item:: Shell output

         ::

            amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
            10 | AMDSMI_STATUS_NO_PERM - Permission Denied

            The above exception was the direct cause of the following exception:

            PermissionError: Command requires elevation

**Resolution:**

- Ensure the command is executed with `sudo`.
- Confirm that no applications or system services are currently utilizing the GPU. If so, terminate or stop them before retrying.

2. Error while creating partitions
-----------------------------------

Partitioning operations can fail if the GPU is actively being used by another process.

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # setting memory partition mode
            sudo amd-smi set --gpu all --compute-partition SPX

      .. tab-item:: Shell output

         ::

            amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
            30 | AMDSMI_STATUS_BUSY - Device busy

            The above exception was the direct cause of the following exception:

            ValueError: Unable to set accelerator partition to SPX on GPU ID: 0 BDF:0000:11:00.0

**Resolution:**

- Ensure that no compute workloads or system services are using the GPU.
- Use `amd-smi`, `ps -aux`, `top` -like tools to identify running GPU jobs.
- Terminate conflicting jobs before retrying the partition command.           

3. Error while resetting partition to SPX
-------------------------------------------

NPS4 memory mode is only compatible with CPX compute mode. If you attempt to switch to SPX while memory mode is still set to NPS4, the operation will fail.

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Set compute partition mode
            sudo amd-smi set --gpu all --compute-partition SPX    

      .. tab-item:: Shell output

         ::

            Attempted to set accelerator partition to SPX (profile #0 on GPU ID: 0 BDF:0000:11:00.0

            [AMDSMI_STATUS_SETTING_UNAVAILABLE] Please check amd-smi partition --memory --accelerator for available profiles.
            Users may need to switch memory partition to another mode in order to enable the desired accelerator partition.

            amdsmi.amdsmi_exception.AmdSmiLibraryException: Error code:
                    55 | AMDSMI_STATUS_SETTING_UNAVAILABLE - Setting is not available

            The above exception was the direct cause of the following exception:

            ValueError: [AMDSMI_STATUS_SETTING_UNAVAILABLE] Unable to set accelerator partition to SPX on GPU ID: 0 BDF:0000:11:00.0

**Resolution:**

Before switching to SPX mode, first revert the memory partition mode to NPS1:

   .. tab-set::

      .. tab-item:: Command

         .. code-block:: shell-session

            # Set memory partition mode
            sudo amd-smi set --memory-partition NPS1  

      .. tab-item:: Shell output

         ::

            GPU: 0
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 1
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 2
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 3
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 4
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 5
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 6
                MEMORY_PARTITION: Successfully set memory partition to NPS1

            GPU: 7
                MEMORY_PARTITION: Successfully set memory partition to NPS1

Once complete, you can safely reset compute partitioning to SPX mode.
   
4. All 64 GPUs not visible in `amd-smi` output in CPX mode
-----------------------------------------------------------

In CPX mode, the system should expose 64 logical GPUs (8 per physical MI300X device). If you observe fewer GPUs, it may be due to a known Linux kernel issue involving the BMC virtual video driver. On most systems this virtual video driver is AST (ASPEED AST media controller). 

**Resolution:**

Unload the AST video driver and reload the AMD GPU kernel modules:

.. code-block:: bash
  
    # Unload the BMC virtual video driver
    sudo modprobe -r ast

    # Unload the amdgpu driver
    sudo modprobe -r amdgpu

    # Load the amdgpu driver
    sudo modprobe amdgpu

After these steps, rerun `amd-smi` to verify that all 64 GPUs are now visible.

.. note::
   If the AST driver cannot be unloaded due to it being in use, consider blacklisting the AST module in `/etc/modprobe.d/blacklist.conf` and rebooting the system.
