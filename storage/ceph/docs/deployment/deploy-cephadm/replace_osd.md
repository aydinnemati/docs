# replace osd disk 
see [redhat](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/2/html/administration_guide/changing_an_osd_drive)
- The general procedure for replacing an OSD involves removing the OSD from your Ceph cluster, replacing the drive and then re-creating the OSD
# Handling a disk failure
- install ceph-osd
```bash
$ sudo apt install ceph-osd
```
## **replaced OSD’s id and CRUSH map entry need to be keep intact after the OSD is destroyed for replacement**
- See [redhat](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html/operations_guide/handling-a-disk-failure)

# Replacing OSD
- 1. make sure it is safe to destroy the OSD
```bash
$ while ! ceph osd safe-to-destroy osd.{id} ; do sleep 10 ; done
```
- 2. destroy the OSD first
```bash
$ sudo ceph osd destroy {id} --yes-i-really-mean-it
```
- 3. zap a disk for the new OSD, if the disk was used before for other purposes. It’s not necessary for a new disk
```bash
$ sudo ceph-volume lvm zap /dev/sdX
```
- 4. prepare the disk for replacement by using the previously destroyed OSD id
```bash
$ sudo ceph-volume lvm prepare --osd-id {id} --data /dev/sdX
```
- 5. activate the OSD
```bash
$ sudo ceph-volume lvm activate {id} {fsid}
```
> Alternatively, instead of preparing and activating, the device can be recreated in one call, like
> ```bash
> $ sudo ceph-volume lvm create --osd-id {id} --data /dev/sdX
> ```