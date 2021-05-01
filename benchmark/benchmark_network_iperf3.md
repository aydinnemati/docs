# Iperf3
```bash
$ sudo apt install
```
# How to Test Network Throughput Between Linux Servers
[See More...](https://www.tecmint.com/test-network-throughput-in-linux/)

# run on server:
```bash
$ iperf3 -s
```
### default port 
> - 5201
### switches
> - -f | k, m, g for Kbits, Mbits, Gbits or K, M, G for KBytes, Mbytes, Gbytes
> - -p | user define port
# run on client
```bash
$ iperf3 -c {{ip to server that running iperf3}}
```