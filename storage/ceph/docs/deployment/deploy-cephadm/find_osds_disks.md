# finding disks related to osds
See [ubuntu.com](https://ubuntu.com/ceph/docs/replacing-osd-disks)

```bash
$ sudo pvs
```
```bash
$ sudo lsblk -i -o NAME,FSTYPE
```