# Balancer
- The balancer can optimize the placement of PGs across OSDs in order to achieve a balanced distribution, either automatically or in a supervised fashion.

## status
```bash
$ sudo ceph balancer status
```
## Automatic balancing on/off
```bash
$ sudo ceph balancer on
$ sudo ceph balancer off
```
# Throttling
- No adjustments will be made to the PG distribution if the cluster is degraded (e.g., because an OSD has failed and the system has not yet healed itself). When the cluster is healthy, the balancer will throttle its changes such that the percentage of PGs that are misplaced (i.e., that need to be moved) is below a threshold of (by default) 5%. The target_max_misplaced_ratio threshold can be adjusted with:
```bash
$ sudo ceph config set mgr target_max_misplaced_ratio .07   # 7%
```
# Balancer Modes
have 2 modes: 
1. crush-compat
2. upmap
see [ceph.com](https://docs.ceph.com/en/octopus/rados/operations/balancer/)