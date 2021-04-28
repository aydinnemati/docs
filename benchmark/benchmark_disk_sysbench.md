> # Disk I/Ops Tests
> ### SYSBENCH

# *** Please make sure that you should select size of test file to be more than your amount of RAM ***

## disk model
```bash 
$ sudo apt install udisks2
$ udisksctl  status
```
## install sysbench
```bash
$ sudo apt-get install sysbench
```
## testing
> 1. my_laptop:
> ```bash
> - $ sysbench fileio --file-total-size=15G --file-test-mode=rndrw --time=300 --max-requests=0 prepare
> - $ sysbench fileio --file-total-size=15G --file-test-mode=rndrw --time=300 --max-requests=0 run
> - $ sysbench fileio --file-total-size=15G --file-test-mode=rndrw --time=300 --max-requests=0 cleanup
> ```
> ```bash
> - resaults:
> File operations:
>    reads/s:                      469.62
>    writes/s:                     313.08
>    fsyncs/s:                     1001.94
>
> Throughput:
>    read, MiB/s:                  7.34
>    written, MiB/s:               4.89
>
> General statistics:
>    total time:                          300.1051s
>    total number of events:              535466
>
> Latency (ms):
>         min:                                    0.00
>         avg:                                    0.56
>         max:                                   16.02
>         95th percentile:                        3.30
>         sum:                               299139.12
>
> Threads fairness:
>    events (avg/stddev):           535466.0000/0.00
>    execution time (avg/stddev):   299.1391/0.00
>
> ```
> 2. server LFF 232:
> ```bash
> - $ time dd if=/data/benchmarks/test1.img of=/dev/null bs=8k
> ```
> ```bash
> - resaults: File operations:
>    reads/s:                      973.22
>    writes/s:                     648.81
>    fsyncs/s:                     2076.37
>
> Throughput:
>    read, MiB/s:                  15.21
>    written, MiB/s:               10.14
>
> General statistics:
>    total time:                          300.0519s
>    total number of events:              1109600
>
> Latency (ms):
>         min:                                    0.00
>         avg:                                    0.27
>         max:                                   85.20
>         95th percentile:                        2.18
>         sum:                               299292.97
>
> Threads fairness:
>    events (avg/stddev):           1109600.0000/0.00
>    execution time (avg/stddev):   299.2930/0.00
> ```