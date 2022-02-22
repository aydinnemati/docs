# *** ( **Options** ) *** ((read about))
- mon_osd_cache_size
- rocksdb_cache_size
- mds_cache_memory
- osd_memory_target

# *** ( **Best Practice** ) ***
- at least 3 mons & 2 managers
- increase number of disks not size of them
- recommend 1 TB disks and each osd on a disk
- dictate that you should run **operating systems**, **OSD data** and **OSD journals** on separate drives
- > recommanded to use SSDs to OSD journals but befor that should test these first: 
> ### Write-intensive semantics
> - Journaling involves write-intensive semantics, so you should ensure that the SSD you choose to deploy will perform equal to or better than a hard disk drive when writing data. Inexpensive SSDs may introduce write latency even as they accelerate access time, because sometimes high performance hard drives can write as fast or faster than some of the more economical SSDs available on the market!
> ### Sequential Writes
> - When you store multiple journals on an SSD you must consider the sequential write limitations of the SSD too, since they may be handling requests to write to multiple OSD journals simultaneously.
> ### Partition Alignment
> - A common problem with SSD performance is that people like to partition drives as a best practice, but they often overlook proper partition alignment with SSDs, which can cause SSDs to transfer data much more slowly. Ensure that SSD partitions are properly aligned.
- HDD OSDs may see a significant performance improvement by offloading WAL+DB(Write-ahead logging: In computer science, write-ahead logging is a family of techniques for providing atomicity and durability in database systems.) onto an SSD
- seperate cephFS metdadata with cephFS content files(you can create a CRUSH hierarchy map for your metadata pool pointing to SSD disk of host)
- check raid controller or HBA throughput for bottle neck.
- its better to use disk controller in it-mode(leave disks to manage with OS - ir-mode is raid functionality)[The Ceph blog is often an excellent source of information on Ceph performance issues. See Ceph Write Throughput 1 and Ceph Write Throughput 2 for additional details.]
- if running multiple osd on a host should check if agregations of cluster dont exeed network bandwidth
- start with at least 10 GB/s networking in your racks
- consider time for recovering and replications in case of failure hard disks
- use seperated volume from os
- **use bluestore**
- best way to deploy is cephadm because is ceph-ansible newer management features and dashboard integration are not available and ceph-deploy is not develope any more so dont use it
- data replication is soooooooooo important so consider it when designing your cluster
- 