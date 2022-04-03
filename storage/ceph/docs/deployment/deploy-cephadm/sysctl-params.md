# mastering ceph book
- page [238]
```bash
#Network buffers
net.core.rmem_max = 56623104
net.core.wmem_max = 56623104
net.core.rmem_default = 56623104
net.core.wmem_default = 56623104
net.core.optmem_max = 40960
net.ipv4.tcp_rmem = 4096 87380 56623104
net.ipv4.tcp_wmem = 4096 65536 56623104
#Maximum connections and backlog
net.core.somaxconn = 1024
net.core.netdev_max_backlog = 50000
#TCP tuning options
net.ipv4.tcp_max_syn_backlog = 30000
net.ipv4.tcp_max_tw_buckets = 2000000
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_fin_timeout = 10
#Don't use slow start on idle TCP connections
net.ipv4.tcp_slow_start_after_idle = 0
```
# getting params
```bash
$ sudo sysctl -a | grep {{?}}
```

# defaults
```bash
net.core.rmem_max = 212992
net.core.wmem_max = 212992
net.core.rmem_default = 212992
net.core.wmem_default = 212992
net.core.optmem_max = 20480
net.ipv4.tcp_rmem = 4096	131072	6291456
net.ipv4.tcp_wmem = 4096	16384	4194304
#Maximum connections and backlog
net.core.somaxconn = 4096
net.core.netdev_max_backlog = 1000
#TCP tuning options
net.ipv4.tcp_max_syn_backlog = 4096
net.ipv4.tcp_max_tw_buckets = 262144
net.ipv4.tcp_tw_reuse = 2
net.ipv4.tcp_tw_recycle = 1  ### nist
net.ipv4.tcp_fin_timeout = 60
#Don't use slow start on idle TCP connections
net.ipv4.tcp_slow_start_after_idle = 1
```