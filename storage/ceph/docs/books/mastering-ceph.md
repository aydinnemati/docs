# Mastering Ceph second edition
> - 3-5-8-9-11-12

- file store: rocksDB + posix fs
- bluestore: raw block device + rocksDB
> raw block device:
> - in Unix and Unix-like operating systems, a raw device is a special kind of logical device associated with a character device file that allows a storage device such as a hard disk drive to be accessed directly, bypassing the operating system's caches and buffers

# *** **_Tips_** ***
# 3) **BlueStore**
1. A beneficial side
effect of this is that, when using an SSD to hold the journal for a spinning disk, it acts like a
write back cache, lowering the latency of writes to the speed of the SSD; however, if the
filestore journal resides on the same storage device as the data partition, then throughput
will be at least halved.

2. rocksdb metadata tables: All new data is written into the memory-based table and WAL, the memory based table is
known as level 0. BlueStore configures level 0 as 256 MB. The default size multiplier
between levels is a factor of ten, this means that level 1 is also 256 MB, level 2 is 2.56 GB,
level 3 is 25.6 GB, and level 4 would be 256 GB. For most Ceph use cases the average total
metadata size per OSD should be around 20-30GB, with the hot data set typically being less
than this. It would be hoped that levels 0, 1, and 2 would contain most of the hot data for
writes, and so sizing an SSD partition to at least 3 GB should mean that these levels are
stored on SSD

3. metadata disk size: The next challenge is sizing your flash device correctly to ensure that all of the metadata
fits. As mentioned previously, RocksDB compacts data down through the various levels of
the database. When BlueStore creates the files for the RocksDB, it will only place a certain
level on your flash device if the whole of that level would fit in it. Therefore, there are
minimum sizes required for each level to ensure that the level is actually located on flash.
For example, to ensure that the 2.56 GB level 2 part of the DB fits on flash, you need to have
at least a 4-5 GB SSD partition. This is because level 0 and level 1 and level 2 all need to fit,
as well as a small amount of overhead. For level 3 to fit in its entirety, you would need just
over 30 G; any smaller and the extra space over level 2 would not be used. To ensure that
level 4 would fit, you would likely need over 300 GB of flash space.

4. arcitecture: example
- WAL, DB, and data all on spinning disk or flash
- WAL and DB on SSD, data on spinning disk
- WAL on NVMe, DB on SSD, and data on spinning disk

5. Compression
- compression_algorithm
- compression_mode : This controls the operating status of compression on a per-
pool basis. It can be set to either none , passive , aggressive , or force . The
passive setting enables the use of compression, but will only compress objects
that are marked to be compressed from higher levels. The aggressive setting
will try and compress all objects unless explicitly told not to. The force setting
will always try and compress data.
- compress_required_ratio : By default, this is set at 87.5%.
> - An additional advantage of using compression over the reduction in space consumed is
also I/O performance when reading or writing large blocks of data. Because of the data
being compressed, the disks or flash devices will have less data to read or write, meaning
faster response times. Additionally, flash devices will possibly see less write wear because
of the reduced amount of total data written.

6. in BlueStore, RAM has to be statically assigned to the OSD on startup
7. Unlike in filestore, where any free RAM in the OSD node is used by the page cache
8. If your OSD nodes have plenty of free memory after all your OSDs are running and storing
data, then it's possible to increase the amount of memory assigned to each OSD and decide
how it's split between the different caches.

9. Recent versions of Ceph contain a feature in BlueStore that auto-tunes the assignment of
memory between the different caches in BlueStore. By default, the OSD will aim to
consume around 4 GB of memory, and by continually analyzing the memory usage will
adjust the allocation to each cache. The major improvement that auto-tuning brings is that
different workloads utilize the different caches in BlueStore differently, and trying to pre-
allocate memory with static variables is an extremely difficult task.
> - **its not recommanded change to manual-mode**

10. **ceph-volume** is the recommended tool for provisioning Bluestore OSDs.Although ceph-volume can function in a simple mode, the recommended approach is to
use the lvm mode.

11. It's recommended that you
encrypt all new OSDs unless you have a specific reason not to

# 3) **RADOS Pools and Client Access**
1. Two types of pools can be created, replicated, and erasure-coded, offering
different usable capacities, durability, and performance. Replicated RADOS pools are the default pool type in Ceph(replBy default, Ceph will use a replication factor of 3x)
2. As mentioned, the default replication size is 3, with a required minimum size of two
replicas to accept client I/O. Decreasing either of these values is not recommended, and
increasing them will likely have minimal effects on increasing data durability, as the chance
of losing three OSDs that all share the same PG is highly unlikely

