
# Hardware Recommendations
## CPU 
> ### CephFS metadata
> - CPU intensive
> - quad core or better
> - benefit from higher clock rate

> ### osd
> - Requirements vary by use-case; a starting point might be one core per OSD for light / archival usage, and two cores per OSD for heavy workloads such as RBD volumes attached to VMs. 

> ### monitors and managers
> - do not have heavy CPU demands so a modest processor can be chosen for them
## RAM
> - 8GB per BlueStore OSD is advised
> - **You may also want to consider tuning settings like mon_osd_cache_size or rocksdb_cache_size after careful research**

## Data Storage
> - Plan your data storage configuration carefully
> - Simultaneous OS operations, and simultaneous request for read and write operations from multiple daemons against a single drive can slow performance considerably
> - recommended to increase number of disks not size of them
> - recommend 1 TB disks and each osd on a disk
> - *** Ceph must write to the journal before it can ACK the write. _**Ceph best practices dictate that you should run operating systems, OSD data and OSD journals on separate drives.**_ ***