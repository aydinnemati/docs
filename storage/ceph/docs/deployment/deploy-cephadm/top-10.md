# 10 Commands Every Ceph Administrator Should Know

1. Check or watch cluster health: ceph status
```bash
$ sudo ceph -w
$ sudo ceph -s
```
2. Check cluster usage stats
```bash
$ sudo ceph df
```
3. Check placement group stats
```bash
$ sudo ceph pg dump
```
4. View the CRUSH map
```bash
$ sudo ceph osd tree
```
5. Create or remove OSDs
```bash
$ sudo ceph osd create 
$ sudo ceph osd rm
```
6. Create or delete a storage pool 
```bash
$ sudo ceph osd pool create
$ sudo ceph osd pool delete
```
7. Repair an OSD
```bash
$ sudo ceph osd repair
```
8. Benchmark an OSD
```bash
$ sudo ceph tell osd.* bench
```
9. Adjust an OSD’s crush weight
```bash
$ sudo ceph osd crush reweight
```
10.  List cluster keys
```bash
$ sudo ceph auth list
```