# This would create a replicated pool with 128 placement groups, called MyPool
```bash
$ sudo ceph osd pool create MyPool 128 128 replicated
```