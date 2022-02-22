# command options
- direct=true | disables buffer use
## readwrite=str, rw=str:
- 1.  read | Sequential reads
- 2. write | Sequential writes
- 3. trim | Sequential trims (Linux block devices and SCSI character devices only)
- 4. randread | Random reads
- 5. randwrite | Random writes
- 6. randtrim | Random trims (Linux block devices and SCSI character devices only)
- 7. rw,readwrite | Sequential mixed reads and writes
- 8. randrw | Random mixed reads and writes
- 9. trimwrite | Sequential trim+write sequences. Blocks will be trimmed first, then the same blocks will be written to


# server 223 LFF:
> ## raid 0:
- disk: SATA 3 TB 7200rpm hp model MB3000GBKAC
### path
> - /data-1-r0
- ### command:
```bash
$ sudo fio --ioengine=posixaio --bs=4k --numjobs=1 --size=4g --iodepth=1 --runtime=60 --time_based --name=random-write --rw=rw --direct=1
``` 

```bash
resault: Run status group 0 (all jobs):
   READ: bw=35.8MiB/s (37.6MB/s), 35.8MiB/s-35.8MiB/s (37.6MB/s-37.6MB/s), io=2149MiB (2254MB), run=60001-60001msec
  WRITE: bw=35.8MiB/s (37.5MB/s), 35.8MiB/s-35.8MiB/s (37.5MB/s-37.5MB/s), io=2148MiB (2252MB), run=60001-60001msec
```

# server 222 SFF:
> ## raid 5:
> - disk: SAS 900 GB hp model EG0900FCSPN 
### path
> - /data-04-r5
- ### command:
```bash
$ sudo fio --ioengine=posixaio --bs=4k --numjobs=1 --size=4g --iodepth=1 --runtime=60 --time_based --name=random-write --rw=rw --direct=1
```
```bash
resault: Run status group 0 (all jobs):
   READ: bw=47.6MiB/s (49.9MB/s), 47.6MiB/s-47.6MiB/s (49.9MB/s-49.9MB/s), io=2856MiB (2995MB), run=60001-60001msec
  WRITE: bw=47.5MiB/s (49.8MB/s), 47.5MiB/s-47.5MiB/s (49.8MB/s-49.8MB/s), io=2852MiB (2991MB), run=60001-60001msec 
```
> ## raid 0:
> - disk: SAS 900 GB hp model EG0900FCSPN 
### path
> - /data-01-r0
- ### command:
### path
> - /data
```bash
$ sudo fio --ioengine=posixaio --bs=4k --numjobs=1 --size=4g --iodepth=1 --runtime=60 --time_based --name=random-write --rw=rw --direct=1
```
```bash
resault: Run status group 0 (all jobs):
   READ: bw=43.3MiB/s (45.4MB/s), 43.3MiB/s-43.3MiB/s (45.4MB/s-45.4MB/s), io=2600MiB (2726MB), run=60001-60001msec
  WRITE: bw=43.3MiB/s (45.4MB/s), 43.3MiB/s-43.3MiB/s (45.4MB/s-45.4MB/s), io=2598MiB (2724MB), run=60001-60001msec
```

# my laptop
- ### command:
```bash
$ sudo fio --ioengine=posixaio --bs=4k --numjobs=1 --size=4g --iodepth=1 --runtime=60 --time_based --name=random-write --rw=rw --direct=1
```
```bash
resault: Run status group 0 (all jobs):
   READ: bw=29.3MiB/s (30.7MB/s), 29.3MiB/s-29.3MiB/s (30.7MB/s-30.7MB/s), io=1757MiB (1843MB), run=60001-60001msec
  WRITE: bw=29.3MiB/s (30.7MB/s), 29.3MiB/s-29.3MiB/s (30.7MB/s-30.7MB/s), io=1756MiB (1841MB), run=60001-60001msec
```

