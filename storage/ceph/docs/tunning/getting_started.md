# ceph tunning - chapter 9 - mastering ceph book(nick fisk - 2019)

# *** **Latency** ***
- page 219
1. use SSD disks for WAL(Bluestore)
2. at least 10G network

# measuring latency
1. Client to Primary OSD
- network(ping, iperf)
> NETWORK

2. Primary OSD to Replica OSD(s)
- it is affected by the speed of the CPU. A faster CPU with a higher frequency will run through the code path faster, reducing latency.
> CPU
- There is also an extra network hop between the primary and the replicated OSDs, which
introduces latency into each request.
> NETWORK

3. Primary OSD to Client
> NETWORK

> # TARGET
> - Overall, in a well-designed and well-tuned Ceph cluster, all of these parts combined should allow an average write 4 KB request to be serviced in around **500-750 microseconds**

# OS tunning
## CPU
### EXAMPLE
- Here is a list from an Intel E3-1200v5 CPU; older CPUs may fare slightly worse:
```
POLL = 0 microsecond
C1-SKL = 2 microseconds
C1E-SKL = 10 microseconds
C3-SKL = 70 microseconds
C6-SKL = 85 microseconds
C7s-SKL = 124 microseconds
C8-SKL = 200 microseconds
```
1) To leak less time to wake cpu up from sleep (C-state) force Linux to only drop-down to the C1 C-state, add this to your GRUB configuration:
```bash
intel_idle.max_cstate=1
```
```text
Some Linux distributions have a performance mode where this runs the CPUs at a
maximum frequency. However, the manual way to achieve this is to echo values via sysfs .
Sticking the following in /etc/rc.local will set all your cores to run at their maximum
frequency on the boot:

$ /sys/devices/system/cpu/intel_pstate/min_perf_pct

After you restart your OSD node, these changes should be in effect. Confirm this by
running these commands:

$ sudo cpupower monitor

As mentioned earlier in this chapter, before making these changes, run a reference
benchmark, and then do it again afterward so that you can understand the gains made by
this change.
```

## RAM
- The latest versions of Ceph contain an auto-tuning functionality for BlueStore OSDs. The
auto-tuning works by analyzing the cache utilization of the OSDs and adjusting the caching
thresholds for the OSD, RocksDB, and data caches, depending on the current hit rate. It also
limits the sum of these caches to try to limit the total OSD memory usage to the limit set by
the osd_memory_target variable, which is set to 4 GB by default.

- Obviously, if you have less RAM in the Ceph node and therefore it unable to provide 4 GB
for each OSD, this figure would need to be reduced to avoid the node running out of
memory. However, if the Ceph node has sufficient memory, it would be recommended to
increase the osd_memory_target variable to allow Ceph to make as much use of the
installed memory as possible. Once enough RAM has been assigned to the OSD and
RocksDB, any additional RAM will be used as a data cache and will help to service the top-
percentile read IOs much more effectively. The current auto-tuning algorithm is fairly slow
and takes a while to ramp up, so at least 24-48 hours should be given to see the full effect of
a change to the osd_memory_target variable.

## WAL deferred writes
- BlueStore can journal writes in the RocksDB WAL and flush them at a later date, allowing
for write coalescing and ordering. This can bring large performance improvements for
clusters that use spinning disks with flash-based devices for RocksDB.
By default, if the OSD is identified as a spinning HDD, writes less or equal to 32 KB are
written into the WAL of the OSD and are then acknowledged and sent back to the client.
This is controlled by the bluestore_prefer_deferred_size_hdd variable; this value
can be adjusted if it is determined that your workload would benefit from also
deferring larger writes via the WAL to achieve lower latency and higher IOPS. Thought
should also be given to the write load of the flash device holding the WAL, both for
bandwidth and endurance reasons.

- The BlueStore configuration also limits how many writes can be queued up before the OSD
is forced to flush them down to the disk; this can be controlled via the
bluestore_deferred_batch_ops variable and is set by default to 64 . Increasing this
value may increase total throughput, but also runs the risk of the HDD spending large
amounts of time being saturated and raising the average latency.

## Scrubbing
- Scrubbing is Ceph's way of verifying that the objects stored in RADOS are consistent, and to protect against bit rot or other corruptions. Scrubbing can either be normal or deep, depending on the set schedule. During a normal scrub operation, Ceph reads all objects for a certain PG and compares the copies to make sure that their size and attributes match.

- A deep scrub operation goes one step further and compares the actual data contents of the objects. This generates a lot more I/O than the simpler standard scrubbing routine. Normal scrubbing is carried out daily, whereas deep scrubbing should be carried out weekly due to the extra I/O load.

- Despite being deprioritized, scrubbing does have an impact on client IO, and so, there are a number of OSD settings that can be tweaked to guide Ceph as to when it should carry out the scrubbing.

