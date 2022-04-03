# warnings

- MDS_CACHE_OVERSIZED: 1 MDSs report oversized cache
```bash
$ sudo ceph config set mds mds_cache_memory_limit 34359738368
$ sudo ceph config get mds mds_cache_memory_limit
```