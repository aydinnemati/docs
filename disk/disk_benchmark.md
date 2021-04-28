# Disk
### #
- sequential  r/w
- random  r/w
- throughput
- iops

# DD
- See [->](https://www.geeksforgeeks.org/dd-command-linux/)
- To backup the entire harddisk 
- To backup a Partition
- To create an image of a Hard Disk 
- To restore using the Hard Disk Image
- To create CDROM Backup
- more...

## Linux and Unix Test Disk I/O Performance With dd Command
- See [cyberciti](https://www.cyberciti.biz/faq/howto-linux-unix-test-disk-performance-with-dd-command/)

### sequential I/O performance test:
- Use the dd command to measure server throughput (write speed)
```bash
dd if=/dev/zero of=/tmp/test1.img bs=1G count=1 oflag=dsync

```
- Use the dd command to measure server latency
```bash
dd if=/dev/zero of=/tmp/test2.img bs=512 count=1000 oflag=dsync

```