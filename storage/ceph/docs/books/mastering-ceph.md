# Mastering Ceph second edition
> - 3-5-8-9-11-12

- file store: rocksDB + posix fs
- bluestore: raw block device + rocksDB
> raw block device:
> - in Unix and Unix-like operating systems, a raw device is a special kind of logical device associated with a character device file that allows a storage device such as a hard disk drive to be accessed directly, bypassing the operating system's caches and buffers

# *** **_Tips_** ***
# **BlueStore**
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
