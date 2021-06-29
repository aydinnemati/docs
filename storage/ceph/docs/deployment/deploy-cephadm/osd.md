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
$ sudo ceph osd df
$ sudo ceph osd tree
$ sudo ceph osd dump
```

# to build pool on specific osds 
- can use device classes and crush rules
- for example want to create pool on hdd o ssd osds can use this

See [suse.com](https://www.suse.com/support/kb/doc/?id=000019699)
# assign class to OSDs
## see OSDs classes
```bash
$ sudo ceph osd tree
```
## change class for an OSD
- first should remove class for that OSD
```bash
$ sudo ceph osd crush rm-device-class <osd-name> [...]
```
- then can assign a new class to it
```bash
$ sudo ceph osd crush set-device-class <class> <osd-name> [...]
```
# crush rules
- you can see what rules are defined for your cluster
```bash
$ sudo ceph osd crush rule ls
```
- you can view the contents of the rules
```bash
$ sudo ceph osd crush rule dump
```
## create rules
```bash
$ sudo ceph osd crush rule create-replicated <rule-name> <root> <failure-domain> <class>
```
- example
```bash
$ sudo ceph osd crush rule create-replicated replicated_hdd default host hdd
```
# tell pools to use new crush rule
```bash
$ sudo ceph osd pool set <pool-name> crush_rule <rule-name>
```