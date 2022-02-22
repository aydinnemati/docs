# CEPH Documentation
See [ceph.io](https://docs.ceph.com/en/latest/)
also See [ceph blog](https://ceph.com/community/blog/)

## simple deploy
> at least requires a monitor, a manager and an osd node.
> also needs meta data server when using ceph fs.
> 

> ## Monitors
- A Ceph Monitor (ceph-mon) maintains maps of the cluster state, including the monitor map, manager map, the OSD map, the MDS map, and the CRUSH map. These maps are critical cluster state required for Ceph daemons to coordinate with each other. Monitors are also responsible for managing authentication between daemons and clients. At least three monitors are normally required for redundancy and high availability.
- **maps of cluster**
- **authenticate**
- **coordinate nodes together**
- **at least 3 nodes**

> ## Managers
- A Ceph Manager daemon (ceph-mgr) is responsible for keeping track of runtime metrics and the current state of the Ceph cluster, including storage utilization, current performance metrics, and system load. The Ceph Manager daemons also host python-based modules to manage and expose Ceph cluster information, including a web-based Ceph Dashboard and REST API. At least two managers are normally required for high availability.
- **keeps current state of cluster**
- **expose metrics to ceph monitor**
- **manage using storage**
- **web-base dashboared and RESTapi**
- **at least 2 nodes**
# CEPH Documentation
See [ceph.io](https://docs.ceph.com/en/latest/)
also See [ceph blog](https://ceph.com/community/blog/)

## simple deploy
> at least requires a monitor, a manager and an osd node.
> also needs meta data server when using ceph fs.
> 

> ## Monitors
- A Ceph Monitor (ceph-mon) maintains maps of the cluster state, including the monitor map, manager map, the OSD map, the MDS map, and the CRUSH map. These maps are critical cluster state required for Ceph daemons to coordinate with # CEPH Documentation
See [ceph.io](https://docs.ceph.com/en/latest/)
also See [ceph blog](https://ceph.com/community/blog/)

## simple deploy
> at least requires a monitor, a manager and an osd node.
> also needs meta data server when using ceph fs.
> 

> ## Monitors
- A Ceph Monitor (ceph-mon) maintains maps of the cluster state, including the monitor map, manager map, the OSD map, the MDS map, and the CRUSH map. These maps are critical cluster state required for Ceph daemons to coordinate with each other. Monitors are also responsible for managing authentication between daemons and clients. At least three monitors are normally required for redundancy and high availability.
- **maps of cluster**
- **authenticate**
- **coordinate nodes together**
- **at least 3 nodes**

> ## Managers
- A Ceph Manager daemon (ceph-mgr) is responsible for keeping track of runtime metrics and the current state of the Ceph cluster, including storage utilization, current performance metrics, and system load. The Ceph Manager daemons also hoster**
- **authenticate**
- **coordinate nodes together**
- **at least 3 nodes**

> ## Managers
- A Ceph Manager daemon (ceph-mgr) is responsible for keeping track of runtime metrics and the current state of the Ceph cluster, including storage utilization, current performance metrics, and system load. The Ceph Manager daemons also hosovery, rebalancing, and provides some monitoring information to Ceph Monitors and Managers by checking other Ceph OSD Daemons for a heartbeat. At least 3 Ceph OSDs are normally required for redundancy and high availability.
- **stores data**
- **replication, recovery, rebalancing**
- **some monitoring info to ceph monitor**
- **check other osd for heart beat**
- **at least 3 nodes**

> ## MDSs
- A Ceph Metadata Server (MDS, ceph-mds) stores metadata on behalf of the Ceph File System (i.e., Ceph Block Devices and Ceph Object Storage do not use MDS). Ceph Metadata Servers allow POSIX file system users to execute basic commands (like ls, find, etc.) without placing an enormous burden on the Ceph Storage Cluster.
- **when using cephFS its needed**
- **stores metadata of cephFS**
- **allows POSIX FS users to use commands like _ls_,  _find_ and etc.**

> ## Ceph RGW
- Object Gateway / Rados Gateway 
- RESTful API interface compatible with Amazon S3 , OpenStack Swift 

## Ceph RBD
- Raw Block Device 
- Provides Block Storage to VM / bare metal as well as regular clients , supports OpenStack and CloudStack . Includes Enterprise features like snapshot , thin provisioning , compression

## CRUSH (Controlled Replication Un- der Scalable Hashing)
- ceph stores data using CRUSH algorithm
- The CRUSH algorithm enables the Ceph Storage Cluster to scale, rebalance, and recover dynamically.
