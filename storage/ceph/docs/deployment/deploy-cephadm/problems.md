# Problems we have
> ## down time
> - 1. turn on and off bare metals with maas goes wrong

> ## down time
> - 2. disks that replaced shuold re-build raid or re-enabled with intelgent provisioning tool of hpe

## DNS
- 3. 10.0.23.200 10-0-23-0--24.maas-internal cant resolve

## fiber cables
- cant PXE boot on it

## ceph GPG key for updating
```
Err:5 https://download.ceph.com/debian-octopus focal InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY E84AC2C0460F3994
```
## when maas is off
```
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/focal-security/InRelease  Unable to connect to 10-0-23-0--24.maas-internal:8000:
```

## witch osd disk is in witch bay???
- we dont know witch disk of osd is witch actual disk in server!!!