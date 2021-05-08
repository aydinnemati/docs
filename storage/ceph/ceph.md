> # __Ceph__
- implements object storage
- 3 in 1 interface to object-, file- and block- level storage
- replicates data
-  makes system fault-telorant (in case of failior of some components stil goes on) using commodity hardware(uses large number of components to work paralel to continue opration in case of failior of some of it components)
-  disaster recovery and data redundancy through replication and erasure coding (EC is a method of data protection in which data is broken into fragments), snapshots and storage cloning
- self-healing and self-managing aiming to minimize administration time

> # __Docs__
- See [Intro to Ceph](https://docs.ceph.com/en/latest/start/intro/)

> ## begin with setting up
- Ceph Monitor
- Ceph Manager
- Ceph OSD (Object Storage Daemon)



## __Monitors__
> A Ceph Monitor (*__ceph-mon__*) maintains maps of the cluster state, including the monitor map, manager map, the OSD map, the MDS map, and the CRUSH map. These maps are critical cluster state required for Ceph daemons to coordinate with each other. Monitors are also responsible for managing authentication between daemons and clients. *__At least three monitors are normally required for redundancy and high availability__*.

## __Managers__
> A Ceph Manager daemon (*__ceph-mgr__*) is responsible for keeping track of runtime metrics and the current state of the Ceph cluster, including storage utilization, current performance metrics, and system load. The Ceph Manager daemons also host python-based modules to manage and expose Ceph cluster information, including a web-based Ceph Dashboard and REST API. *__At least two managers are normally required for high availability__*.

## __Ceph OSDs__
> A Ceph OSD (object storage daemon, *__ceph-osd__*) stores data, handles data replication, recovery, rebalancing, and provides some monitoring information to Ceph Monitors and Managers by checking other Ceph OSD Daemons for a heartbeat.*__At least 3 Ceph OSDs are normally required for redundancy and high availability__*.

## __MDSs__
> A Ceph Metadata Server (MDS, *__ceph-mds__*) stores metadata on behalf of the Ceph File System (i.e., Ceph Block Devices and Ceph Object Storage do not use MDS). Ceph Metadata Servers allow POSIX file system users to execute basic commands (like ls, find, etc.) without placing an enormous burden on the Ceph Storage Cluster.

# Hardware Recommendations
See [Recommendations](https://docs.ceph.com/en/latest/start/hardware-recommendations/)

# *__AVOID RAID__* 
> __if you have raid controller 
come with raid 0 for all disks__