3. Ceph will prioritize
the recovery of PGs that have the fewest copies, this further minimizes the risk of data loss,
therefore, increasing the number of replica copies to four is only beneficial when it comes to
improving data availability

4. 4+2 configurations would give you 66% usable capacity and allows for two OSD failures.
This is probably a good configuration for most people to use.
5. At the other end of the scale, 18+2 would give you 90% usable capacity and still allow for
two OSD failures. On the surface, this sounds like an ideal option, but the greater total
number of shards comes at a cost. A greater number of total shards has a negative impact
on performance and also an increased CPU demand. The same 4 MB object that would be
stored as a whole single object in a replicated pool would now be split into 20 x 200-KB
chunks, which have to be tracked and written to 20 different OSDs. Spinning disks will
exhibit faster bandwidth, measured in MBps with larger I/O sizes, but bandwidth
drastically tails off at smaller I/O sizes. These smaller shards will generate a large amount
of small I/O and cause an additional load on some clusters.
6. it's important not to forget that these shards need to be spread across different hosts
according to the CRUSH map rules: no shard belonging to the same object can be stored on
the same host as another shard from the same object. Some clusters may not have a
sufficient number of hosts to satisfy this requirement. If a CRUSH rule cannot be satisfied,
the PGs will not become active, and any I/O destined for these PGs will be halted, so it's
important to understand the impact on a cluster's health of making CRUSH modifications.

7. The default erasure plugin in Ceph is the jerasure plugin
- different techniques that can be used to calculate the erasure codes:
> - reed_sol_van : The default technique, complete flexibility on number of k+m
shards, also the slowest.
> - reed_sol_r6_op : Optimized version of default technique for use cases where
m=2. Although it is much faster than the unoptimized version, it's not as fast as other versions. However, the number of k shards is flexible.
> - cauchy_orig : Better than the default, but it's better to use cauchy_good
> - cauchy_good : Middle-of-the-road performance while maintaining full flexibility of the shard configuration.
> - liberation : Total number of shards must be equal to a prime number and m=2 so 3+2, 5+2, or 9+2 are all good candidates, excellent performance.
> - liber8tion : Total number of shards must be equal to 8 and m=2, only 6+2 is possible, but excellent performance.
> - blaum_roth : Total number of shards must be one less than a prime number and m=2, so the ideal is 4+2, excellent performance.

8. 
> K
> - the number of data chunks, i.e. the number of chunks in which the original object is divided. For instance if K = 2 a 10KB object will be divided into K objects of 5KB each.

> M
> - the number of coding chunks, i.e. the number of additional chunks computed by the encoding functions. If there are 2 coding chunks, it means 2 OSDs can be out without losing data.

9. **Although erasure-coded pool support has been in Ceph for several releases now, before the arrival of BlueStore in the Luminous release, it had not supported partial writes. This limitation meant that erasure pools could not directly be used with RBD and CephFS workloads. With the introduction of BlueStore in Luminous, it provided the groundwork for partial write support to be implemented. With partial write support, the number of I/O types that erasure pools can support almost matches replicated pools, enabling the use of erasure-coded pools directly with RBD and CephFS workloads. This dramatically lowers the cost of storage capacity for these use cases.**

# 5) Ceph RADOS Pools and Client Access

1. There is a fast read option that can be enabled on erasure pools, which allows
the primary OSD to reconstruct the data from erasure shards if they return quicker than
data shards. This can help to lower average latency at the cost of a slightly higher CPU
usage.
2. Algorithms and profiles: see every option to identify which technique best suits your workload. chapter 5 page 132 mastering ceph
3. The MDS currently runs as a single-threaded
process and so it is recommended that the MDS is run on hardware with the highest-
clocked CPU as possible.
4. in larger deployments, a single
MDS could possibly start to become a limitation, especially due to the single-threaded
limitation of MDSes. It should be noted that multiple active MDSes are purely for increased performance and do not provide any failover or high availability themselves; therefore, sufficient standby MDSes should always be provisioned
5. The index pools helps with the listing of bucket contents and so placing
the index pool on SSDs is highly recommended.
6. RGW: only the data pool should be placed on erasure-coded pools.

# 8) Monitoring Ceph
1. If your Ceph cluster fills up, it
will stop accepting I/O requests and will not be able to recover from future OSD failures.
2. We will build this monitoring infrastructure on one of our monitor nodes in our test cluster.
In a production cluster, it is highly recommended that it gets its own dedicated server.

# Tuning Ceph