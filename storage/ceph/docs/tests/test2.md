# test 2 - recovery
- with 8 OSDs and replacing 1 OSD with removing osd and recreating it.
- TIP: you can replace OSDs with remaining OSD.id too
# logs and resaults
```
sudo ceph -w
  cluster:
    id:     15aff95a-de16-11eb-8213-cd7155651051
    health: HEALTH_WARN
            1 nearfull osd(s)
            Low space hindering backfill (add storage if this doesn't resolve itself): 1 pg backfill_toofull
            3 pool(s) nearfull
 
  services:
    mon: 1 daemons, quorum lff-204 (age 20h)
    mgr: lff-204.urbjnn(active, since 20h), standbys: lff-206.nsvakx
    mds: fs-01:1 {0=fs-01.lff-206.npyqfo=up:active}
    osd: 8 osds: 8 up (since 32s), 8 in (since 18h); 12 remapped pgs
 
  data:
    pools:   3 pools, 161 pgs
    objects: 1.49M objects, 1.9 TiB
    usage:   4.1 TiB used, 2.5 TiB / 6.5 TiB avail
    pgs:     190410/2989904 objects misplaced (6.368%)
             149 active+clean
             7   active+remapped+backfill_wait
             3   active+remapped+backfilling
             1   active+remapped
             1   active+remapped+backfill_wait+backfill_toofull
 
  io:
    recovery: 31 MiB/s, 23 objects/s
```
```
sudo ceph -s
  cluster:
    id:     15aff95a-de16-11eb-8213-cd7155651051
    health: HEALTH_WARN
            Degraded data redundancy: 325514/2990120 objects degraded (10.886%), 28 pgs degraded, 28 pgs undersized
 
  services:
    mon: 1 daemons, quorum lff-204 (age 20h)
    mgr: lff-204.urbjnn(active, since 20h), standbys: lff-206.nsvakx
    mds: fs-01:1 {0=fs-01.lff-206.npyqfo=up:active}
    osd: 8 osds: 8 up (since 4m), 8 in (since 4m); 47 remapped pgs
 
  data:
    pools:   3 pools, 161 pgs
    objects: 1.50M objects, 1.9 TiB
    usage:   3.5 TiB used, 3.0 TiB / 6.5 TiB avail
    pgs:     325514/2990120 objects degraded (10.886%)
             164809/2990120 objects misplaced (5.512%)
             114 active+clean
             27  active+undersized+degraded+remapped+backfill_wait
             17  active+remapped+backfill_wait
             2   active+remapped+backfilling
             1   active+undersized+degraded+remapped+backfilling
 
  io:
    recovery: 20 MiB/s, 15 objects/s
 
  progress:
    Rebalancing after osd.5 marked in (4m)
      [............................] 
```
## start 9:20 until 15:30 > 215 GB data on OSD

# **16:35**
```
sudo ceph -s
  cluster:
    id:     15aff95a-de16-11eb-8213-cd7155651051
    health: HEALTH_WARN
            Degraded data redundancy: 125068/2990120 objects degraded (4.183%), 11 pgs degraded, 11 pgs undersized
 
  services:
    mon: 1 daemons, quorum lff-204 (age 27h)
    mgr: lff-204.urbjnn(active, since 27h), standbys: lff-206.nsvakx
    mds: fs-01:1 {0=fs-01.lff-206.npyqfo=up:active}
    osd: 8 osds: 8 up (since 6h), 8 in (since 6h); 28 remapped pgs
 
  data:
    pools:   3 pools, 161 pgs
    objects: 1.50M objects, 1.9 TiB
    usage:   3.7 TiB used, 2.8 TiB / 6.5 TiB avail
    pgs:     125068/2990120 objects degraded (4.183%)
             127967/2990120 objects misplaced (4.280%)
             133 active+clean
             17  active+remapped+backfill_wait
             10  active+undersized+degraded+remapped+backfill_wait
             1   active+undersized+degraded+remapped+backfilling
 
  io:
    recovery: 8.6 MiB/s, 6 objects/s
 
  progress:
    Rebalancing after osd.5 marked in (6h)
      [............................] 
```