# Configuring Metadata Server Daemons
- See [RedHat](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html/ceph_file_system_guide/configuring-metadata-server-daemons)

## number of active mds daemons
```bash
$ sudo ceph fs set <name> max_mds <number>
```