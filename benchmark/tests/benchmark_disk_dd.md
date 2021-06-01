> # Disk I/Ops Tests
> ### DD
## clear cache
```bash 
$ echo 3 | sudo tee /proc/sys/vm/drop_caches
```
## disk model
```bash 
$ sudo apt install udisks2
$ udisksctl  status
```
> ## sequential read 
> ### throughput
> 1. my_laptop:
> - disk: Samsung SSD 850 EVO 500GB EMT02B6Q
> ```bash
> - $ time dd if=/path/to/bigfile of=/dev/null bs=8k
> ```
> ```bash
> - resaults:131072+0 records in
> 131072+0 records out
> 1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.278144 s, 3.9 GB/s
>
> real	0m0.281s
> user	0m0.108s
> sys	0m0.173s
> ```
> 2. server LFF 232:
> ```bash
> - $ time dd if=/data/benchmarks/test1.img of=/dev/null bs=8k
> ```
> ```bash
> - resaults: 131072+0 records in
> 131072+0 records out
> 1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.295073 s, 3.6 GB/s
>
> real	0m0.297s
> user	0m0.061s
> sys	0m0.237s
> ```

> ## sequential write
> ### lateancy
> 1. my_laptop:
> - disk: Samsung SSD 850 EVO 500GB EMT02B6Q
> ```bash
> - $ dd if=/dev/zero of=/tmp/test2.img bs=512 count=1000 oflag=dsync
> ```
> ```bash
> - resaults: 512000 bytes (512 kB, 500 KiB) copied, 2.20007 s, 233 kB/s
> ```
> 2. server LFF 232:
> ```bash
> - $ sudo dd if=/dev/zero of=/data/benchmarks/test2.img bs=512 count=1000 oflag=dsync
> ```
> ```bash
> - resaults: 512000 bytes (512 kB, 500 KiB) copied, 0.0953887 s, 5.4 MB/s
> ```
> ### throughput
> 1. my_laptop:
> - disk: Samsung SSD 850 EVO 500GB EMT02B6Q
> ```bash
> - $ dd if=/dev/zero of=/tmp/test1.img bs=1G count=1 oflag=dsync
> ```
> ```bash
> - resaults: 1073741824 bytes (1.1 GB, 1.0 GiB) copied, 2.56818 s, 418 MB/s
> ```
> 2. server LFF 232:
> ```bash
> - $ sudo dd if=/dev/zero of=/data/benchmarks/test1.img bs=1G count=1 oflag=dsync
> ```
> ```bash
> - resaults: 1073741824 bytes (1.1 GB, 1.0 GiB) copied, 2.95587 s, 363 MB/s
> ```
> ## random read 
> ### throughput
> 1. my_laptop:
> - disk: Samsung SSD 850 EVO 500GB EMT02B6Q
> ```bash
> - $
> ```
> ```bash
> - resaults:
> ```
> 2. server LFF 232:
> ```bash
> - $
> ```
> ```bash
> - resaults:
> ```
> ## random write
> ### lateancy
> 1. my_laptop:
> - disk: Samsung SSD 850 EVO 500GB EMT02B6Q
> ```bash
> - $
> ```
> ```bash
> - resaults:
> ```
> 2. server LFF 232:
> ```bash
> - $
> ```
> ```bash
> - resaults:
> ```
> ### throughput
> 1. my_laptop:
> - disk: Samsung SSD 850 EVO 500GB EMT02B6Q
> ```bash
> - $
> ```
> ```bash
> - resaults:
> ```
> 2. server LFF 232:
> ```bash
> - $
> ```
> ```bash
> - resaults:
> ```