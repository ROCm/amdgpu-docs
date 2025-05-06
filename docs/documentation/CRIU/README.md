# What is CRIU?

Checkpoint and Restore in Userspace (CRIU) is a utility that allows the state of another running program (or an entire container) to be saved to disk.
The data saved can later be used to restart the program as it was at the moment it was captured on the same computer or a different one.

CRIU is a fully open source project. CRIU can be installed with your package manager of choice or built from source from: https://github.com/checkpoint-restore/criu.git.
CRIU documentation can be found on the [CRIU wiki](http://criu.org/).

## CRIU Support with AMDs

CRIU has a plugin to support checkpoint and restore of processes that have AMDGPU resources such as buffer objects and queues.
This plugin is open-source and part of upstream CRIU, and is enabled by default. The plugin supports processes that use amdkfd kernel interfaces, but not amdgpu ones

CRIU works only on Linux. CRIU requires superuser permissions. Because a CRIU dump contains copies of all memory held by the target process (both RAM and VRAM),
CRIU dumps can be quite large. CRIU does not support graphical applications or distributed applications.

To use CRIU, first the process you want to checkpoint must be running. Start a new shell and navigate to an empty directory. Find the process ID of the process
you want to checkpoint with ps or a similar utility. In the new shell, run:

```shell
sudo criu dump -vvv --shell-job --link-remap --ext-unix-sk -o dump.log -t <pid>
```

When CRIU is finished, the target process will be dead and there will be a large number of files in the directory.

To restore a process, navigate to the directory containing all the files that resulted from checkpoint and run:

```shell
sudo criu restore -vvv --shell-job --link-remap --ext-unix-sk -o restore.log
```

## Common Command-Line Options

Theses are common command-line options used with CRIU:

```shell
-vvv -o <logfile>
```

Create a logfile for this CRIU operation with maximum verboseness. The files can be named anything you wish.

```shell
--shell-job (or -j)
```

This option is required when checkpointing a process that was started from the shell

```shell
--ext-unix-sk
```

This option is required when checkpointing any process that opens a socket

```shell
--link-remap
```

This option is required when checkpointing any process that opens files

```shell
--file-locks
```

This option is required when checkpointing any process that holds file locks

If one of the above four options is missing and needed, the dump and restore log will contain a helpful message telling you so

```shell
--ext-mount-map
```

This option is required to handle docker's unusual way of mounting the /etc/* files

```shell
--ghost-limit <size>
```

Sets the maximum size of [invisible files](https://criu.org/Invisible_files) that CRIU will save.

## Common CRIU Errors

If you see something like this:
>unsupported action \
>create table inet criu \
>Then your kernel was built without NF_TABLES_INET. This kernel option is necessary for CRIU to work

CRIU copies the checkpointed program's entire memory footprint into storage. If the program has allocated more RAM than there is
available storage on the file system, CRIU will fail, possibly with an error in the dump log such as:

>Error (criu/bfd.c:131): bfd: Error flushing image: No space left on device \
>(You can use command "top" to see a running program's memory usage, and command "df" to see the available space in currently mounted drives) \
>There is no solution for this. In particular, this means that, on some systems, checkpointing the kfdtest `LargestSysBufferTest` may be impossible

Something like this:
>(00.150425) Error (criu/mount.c:753): mnt: 730:./etc/hosts doesn't have a proper root mount \
> This is a docker quirk: you need --ext-mount-map

 If the dump or restore log contains a line that mentions a CRIU command line option such as:

>(00.087742) Error (criu/file-lock.c:110): Some file locks are hold by dumping tasks! You can try --file-locks to dump them \
>You need that option

If the dump log contains a line like:

```shell
(00.104296) Error (criu/files-reg.c:1031): Can't dump ghost file /dev/shm/nccl-tsD6S7 of 1052672 size, increase limit 
```

 then you need to increase the --ghost-limit option
