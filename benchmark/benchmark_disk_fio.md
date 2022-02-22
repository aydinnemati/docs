# FIO benchmark disk 
[See more...](https://fio.readthedocs.io/en/latest/)

## install fio
```bash
$ sudo apt install fio
```
### good to know: 
- directory that command is executing in it will be tested 
for example directory /media/a witch is in usb SONY , 
tests that SONY usb.

## simple sample command for random write testing :
```bash
$ sudo fio --name=random-write --ioengine=posixaio --rw=randwrite --bs=4k --numjobs=1 --size=4g --iodepth=1 --runtime=60 --time_based --end_fsync=1
```
> ### Let's break down what each argument does.

>#### --name=
>- is a required argument, but it's basically human-friendly fluff—fio will create files based on that name to test with, inside the working directory you're currently in.

> #### --ioengine=posixaio
> - sets the mode fio interacts with the filesystem. POSIX is a standard Windows, Macs, Linux, and BSD all understand, so it's great for portability—although inside fio itself, Windows users need to invoke --ioengine=windowsaio, not --ioengine=posixaio, unfortunately. AIO stands for Asynchronous Input Output and means that we can queue up multiple operations to be completed in whatever order the OS decides to complete them. (In this particular example, later arguments effectively nullify this.)

> #### --rw=
> - randwrite means exactly what it looks like it means: we're going to do random write operations to our test files in the current working directory. Other options include seqread, seqwrite, randread, and randrw, all of which should hopefully be fairly self-explanatory.

> #### --bs=4k
> - blocksize 4K. These are very small individual operations. This is where the pain lives; it's hard on the disk, and it also means a ton of extra overhead in the SATA, USB, SAS, SMB, or whatever other command channel lies between us and the disks, since a separate operation has to be commanded for each 4K of data.

> #### --size=4g 
> - our test file(s) will be 4GB in size apiece. (We're only creating one, see next argument.)

> #### --numjobs=1 
> - we're only creating a single file, and running a single process commanding operations within that file. If we wanted to simulate multiple parallel processes, we'd do, eg, --numjobs=16, which would create 16 separate test files of --size size, and 16 separate processes operating on them at the same time.


## sample resault 
```bash
Run status group 0 (all jobs):
  WRITE: bw=116MiB/s (122MB/s), 116MiB/s-116MiB/s (122MB/s-122MB/s), io=8192MiB (8590MB), run=70635-70635msec
```

# sample testing commands:
- ### Single 4KiB random write process
```bash
$ sudo fio --name=random-write --ioengine=posixaio --rw=randwrite --bs=4k --size=4g --numjobs=1 --iodepth=1 --runtime=60 --time_based --end_fsync=1
```
- ### 16 parallel 64KiB random write processes
```bash
$ sudo fio --name=random-write --ioengine=posixaio --rw=randwrite --bs=64k --size=256m --numjobs=16 --iodepth=16 --runtime=60 --time_based --end_fsync=1
```
- ### Single 1MiB random write process
```bash
$ sudo fio --name=random-write --ioengine=posixaio --rw=randwrite --bs=1m --size=16g --numjobs=1 --iodepth=1 --runtime=60 --time_based --end_fsync=1
```