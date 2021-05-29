# add and remove OSDs from your cluster
- > ## adding host to ceph
```bash
$ sudo ceph orch host add *<hostname>* *<ip>*
```
- > ## check available disks to create osd
```bash
$ sudo ceph orch device ls [--hostname=...] [--wide] [--refresh]
```
- The device must have no partitions.
- The device must not have any LVM state.
- The device must not be mounted.
- The device must not contain a file system.
- The device must not contain a Ceph BlueStore OSD.
- The device must be larger than 5 GB.
- > ## add osd
```bash
$ sudo ceph orch daemon add osd *<host>*:*<device-path>*
```
- > ## remove osd
removing an OSD from a cluster involves two steps:
1. evacuating all placement groups (PGs) from the cluster
2. removing the PG-free OSD from the cluster
```bash
$ sudo ceph orch osd rm <osd_id(s)> [--replace] [--force]
```
### example
```bash
$ sudo ceph orch osd rm 0
```
### expected output
```bash
Scheduled OSD(s) for removal
```
- > ## check your OSDs status by
```bash
$ sudo ceph osd status
```
## and 
```bash
$ sudo sudo ceph orch osd rm status
```
# *** stop OSD removal ***
```bash
$ sudo ceph orch osd rm stop <svc_id(s)>
```
### example
```bash
$ sudo ceph orch osd rm stop 4 
```
## expected output
```bash
Stopped OSD(s) removal
```
# osd info
```bash
$ sudo ceph orch ps
$ sudo ceph osd info
```