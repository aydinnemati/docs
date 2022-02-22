# cephFS
```bash
$ sudo fs set <fs name> max_file_size <size in bytes>
```
> - CephFS has a configurable maximum file size, and it’s 1TB by default. You may wish to set this limit higher if you expect to store large files in CephFS. It is a 64-bit field.
> - Setting max_file_size to 0 does not disable the limit. It would simply limit clients to only creating empty files.

# create file systems
1. 
```bash
$ sudo ceph orch apply -i mds.yml

===Service Spec
service_type: mds
service_id: test-fs
placement:
  count: 3
  hosts:
    - lff-11
    - lff-13
===

```
```bash
$ sudo ceph osd pools create *<fs metadata pool name>*metadata

example:
$ sudo ceph osd pools create test-fs-metadata
```
```bash
$ sudo ceph osd pools create *<fs data pool name>*data

example:
$ sudo ceph osd pools create test-fs-data
```
```bash
$ sudo ceph fs new *< mds server name >* *< fs metadata pool name >* *<fs data pool name>*

example:
$ sudo ceph fs new test-fs test-fs-metadata test-fs-data
```