- The osd _scrub_begin_hour and osd _scrub_end_hour OSD configuration options
determine the window Ceph will try to schedule scrubs in. By default, these are set to allow scrubbing to occur throughout a 24-hour period. If your workload only runs during the day, you might want to adjust the scrub start and end times to tell Ceph that you want it to scrub during off-peak times only. The osd_scrub_sleep configuration option controls the amount of time in seconds that a scrub operation waits between each chunk—this can help to allow the client IO to be serviced in-between the reading of each object. The chunk size is determined by the two variables osd_scrub_chunk_min and osd_scrub_chunk_max .

- It should be noted that this time, a window is only honored if the PG has not fallen outside its maximum scrub interval. If it has, it will be scrubbed, regardless of the time window settings. The default maximum intervals for both normal and deep scrubs are set to one week.

## OP (operation) priorities
- Ceph has the ability to prioritize certain operations over others, with the idea that the client I/Os should have precedence over the recovery, scrubbing, and snapshot trimming IO. These priorities are controlled by the following configuration options:
```bash
osd client op priority
osd recovery op priority
osd scrub priority
osd snap trim priority
```
- Here, the higher the value, the higher priority. The default values work fairly well, and there shouldn't be much requirement to change them. But there can be some benefit in
lowering the priority of scrub and recovery operations to limit their impact on the client I/O. It's important to understand that Ceph can only prioritize the I/O in the sections of the I/O path that it controls. Therefore, tuning the disk queue lengths in the previous section may be needed to get the maximum benefits.

# Network
- The network is a core component of a Ceph cluster, and its performance will greatly affect the overall performance of the cluster. 10 GB should be treated as a minimum; 1 GB
networking will not provide the required latency for a high performance Ceph cluster.
There are a number of tunings that can help to improve network performance which is
done by decreasing latency and increasing throughput.

- The first thing to consider if you wish to use jumbo frames is using an MTU of 9,000 instead
of 1,500; each I/O request can be sent using fewer Ethernet frames. As each Ethernet frame
has a small overhead, increasing the maximum Ethernet frame to 9,000 can help. In
practice, gains are normally less than 5% and should be weighed against the disadvantages
of having to make sure every device is configured correctly.
The following network options set in your sysctl.conf file are recommended to
maximize network performance:

```bash
#Network buffers
net.core.rmem_max = 56623104
net.core.wmem_max = 56623104
net.core.rmem_default = 56623104
net.core.wmem_default = 56623104
net.core.optmem_max = 40960
net.ipv4.tcp_rmem = 4096 87380 56623104
net.ipv4.tcp_wmem = 4096 65536 56623104
#Maximum connections and backlog
net.core.somaxconn = 1024
net.core.netdev_max_backlog = 50000
#TCP tuning options
net.ipv4.tcp_max_syn_backlog = 30000
net.ipv4.tcp_max_tw_buckets = 2000000
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_fin_timeout = 10
#Don't use slow start on idle TCP connections
net.ipv4.tcp_slow_start_after_idle = 0
```
# General system tuning
- There are a number of general system parameters that are recommended to be tuned to best suit Ceph's performance requirements. The following settings can be added to your
/etc/sysctl.conf file.

- Make sure that the system has sufficient memory free at all times:
```bash
vm/min_free_kbytes = 524288
```
- Increase the maximum number of allowed processes:
```bash
kernel.pid_max=4194303
```
- Use the following to set the maximum number of file handles:
```bash
fs.file-max=26234859
```


# Tuning CephFS
- Metadata performance is determined by two factors: the speed of reading/writing metadata via the RADOS metadata pool, and the speed at which the MDS can handle client requests. First, make sure that the metadata pool is residing on flash storage, as this will reduce the latency of metadata requests by at least and order of magnitude, if not more. However, as was discussed earlier in the Latency section of this chapter, the latency introduced by a distributed network-storage platform can also have an impact on metadata performance.

- To work around some of this latency, the MDS has the concept of a local cache to serve hot metadata requests from. By default, an MDS reserves 1 GB of RAM to use as a cache and, generally speaking, the more ram you can allocate, the better. The reservation is controlled by the mds_cache_memory_limit variable. By increasing the amount of memory the MDS can use as a cache, the number of requests having to go to the RADOS pool are reduced, and the locality of the RAM will reduce metadata access latency.

- There will come a point when adding additional RAM brings very little benefit. This may
either be due to the cache being sufficiently sized that the majority of requests are being served from cache, or that the number of requests the actual MDS can handle has been reached.

