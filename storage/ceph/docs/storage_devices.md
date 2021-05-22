# Storage Devices
See [=>](https://docs.ceph.com/en/latest/rados/configuration/storage-devices/)

## There are two Ceph daemons that store data on devices:
- > Ceph OSDs (or Object Storage Daemons)
  > - stores data

-   > Ceph Monitor daemons
    > - critical cluster state
    > - take care of membership and authenticate

## There are two ways that OSDs can manage the data they store
- bluestore(powerfully recommanded)
- filestore(well tested but suffers from low performance)

> ### bluestore
> #### Direct management of storage devices
> - no additional abstraction layer

> #### Metadata management with RocksDB
> - key/value mapping metadata to data location with rockdb

> #### Full data and metadata checksumming
> - one or more verifications on data

> #### Inline compression
> - optionally can compress data befor write to disk

> #### Multi-device metadata tiering
> - BlueStore allows its internal journal (write-ahead log) to be written to a separate, high-speed device (like an SSD, NVMe, or NVDIMM) to increased performance. If a significant amount of faster storage is available, internal metadata can also be stored on the faster device.

> #### Efficient copy-on-write
> - RBD and CephFS snapshots rely on a copy-on-write clone mechanism that is implemented efficiently in BlueStore. This results in efficient IO both for regular snapshots and for erasure coded pools (which rely on cloning to implement efficient two-phase commits)

