# testing servers network with iperf3
# server LFF 223 server side & SFF 222 client side
## command 
### server side 
```bash
$ iperf3 -s
```
### client side
```bash
$ iperf3 -c 192.168.88.236
```
## resault on server
```
resault: Server listening on 5201
-----------------------------------------------------------
Accepted connection from 192.168.88.235, port 60088
[  5] local 192.168.88.236 port 5201 connected to 192.168.88.235 port 60090
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   1.00-2.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   2.00-3.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   3.00-4.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   4.00-5.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   5.00-6.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   6.00-7.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   7.00-8.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   8.00-9.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   9.00-10.00  sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]  10.00-10.00  sec   255 KBytes  8.87 Gbits/sec                  
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-10.00  sec  11.0 GBytes  9.41 Gbits/sec                  receiver

```
## resault on client
```
resault: Connecting to host 192.168.88.236, port 5201
[  5] local 192.168.88.235 port 60090 connected to 192.168.88.236 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.10 GBytes  9.43 Gbits/sec    0   1.65 MBytes       
[  5]   1.00-2.00   sec  1.10 GBytes  9.42 Gbits/sec    0   1.65 MBytes       
[  5]   2.00-3.00   sec  1.09 GBytes  9.41 Gbits/sec    0   1.65 MBytes       
[  5]   3.00-4.00   sec  1.10 GBytes  9.42 Gbits/sec    0   1.65 MBytes       
[  5]   4.00-5.00   sec  1.10 GBytes  9.42 Gbits/sec    0   1.65 MBytes       
[  5]   5.00-6.00   sec  1.10 GBytes  9.42 Gbits/sec    0   1.73 MBytes       
[  5]   6.00-7.00   sec  1.10 GBytes  9.41 Gbits/sec    0   1.73 MBytes       
[  5]   7.00-8.00   sec  1.10 GBytes  9.41 Gbits/sec    0   1.73 MBytes       
[  5]   8.00-9.00   sec  1.09 GBytes  9.41 Gbits/sec    0   1.73 MBytes       
[  5]   9.00-10.00  sec  1.10 GBytes  9.42 Gbits/sec    0   1.73 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  11.0 GBytes  9.42 Gbits/sec    0             sender
[  5]   0.00-10.00  sec  11.0 GBytes  9.41 Gbits/sec                  receiver
```


# server SFF 222 side & LFF 223 server client side
## command 
### server side 
```bash
$ iperf3 -s
```
### client side
```bash
$ iperf3 -c 192.168.88.234
```
## resault on server
```
resault: Accepted connection from 192.168.88.237, port 55188
[  5] local 192.168.88.234 port 5201 connected to 192.168.88.237 port 55190
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   1.00-2.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   2.00-3.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   3.00-4.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   4.00-5.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   5.00-6.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   6.00-7.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   7.00-8.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   8.00-9.00   sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]   9.00-10.00  sec  1.10 GBytes  9.41 Gbits/sec                  
[  5]  10.00-10.00  sec   827 KBytes  9.32 Gbits/sec                  
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-10.00  sec  11.0 GBytes  9.41 Gbits/sec                  receiver

```
## resault on client
```
resault: Connecting to host 192.168.88.234, port 5201
[  5] local 192.168.88.237 port 55190 connected to 192.168.88.234 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec  1.10 GBytes  9.44 Gbits/sec    0   1.64 MBytes       
[  5]   1.00-2.00   sec  1.09 GBytes  9.41 Gbits/sec    0   1.64 MBytes       
[  5]   2.00-3.00   sec  1.10 GBytes  9.42 Gbits/sec    0   1.72 MBytes       
[  5]   3.00-4.00   sec  1.10 GBytes  9.42 Gbits/sec    0   1.72 MBytes       
[  5]   4.00-5.00   sec  1.10 GBytes  9.42 Gbits/sec    0   1.72 MBytes       
[  5]   5.00-6.00   sec  1.10 GBytes  9.41 Gbits/sec    0   1.72 MBytes       
[  5]   6.00-7.00   sec  1.10 GBytes  9.41 Gbits/sec    0   1.72 MBytes       
[  5]   7.00-8.00   sec  1.09 GBytes  9.41 Gbits/sec    0   1.72 MBytes       
[  5]   8.00-9.00   sec  1.10 GBytes  9.42 Gbits/sec    0   1.72 MBytes       
[  5]   9.00-10.00  sec  1.10 GBytes  9.42 Gbits/sec    0   1.72 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  11.0 GBytes  9.42 Gbits/sec    0             sender
[  5]   0.00-10.00  sec  11.0 GBytes  9.41 Gbits/sec                  receiver
```