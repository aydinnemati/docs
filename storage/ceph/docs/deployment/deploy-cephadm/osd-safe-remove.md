
# SAFE REAMOVE OSD's
- See [ceph](https://docs.ceph.com/en/latest/rados/operations/add-or-rm-osds/#removing-the-osd)
- See [medium](https://vineetcic.medium.com/how-to-remove-add-osd-from-ceph-cluster-1c038eefe522)

### recovery config default
1. set osd out
```bash
$ sudo ceph osd out osd.{ID}
```
> - TIP: should wait until pg's are remapped on another OSD's befor set OSD down for removing it.

2. set osd down
```bash
$ sudo ceph osd down osd.{ID}
```
3. remove osd from crush map
```bash
$ sudo ceph osd crush rm osd.{ID}
```
4. remove it authorization (it should prevent problems with ‘couldn’t add new osd with same number’)
```bash
$ sudo ceph auth del osd.{ID}
```
5. make sure osd can be removed safly
```bash
$ sudo ceph osd safe-to-destroy osd.{ID}
```
6. destroy osd
```bash
$ sudo ceph osd destroy osd.{ID} --yes-i-really-mean-it
```
7. remove osd
```bash
$ sudo ceph osd rm osd.{ID}
```

# test osd safe remove 

- first out at 11:23 on sff-10

```
Every 0.1s: sudo ceph -s 
lff-11: Sun Feb 27 11:28:58 2022
  cluster:
    id:     373c158c-93eb-11ec-bcda-196a56b13d6f
    health: HEALTH_OK

  services:
    mon: 3 daemons, quorum lff-11,sff-10,sff-12 (age 17h)
    mgr: lff-11.pltwwe(active, since 3d), standbys: sff-10.kxnocd, sff-12.cgfeaf
    mds: 1/1 daemons up, 5 standby
    osd: 45 osds: 45 up (since 17h), 44 in (since 5m); 5 remapped pgs

  data:
    volumes: 1/1 healthy
    pools:   3 pools, 161 pgs
    objects: 526.47k objects, 1.0 TiB
    usage:   3.0 TiB used, 33 TiB / 36 TiB avail
    pgs:     4681/1579401 objects misplaced (0.296%)
             156 active+clean
             4   active+remapped+backfilling
             1   active+remapped+backfill_wait

  io:
    recovery: 49 MiB/s, 24 objects/s

  progress:
    Global Recovery Event (0s)
      [............................]
```
- second osd out at 11:31 on sff-12
```
Every 2.0s: sudo ceph -s                                                                                                                                                           lff-11: Sun Feb 27 11:33:38 2022

  cluster:
    id:     373c158c-93eb-11ec-bcda-196a56b13d6f
    health: HEALTH_OK

  services:
    mon: 3 daemons, quorum lff-11,sff-10,sff-12 (age 17h)
    mgr: lff-11.pltwwe(active, since 3d), standbys: sff-10.kxnocd, sff-12.cgfeaf
    mds: 1/1 daemons up, 5 standby
    osd: 45 osds: 45 up (since 17h), 43 in (since 3m); 14 remapped pgs

  data:
    volumes: 1/1 healthy
    pools:   3 pools, 161 pgs
    objects: 526.48k objects, 1.0 TiB
    usage:   3.0 TiB used, 32 TiB / 35 TiB avail
    pgs:     42799/1579440 objects misplaced (2.710%)
             147 active+clean
             12  active+remapped+backfilling
             2   active+remapped+backfill_wait

  io:
    recovery: 124 MiB/s, 61 objects/s

  progress:
    Global Recovery Event (3m)
      [=========================...] (remaining: 20s)
```
- 3rd out on sff-14
- 4th on sff-15
- 5th on sff-16
```
Every 2.0s: sudo ceph -s 
  lff-11: Sun Feb 27 11:35:53 2022

  cluster:
    id:     373c158c-93eb-11ec-bcda-196a56b13d6f
    health: HEALTH_OK

  services:
    mon: 3 daemons, quorum lff-11,sff-10,sff-12 (age 17h)
    mgr: lff-11.pltwwe(active, since 3d), standbys: sff-10.kxnocd, sff-12.cgfeaf
    mds: 1/1 daemons up, 5 standby
    osd: 45 osds: 45 up (since 17h), 40 in (since 18s); 43 remapped pgs

  data:
    volumes: 1/1 healthy
    pools:   3 pools, 161 pgs
    objects: 526.48k objects, 1.0 TiB
    usage:   2.7 TiB used, 30 TiB / 33 TiB avail
    pgs:     176700/1579446 objects misplaced (11.187%)
             118 active+clean
             22  active+remapped+backfilling
             21  active+remapped+backfill_wait

  io:
    recovery: 246 MiB/s, 3.55k keys/s, 124 objects/s

  progress:
    Global Recovery Event (5m)
      [====================........] (remaining: 2m)
```
- all out OSD's down at 11:37
``` 
Every 2.0s: sudo ceph -s      
lff-11: Sun Feb 27 11:38:33 2022
  cluster:
    id:     373c158c-93eb-11ec-bcda-196a56b13d6f
    health: HEALTH_OK

  services:
    mon: 3 daemons, quorum lff-11,sff-10,sff-12 (age 17h)
    mgr: lff-11.pltwwe(active, since 3d), standbys: sff-10.kxnocd, sff-12.cgfeaf
    mds: 1/1 daemons up, 5 standby
    osd: 45 osds: 45 up (since 91s), 40 in (since 2m); 43 remapped pgs

  data:
    volumes: 1/1 healthy
    pools:   3 pools, 161 pgs
    objects: 526.48k objects, 1.0 TiB
    usage:   2.8 TiB used, 30 TiB / 33 TiB avail
    pgs:     155659/1579446 objects misplaced (9.855%)
             118 active+clean
             23  active+remapped+backfilling
             20  active+remapped+backfill_wait

  io:
    recovery: 242 MiB/s, 121 objects/s

  progress:
    Global Recovery Event (8m)
      [====================........] (remaining: 3m)
```
- removed OSD's from crush map at 11:43
```
Every 2.0s: sudo ceph -s
lff-11: Sun Feb 27 11:43:40 2022

  cluster:
    id:     373c158c-93eb-11ec-bcda-196a56b13d6f
    health: HEALTH_OK

  services:
    mon: 3 daemons, quorum lff-11,sff-10,sff-12 (age 17h)
    mgr: lff-11.pltwwe(active, since 3d), standbys: sff-10.kxnocd, sff-12.cgfeaf
    mds: 1/1 daemons up, 5 standby
    osd: 45 osds: 45 up (since 6m), 40 in (since 8m); 44 remapped pgs

  data:
    volumes: 1/1 healthy
    pools:   3 pools, 161 pgs
    objects: 526.48k objects, 1.0 TiB
    usage:   2.8 TiB used, 30 TiB / 33 TiB avail
    pgs:     195665/1579446 objects misplaced (12.388%)
             117 active+clean
             27  active+remapped+backfill_wait
             17  active+remapped+backfilling

  io:
    recovery: 181 MiB/s, 90 objects/s

  progress:
    Global Recovery Event (13m)
      [====================........] (remaining: 5m)
```
