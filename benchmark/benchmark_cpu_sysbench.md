# CPU

## testing

> 1. my_laptop:
> - cpu: Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz - 4 cores & 8 threads
> ```bash
> - $ sysbench --test=cpu --cpu-max-prime=20000 run
> ```
> ```bash
> - resaults: CPU speed:
>    events per second:   435.22
>
> General statistics:
>    total time:                          10.0004s
>    total number of events:              4353
>
> Latency (ms):
>         min:                                    1.95
>         avg:                                    2.30
>         max:                                    3.52
>         95th percentile:                        2.61
>         sum:                                 9995.28
>
> Threads fairness:
>    events (avg/stddev):           4353.0000/0.00
>    execution time (avg/stddev):   9.9953/0.00
> ```
> 2. server LFF 232:
> - cpu: Intel(R) Xeon(R) CPU E5-2667 v2 @ 3.30GHz - 8 cores & 16 threads
> ```bash
> - $ sysbench --test=cpu --cpu-max-prime=20000 run
> ```
> 
> ```bash
> - resaults: CPU speed:
>    events per second:   357.54
>
> General statistics:
>    total time:                          10.0012s
>    total number of events:              3577
>
> Latency (ms):
>         min:                                    2.31
>         avg:                                    2.80
>         max:                                    6.38
>         95th percentile:                        2.81
>         sum:                                10000.17
>
> Threads fairness:
>    events (avg/stddev):           3577.0000/0.00
>    execution time (avg/stddev):   10.0002/0.00
> ```
> 3. server SFF 235:
> - cpu: Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz - 10 cores & 20 threads
> ```bash
> - $ sysbench --test=cpu --cpu-max-prime=20000 run
> ```
> 
> ```bash
> - resaults: CPU speed:
>    events per second:   369.90
>
> General statistics:
>    total time:                          10.0018s
>    total number of events:              3701
>
> Latency (ms):
>         min:                                    2.56
>         avg:                                    2.70
>         max:                                    7.48
>         95th percentile:                        3.07
>         sum:                                10000.98
>
> Threads fairness:
>    events (avg/stddev):           3701.0000/0.00
>    execution time (avg/stddev):   10.0010/0.00
> ```