- Regarding the later point, the MDS process is single-threaded and so there will come a
point where the number of metadata requests is causing an MDS to consume 100% of a single CPU core and no additional caching or SSDs will help. The current recommendations
are to try and run the MDS on a high clocked CPU as possible. The quad core Xeon E3s are
ideal for this use and can often be obtained with frequencies nearing 4 GHz for a reasonable price. Compared to some of the lower-clocked Xeon CPUs, often with high core counts, the performance gain could almost be double by ensuring a fast CPU is used.

- If you have purchased the fastest CPU possible and are finding that a single MDS process is still the bottleneck, the last option should be to start deploying multiple active MDSes, so that the metadata requests are sharded across multiple MDSes.

# PG distributions
- While not strictly a performance-tuning option, ensuring even PG distribution across your Ceph cluster is an essential task that should be undertaken during the early stages of the deployment of your cluster. As Ceph uses CRUSH to pseudo-randomly determine where to place data, it will not always balance PG equally across every OSD. A Ceph cluster that is not balanced will be unable to take full advantage of the raw capacity, as the most oversubscribed OSD will effectively become the limit to the capacity.

- An unevenly balanced cluster will mean that a higher number of requests will be targeted at the OSDs holding the most PGs. These OSDs will then place an artificial performance ceiling on the cluster, especially if the cluster is composed of spinning-disk OSDs.

- To rebalance PGs across a Ceph cluster, you simply have to reweight the OSD so that
CRUSH adjusts how many PGs will be stored on it. It's important to note that, by default,
the weight of every OSD is 1, and you cannot weight an underutilized OSD above 1 to
increase its utilization. The only option is to decrease the reweight value of over-utilized OSDs, which should move PGs to the less-utilized OSDs.

- It is also important to understand that there is a difference between the CRUSH weight of an OSD and the reweight value. The reweight value is used as an override to correct the misplacement from the CRUSH algorithm. The reweight command only affects the OSD
and will not affect the weight of the bucket (for example, host) that it is a member of. It is also reset to 1.0 on restart of the OSD. While this can be frustrating, it's  important to understand that any future modification to the cluster, be it increasing the number of PGs or adding additional OSDs, would have likely made any reweight value incorrect. Therefore, reweighting OSDs should not be looked at as a one-time operation, but something that is being continuously done and will adjust to the changes in the cluster.

- To reweight an OSD, use this simple command:
```bash
Ceph osd reweight <osd number> <weight value 0.0-1.0>
```
- Once executed, Ceph will start backfilling to move PGs to their newly-assigned OSDs.
- Of course, searching through all your OSDs and trying to find the OSD that needs
weighting and then running this command for every one would be a very lengthy process.
Luckily, there is another Ceph tool that can automate a large part of this process:
```bash
ceph osd reweight-by-utilization <threshold> <max change> <number of OSDs>
```
- This command will compare all the OSDs in your cluster and change the override
weighting of the top N OSDs, where N is controlled by the last parameter, which is over the threshold value. You can also limit the maximum change applied to each OSD by
specifying the second parameter: 0.05 or 5% is normally a recommended figure.

- There is also a test-reweight-by-utilization command, which will allow you to see
what the command will do before running it.

- While this command is safe to use, there are a number of things that should be taken into
consideration before running it:
1. It has no concept of different pools on different OSDs. If, for example, you have
an SSD tier and an HDD tier, the reweight-by-utilization command will
still try to balance data across all OSDs. If your SSD tier is not as full as the HDD
tier, the command will not work as expected. If you wish to balance OSDs
confined to a single bucket, look into the script version of this command that was
created by CERN.
2. It is possible to reweight the cluster to the point that CRUSH is unable to
determine placement for some PGs. If recovery halts and one or more PGs are left
in a remapped state, this is likely what happened. Simply increase or reset the
reweight values to fix it.

- Once you are confident with the operation of the command, it is possible to schedule it via cron so that your cluster is kept in a more balanced state automatically.

- Since the Luminous release, a new manager module has been included, called Ceph
balancer. This new module works continuously in the background to optimize PG
distribution and ensure that the maximum amount of capacity is available on your Ceph
cluster.

- The Ceph balancer module can use one of two methods to balance data distribution. The
first is crush-compat; this method uses an additional weight field to adjust the weights of each OSD. The main benefit of crush-compat is that it's backward-compatible with older
clients. The other method is called upmap; upmap can achieve much more fine-grained PG
mapping than is possible with crush-compat as it uses new capabilities in the OSD map to
influence PG mapping. The downside is that due to these new capabilities, Ceph clients
need to be running Luminous or a newer release.

- To enable ceph balancer, simply run these two commands:
```bash
ceph mgr module enable balancer
ceph balancer on
```
- You will see Ceph start to backfill as PGs are remapped to new OSDs to balance out the
space utilization; this will continue to occur until the Ceph balancer has reduced deviation of OSD utilization.

