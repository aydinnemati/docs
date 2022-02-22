# mount ceph fs using fuse
see [redhat](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/2/html/ceph_file_system_guide_technology_preview/mounting_and_unmounting_ceph_file_systems)

# ceph file system
## volume
- data pool
- metadata pool
## volume cmd
```bash
$ sudo ceph fs new <fs_name> <metadata> <data>
$ sudo ceph fs volume create <fs name> # also it makes 2 pools for it too
$ sudo ceph fs volume ls
$ sudo ceph osd pool ls
$ sudo ceph osd pool create <pool name>
$ sudo ceph mds stat
```
> **let's mount it**
# Mount CephFS using FUSE
## install ceph-fuse using apt
```bash
$ sudo apt install ceph-fuse
```
## mount volume
```bash
$ sudo ceph-fuse -n client.admin -k /path/to/keyring -m <mon-ip>:6789 /path/to/mount # default port of monitor
```
## unmount volume
```bash
$ sudo umount /path/to/unmount
```
## Persistent Mounts
To mount CephFS as a file system in user space, add the following to /etc/fstab
```bash
#DEVICE PATH       TYPE      OPTIONS
none    /mnt/mycephfs  fuse.ceph ceph.id={user-ID}[,ceph.conf={path/to/conf.conf}],_netdev,defaults  0 0
```
then 
```bash
$ sudo systemctl start ceph-fuse@/mnt/mycephfs.service
$ sudo systemctl enable ceph-fuse.target
$ sudo systemctl enable ceph-fuse@-mnt-mycephfs.service
```

# mount cephFS on server
- for mounting ceph-fs on a server, should have a user with keyring on that server and run command below:
```bash
$ sudo ceph-fuse -n user -k /path/to/keyring/file  -m <mon-ip>:6789 /mount/point
```
## example
```bash
$ sudo ceph-fuse -n client.admin -k /etc/ceph/ceph.client.admin.keyring -m 192.168.xxx.xxx:6789 /data
```
## # **you can mount a fs volume on sevral servers** \#


# If you are using BlueStore, the file structure of the OSD is no longer viewable by default. However, you can use the following command on a stopped OSD to mount the BlueStore OSD as a Linux filesystem.
```bash
$ sudo ceph-objectstore-tool --op fuse --data-path /var/lib/ceph/osd/ceph-0 --
mountpoint /mnt
```