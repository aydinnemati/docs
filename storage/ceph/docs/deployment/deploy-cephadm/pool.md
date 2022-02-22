# create pools
```bash
$ sudo ceph osd pool create {pool-name} [{pg-num} [{pgp-num}]] [replicated] [crush-rule-name] [expected-num-objects]
$ sudo ceph osd pool create {pool-name} [{pg-num} [{pgp-num}]]   erasure [erasure-code-profile] [crush-rule-name] [expected_num_objects] [--autoscale-mode=<on,off,warn>]
```
See [computingforgeeks.com](https://computingforgeeks.com/create-a-pool-in-ceph-storage-cluster/)
See [ceph.com](https://docs.ceph.com/en/latest/rados/operations/pools/)

## pool details
```bash
$ sudo ceph df [detail]
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
# get pool crush rule
```bash
$ sudo ceph osd pool get {pool-name} crush_rule
```