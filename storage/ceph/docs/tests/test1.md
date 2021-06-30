# test 1
## info
> 12 osd
- 10 ssf
- 2 lff

## status
- pool replica size 2 to 3 - when ceph making third replica - taking out 1 sff osd of sff-203
```bash
sudo ceph osd df
ID  CLASS  WEIGHT   REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS
 0    lff  2.72899   1.00000  2.7 TiB   38 GiB   37 GiB  242 MiB   782 MiB  2.7 TiB   1.37  0.12   55      up
 1    lff  2.72899   1.00000  2.7 TiB   38 GiB   37 GiB   82 MiB   942 MiB  2.7 TiB   1.36  0.12   51      up
 2    hdd  0.81870   1.00000  838 GiB   80 GiB   79 GiB   27 MiB   997 MiB  758 GiB   9.56  0.84   11      up
 3    hdd  0.81870   1.00000  838 GiB  195 GiB  194 GiB   50 MiB   974 MiB  643 GiB  23.28  2.05   30      up
 4    hdd  0.81870   1.00000  838 GiB  328 GiB  327 GiB   68 MiB   956 MiB  510 GiB  39.15  3.44    0    down
 5    hdd  0.81870   1.00000  838 GiB   68 GiB   67 GiB   28 MiB   996 MiB  770 GiB   8.16  0.72   10      up
 6    hdd  0.81870   1.00000  838 GiB   91 GiB   90 GiB   17 MiB  1007 MiB  747 GiB  10.84  0.95   13      up
 7    hdd  0.81870   1.00000  838 GiB  125 GiB  124 GiB   38 MiB   986 MiB  713 GiB  14.89  1.31    9      up
 8    hdd  0.81870   1.00000  838 GiB  172 GiB  171 GiB   41 MiB   983 MiB  666 GiB  20.58  1.81   18      up
 9    hdd  0.81870   1.00000  838 GiB   23 GiB   22 GiB   56 MiB   968 MiB  815 GiB   2.80  0.25    8      up
10    hdd  0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  1.90   14      up
11    hdd  0.81870   1.00000  838 GiB  248 GiB  247 GiB   27 MiB   997 MiB  591 GiB  29.56  2.60   19      up
                       TOTAL   14 TiB  1.6 TiB  1.5 TiB  705 MiB    11 GiB   12 TiB  11.37                   
MIN/MAX VAR: 0.12/3.44  STDDEV: 12.02
```
```bash
sudo ceph health detail
HEALTH_WARN 1 failed cephadm daemon(s); 1 osds down; Reduced data availability: 13 pgs inactive; Degraded data redundancy: 491574/1106208 objects degraded (44.438%), 33 pgs degraded, 14 pgs undersized
[WRN] CEPHADM_FAILED_DAEMON: 1 failed cephadm daemon(s)
    daemon crash.sff-205 on sff-205 is in error state
[WRN] OSD_DOWN: 1 osds down
    osd.4 (root=default,host=sff-203) is down
[WRN] PG_AVAILABILITY: Reduced data availability: 13 pgs inactive
    pg 5.0 is stuck inactive for 60s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1 is stuck inactive for 60s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.3 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.4 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.9 is stuck inactive for 60s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.a is stuck inactive for 60s, current state undersized+degraded+remapped+backfilling+peered, last acting [8]
    pg 5.c is stuck inactive for 60s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.f is stuck inactive for 60s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.15 is stuck inactive for 60s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.17 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.18 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.19 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.1b is stuck inactive for 60s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
[WRN] PG_DEGRADED: Degraded data redundancy: 491574/1106208 objects degraded (44.438%), 33 pgs degraded, 14 pgs undersized
    pg 4.9 is active+undersized+degraded, acting [0,11]
    pg 4.c is active+undersized+degraded, acting [9,1]
    pg 5.0 is undersized+degraded+remapped+backfill_wait+peered, acting [10]
    pg 5.1 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.2 is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [2,10]
    pg 5.3 is undersized+degraded+remapped+backfill_wait+peered, acting [10]
    pg 5.4 is undersized+degraded+remapped+backfill_wait+peered, acting [7]
    pg 5.5 is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [3,11]
    pg 5.6 is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.7 is active+undersized+degraded+remapped+backfill_wait, acting [7,5]
    pg 5.8 is active+undersized+degraded+remapped+backfill_wait, acting [2,8]
    pg 5.9 is undersized+degraded+remapped+backfill_wait+peered, acting [7]
    pg 5.a is undersized+degraded+remapped+backfilling+peered, acting [8]
    pg 5.b is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [5,8]
    pg 5.c is undersized+degraded+remapped+backfill_wait+peered, acting [10]
    pg 5.d is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [11,3]
    pg 5.e is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [9,5]
    pg 5.f is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.10 is active+undersized+degraded+remapped+backfill_wait, acting [11,6]
    pg 5.11 is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [3,10]
    pg 5.12 is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [3,11]
    pg 5.13 is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [7,3]
    pg 5.14 is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [3,11]
    pg 5.15 is undersized+degraded+remapped+backfill_wait+peered, acting [8]
    pg 5.16 is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,11]
    pg 5.17 is undersized+degraded+remapped+backfill_wait+peered, acting [8]
    pg 5.18 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.19 is undersized+degraded+remapped+backfill_wait+peered, acting [7]
    pg 5.1a is active+undersized+degraded, acting [8,0]
    pg 5.1b is undersized+degraded+remapped+backfill_wait+peered, acting [10]
    pg 5.1c is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [11,2]
    pg 5.1e is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.1f is stuck undersized for 41m, current state active+undersized+degraded+remapped+backfill_wait, last acting [3,11]
```
```bash
sudo ceph osd dump
epoch 276
fsid 056b080a-d7db-11eb-af8f-d1706eecbddb
created 2021-06-28T06:36:01.816803+0000
modified 2021-06-30T07:11:45.355309+0000
flags sortbitwise,recovery_deletes,purged_snapdirs,pglog_hardlimit
crush_version 45
full_ratio 0.95
backfillfull_ratio 0.9
nearfull_ratio 0.85
require_min_compat_client jewel
min_compat_client jewel
require_osd_release octopus
pool 1 'device_health_metrics' replicated size 3 min_size 2 crush_rule 0 object_hash rjenkins pg_num 1 pgp_num 1 autoscale_mode on last_change 271 flags hashpspool stripe_width 0 pg_num_min 1 application mgr_devicehealth
pool 4 'cephfs.test-fs-1.meta' replicated size 3 min_size 2 crush_rule 0 object_hash rjenkins pg_num 32 pgp_num 32 autoscale_mode on last_change 257 flags hashpspool stripe_width 0 pg_autoscale_bias 4 pg_num_min 16 recovery_priority 5 application cephfs
pool 5 'cephfs.test-fs-1.data' replicated size 3 min_size 2 crush_rule 0 object_hash rjenkins pg_num 32 pgp_num 32 autoscale_mode on last_change 261 flags hashpspool stripe_width 0 application cephfs
pool 6 'lff-poo' replicated size 3 min_size 2 crush_rule 1 object_hash rjenkins pg_num 32 pgp_num 32 autoscale_mode on last_change 254 flags hashpspool stripe_width 0
max_osd 12
osd.0 up   in  weight 1 up_from 235 up_thru 274 down_at 223 last_clean_interval [140,222) [v2:10.0.23.4:6800/2262148995,v1:10.0.23.4:6801/2262148995] [v2:10.0.22.4:6802/2262148995,v1:10.0.22.4:6803/2262148995] exists,up 1ca23f1e-d9bd-493e-a9b6-7be968a54917
osd.1 up   in  weight 1 up_from 233 up_thru 274 down_at 232 last_clean_interval [148,223) [v2:10.0.23.6:6800/3772970023,v1:10.0.23.6:6801/3772970023] [v2:10.0.22.6:6802/3772970023,v1:10.0.22.6:6803/3772970023] exists,up cf44e216-c22d-48f7-b31e-a3312994b0e9
osd.2 up   in  weight 1 up_from 233 up_thru 274 down_at 232 last_clean_interval [137,223) [v2:10.0.22.3:6826/4018773204,v1:10.0.22.3:6827/4018773204] [v2:10.0.22.3:6828/4018773204,v1:10.0.22.3:6829/4018773204] exists,up 262f583c-a9a0-4b82-affb-134ddea1423a
osd.3 up   in  weight 1 up_from 234 up_thru 265 down_at 233 last_clean_interval [138,223) [v2:10.0.23.3:6818/331541622,v1:10.0.23.3:6819/331541622] [v2:10.0.22.3:6820/331541622,v1:10.0.22.3:6821/331541622] exists,up 98b85a30-6ce4-411f-9298-13adca9f90dd
osd.4 down in  weight 1 up_from 234 up_thru 265 down_at 274 last_clean_interval [137,223) [v2:10.0.23.3:6802/1444372829,v1:10.0.23.3:6803/1444372829] [v2:10.0.22.3:6804/1444372829,v1:10.0.22.3:6805/1444372829] exists b3cb65ae-c5a0-44f3-8ddd-21c56a832dad
osd.5 up   in  weight 1 up_from 232 up_thru 265 down_at 231 last_clean_interval [138,223) [v2:10.0.23.3:6834/3331078859,v1:10.0.23.3:6835/3331078859] [v2:10.0.22.3:6836/3331078859,v1:10.0.22.3:6837/3331078859] exists,up 407c4c95-7057-46be-940f-43a8f2343a7a
osd.6 up   in  weight 1 up_from 232 up_thru 265 down_at 231 last_clean_interval [138,223) [v2:10.0.23.3:6810/3315713204,v1:10.0.23.3:6811/3315713204] [v2:10.0.22.3:6812/3315713204,v1:10.0.22.3:6813/3315713204] exists,up b2ec551d-8e4e-4e55-86b0-29f875cfa8d6
osd.7 up   in  weight 1 up_from 231 up_thru 274 down_at 230 last_clean_interval [135,223) [v2:10.0.23.5:6834/1847803541,v1:10.0.23.5:6835/1847803541] [v2:10.0.22.5:6836/1847803541,v1:10.0.22.5:6837/1847803541] exists,up b401fd0c-c920-4611-8cd0-5a5dd71aad85
osd.8 up   in  weight 1 up_from 232 up_thru 274 down_at 231 last_clean_interval [135,223) [v2:10.0.23.5:6802/1662250473,v1:10.0.23.5:6803/1662250473] [v2:10.0.22.5:6804/1662250473,v1:10.0.22.5:6805/1662250473] exists,up 2b1ba4da-7664-4c3f-b82e-519ce5f51ee0
osd.9 up   in  weight 1 up_from 230 up_thru 274 down_at 229 last_clean_interval [135,223) [v2:10.0.23.5:6811/3275088528,v1:10.0.23.5:6813/3275088528] [v2:10.0.22.5:6816/3275088528,v1:10.0.22.5:6819/3275088528] exists,up ce6be08a-8b65-439c-9727-a417e142cc0b
osd.10 up   in  weight 1 up_from 232 up_thru 274 down_at 231 last_clean_interval [135,223) [v2:10.0.23.5:6812/1673980142,v1:10.0.23.5:6814/1673980142] [v2:10.0.22.5:6817/1673980142,v1:10.0.22.5:6820/1673980142] exists,up 8959c15a-869c-45d0-a7ac-f08580627f16
osd.11 up   in  weight 1 up_from 233 up_thru 274 down_at 232 last_clean_interval [135,223) [v2:10.0.23.5:6810/324008842,v1:10.0.23.5:6815/324008842] [v2:10.0.22.5:6818/324008842,v1:10.0.22.5:6822/324008842] exists,up 5c78aba1-c153-47c4-b127-7cff616c1645
pg_temp 5.0 [4,10]
pg_temp 5.1 [4,11]
pg_temp 5.2 [2,10]
pg_temp 5.3 [4,10]
pg_temp 5.4 [4,7]
pg_temp 5.5 [3,11]
pg_temp 5.6 [6,10]
pg_temp 5.7 [7,5]
pg_temp 5.8 [2,8]
pg_temp 5.9 [7,4]
pg_temp 5.a [4,8]
pg_temp 5.b [5,8]
pg_temp 5.c [4,10]
pg_temp 5.d [11,3]
pg_temp 5.e [9,5]
pg_temp 5.f [4,11]
pg_temp 5.10 [11,6]
pg_temp 5.11 [3,10]
pg_temp 5.12 [3,11]
pg_temp 5.13 [7,3]
pg_temp 5.14 [3,11]
pg_temp 5.15 [4,8]
pg_temp 5.16 [6,11]
pg_temp 5.17 [4,8]
pg_temp 5.18 [4,11]
pg_temp 5.19 [4,7]
pg_temp 5.1b [4,10]
pg_temp 5.1c [11,2]
pg_temp 5.1e [6,10]
pg_temp 5.1f [3,11]
pg_temp 6.0 [0,1,2]
pg_temp 6.1 [0,1,6]
pg_temp 6.4 [0,1,6]
pg_temp 6.5 [0,1,3]
pg_temp 6.6 [1,0,8]
pg_temp 6.7 [1,0,5]
pg_temp 6.8 [1,0,6]
pg_temp 6.9 [0,1,3]
pg_temp 6.b [0,1,8]
pg_temp 6.d [0,1,3]
pg_temp 6.e [0,1,10]
pg_temp 6.10 [0,1,2]
pg_temp 6.11 [1,0,6]
pg_temp 6.12 [1,0,6]
pg_temp 6.14 [1,0,3]
pg_temp 6.15 [0,1,2]
pg_temp 6.16 [0,1,7]
pg_temp 6.17 [0,1,2]
pg_temp 6.19 [1,0,3]
pg_temp 6.1a [0,1,2]
pg_temp 6.1b [0,1,3]
pg_temp 6.1c [0,1,3]
pg_temp 6.1d [0,1,5]
pg_temp 6.1e [0,1,3]
pg_temp 6.1f [1,0,3]
blacklist 10.0.23.3:0/3456329347 expires 2021-07-01T06:47:47.476458+0000
blacklist 10.0.23.5:6843/3145065650 expires 2021-07-01T05:15:31.097047+0000
blacklist 10.0.23.3:6843/312399314 expires 2021-07-01T06:47:47.476458+0000
blacklist 10.0.23.3:6841/887318668 expires 2021-06-30T11:35:26.114538+0000
blacklist 10.0.23.3:6840/887318668 expires 2021-06-30T11:35:26.114538+0000
blacklist 10.0.23.3:0/850209898 expires 2021-06-30T13:35:44.469080+0000
blacklist 10.0.23.3:6841/369029989 expires 2021-06-30T13:35:44.469080+0000
blacklist 10.0.23.5:0/2405385918 expires 2021-06-30T15:38:42.638123+0000
blacklist 10.0.23.5:6842/2206507652 expires 2021-07-01T05:10:26.725052+0000
blacklist 10.0.23.3:6840/369029989 expires 2021-06-30T13:35:44.469080+0000
blacklist 10.0.23.3:6842/3388675123 expires 2021-07-01T05:10:25.156194+0000
blacklist 10.0.23.5:6841/611726419 expires 2021-07-01T05:10:35.526854+0000
blacklist 10.0.23.3:0/3771892218 expires 2021-07-01T06:47:47.476458+0000
blacklist 10.0.23.3:0/459586095 expires 2021-06-30T11:35:26.114538+0000
blacklist 10.0.23.5:6840/1717674289 expires 2021-06-30T10:01:48.179779+0000
blacklist 10.0.23.5:0/2968608373 expires 2021-06-30T10:01:48.179779+0000
blacklist 10.0.23.3:0/3762449070 expires 2021-06-30T11:35:26.114538+0000
blacklist 10.0.23.5:6841/1717674289 expires 2021-06-30T10:01:48.179779+0000
blacklist 10.0.23.3:0/2472766133 expires 2021-06-30T13:35:44.469080+0000
blacklist 10.0.23.5:0/1009929530 expires 2021-06-30T10:01:48.179779+0000
blacklist 10.0.23.5:0/2056597828 expires 2021-06-30T10:01:48.179779+0000
blacklist 10.0.23.5:6844/4219987915 expires 2021-06-30T08:59:57.141813+0000
blacklist 10.0.23.5:6845/4219987915 expires 2021-06-30T08:59:57.141813+0000
blacklist 10.0.23.5:0/2088230881 expires 2021-06-30T15:38:42.638123+0000
blacklist 10.0.23.5:6842/3145065650 expires 2021-07-01T05:15:31.097047+0000
blacklist 10.0.23.5:6841/1139300828 expires 2021-06-30T15:38:42.638123+0000
blacklist 10.0.23.5:6840/1139300828 expires 2021-06-30T15:38:42.638123+0000
blacklist 10.0.23.3:6843/3388675123 expires 2021-07-01T05:10:25.156194+0000
blacklist 10.0.23.5:6843/2206507652 expires 2021-07-01T05:10:26.725052+0000
blacklist 10.0.23.5:0/126888795 expires 2021-07-01T05:10:35.526854+0000
blacklist 10.0.23.5:0/3471251616 expires 2021-07-01T05:15:31.097047+0000
blacklist 10.0.23.5:0/2123869471 expires 2021-07-01T05:10:35.526854+0000
blacklist 10.0.23.3:6800/3793408774 expires 2021-07-01T06:34:30.363219+0000
blacklist 10.0.23.5:6840/611726419 expires 2021-07-01T05:10:35.526854+0000
blacklist 10.0.23.5:0/1300402075 expires 2021-07-01T05:15:31.097047+0000
blacklist 10.0.23.3:6842/312399314 expires 2021-07-01T06:47:47.476458+0000
blacklist 10.0.23.5:0/96457135 expires 2021-07-01T05:15:31.097047+0000
blacklist 10.0.23.3:0/295213818 expires 2021-07-01T06:47:47.476458+0000
blacklist 10.0.23.3:6801/3793408774 expires 2021-07-01T06:34:30.363219+0000
```
```bash
sudo ceph pg stat
97 pgs: 1 undersized+degraded+remapped+backfilling+peered, 32 active+clean, 25 active+clean+remapped, 12 undersized+degraded+remapped+backfill_wait+peered, 7 active+undersized, 17 active+undersized+degraded+remapped+backfill_wait, 3 active+undersized+degraded; 720 GiB data, 1.5 TiB used, 12 TiB / 14 TiB avail; 490466/1106208 objects degraded (44.338%); 331097/1106208 objects misplaced (29.931%); 16 MiB/s, 7 objects/s recovering
```
```bash
sudo ceph osd pool stats
pool device_health_metrics id 1
  nothing is going on

pool cephfs.test-fs-1.meta id 4
  7/381 objects degraded (1.837%)

pool cephfs.test-fs-1.data id 5
  487765/1105827 objects degraded (44.109%)
  331097/1105827 objects misplaced (29.941%)
  recovery io 13 MiB/s, 6 objects/s
```
```bash
sudo ceph osd df tree
ID  CLASS  WEIGHT    REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS  TYPE NAME       
-1         13.64493         -   14 TiB  1.6 TiB  1.5 TiB  705 MiB    11 GiB   12 TiB  11.44  1.00    -          root default    
-3          2.72899         -  2.7 TiB   43 GiB   42 GiB  242 MiB   782 MiB  2.7 TiB   1.53  0.13    -              host lff-204
 0    lff   2.72899   1.00000  2.7 TiB   43 GiB   42 GiB  242 MiB   782 MiB  2.7 TiB   1.53  0.13   55      up          osd.0   
-5          2.72899         -  2.7 TiB   43 GiB   42 GiB   82 MiB   942 MiB  2.7 TiB   1.53  0.13    -              host lff-206
 1    lff   2.72899   1.00000  2.7 TiB   43 GiB   42 GiB   82 MiB   942 MiB  2.7 TiB   1.53  0.13   51      up          osd.1   
-7          4.09348         -  4.1 TiB  763 GiB  758 GiB  190 MiB   4.8 GiB  3.3 TiB  18.20  1.59    -              host sff-203
 2    hdd   0.81870   1.00000  838 GiB   80 GiB   79 GiB   27 MiB   997 MiB  758 GiB   9.56  0.84   11      up          osd.2   
 3    hdd   0.81870   1.00000  838 GiB  195 GiB  194 GiB   50 MiB   974 MiB  643 GiB  23.28  2.04   30      up          osd.3   
 4    hdd   0.81870   1.00000  838 GiB  328 GiB  327 GiB   68 MiB   956 MiB  510 GiB  39.15  3.42    0    down          osd.4   
 5    hdd   0.81870   1.00000  838 GiB   68 GiB   67 GiB   28 MiB   996 MiB  770 GiB   8.16  0.71   10      up          osd.5   
 6    hdd   0.81870   1.00000  838 GiB   91 GiB   90 GiB   17 MiB  1007 MiB  747 GiB  10.84  0.95   13      up          osd.6   
-9          4.09348         -  4.1 TiB  750 GiB  745 GiB  191 MiB   4.8 GiB  3.4 TiB  17.89  1.56    -              host sff-205
 7    hdd   0.81870   1.00000  838 GiB  125 GiB  124 GiB   38 MiB   986 MiB  713 GiB  14.89  1.30    9      up          osd.7   
 8    hdd   0.81870   1.00000  838 GiB  172 GiB  171 GiB   41 MiB   983 MiB  666 GiB  20.58  1.80   18      up          osd.8   
 9    hdd   0.81870   1.00000  838 GiB   23 GiB   22 GiB   56 MiB   968 MiB  815 GiB   2.80  0.24    8      up          osd.9   
10    hdd   0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  1.89   14      up          osd.10  
11    hdd   0.81870   1.00000  838 GiB  248 GiB  247 GiB   27 MiB   997 MiB  591 GiB  29.56  2.58   19      up          osd.11  
                        TOTAL   14 TiB  1.6 TiB  1.5 TiB  705 MiB    11 GiB   12 TiB  11.44                                     
MIN/MAX VAR: 0.13/3.42  STDDEV: 11.98
```
```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_WARN
            1 failed cephadm daemon(s)
            1 osds down
            Reduced data availability: 13 pgs inactive
            Degraded data redundancy: 486656/1106208 objects degraded (43.993%), 33 pgs degraded, 40 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 2m)
    mgr: sff-205.narmtr(active, since 28m), standbys: sff-203.wprkbk
    mds: test-fs-1:1 {0=test-fs-1.sff-205.bziwst=up:active} 1 up:standby
    osd: 12 osds: 11 up (since 6m), 12 in (since 24h); 55 remapped pgs
 
  task status:
 
  data:
    pools:   4 pools, 97 pgs
    objects: 368.74k objects, 720 GiB
    usage:   1.6 TiB used, 12 TiB / 14 TiB avail
    pgs:     13.402% pgs not active
             486656/1106208 objects degraded (43.993%)
             331097/1106208 objects misplaced (29.931%)
             32 active+clean
             25 active+clean+remapped
             17 active+undersized+degraded+remapped+backfill_wait
             12 undersized+degraded+remapped+backfill_wait+peered
             7  active+undersized
             3  active+undersized+degraded
             1  undersized+degraded+remapped+backfilling+peered
 
  io:
    recovery: 13 MiB/s, 6 objects/s
 

2021-06-30T11:46:41.080735+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 486656/1106208 objects degraded (43.993%), 33 pgs degraded, 40 pgs undersized (PG_DEGRADED)
2021-06-30T11:46:46.090604+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 486498/1106208 objects degraded (43.979%), 33 pgs degraded, 40 pgs undersized (PG_DEGRADED)
2021-06-30T11:46:52.159754+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 486418/1106208 objects degraded (43.972%), 33 pgs degraded, 40 pgs undersized (PG_DEGRADED)
2021-06-30T11:47:01.118617+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 486338/1106208 objects degraded (43.964%), 33 pgs degraded, 40 pgs undersized (PG_DEGRADED)
2021-06-30T11:47:06.119690+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 486178/1106208 objects degraded (43.950%), 33 pgs degraded, 40 pgs undersized (PG_DEGRADED)
2021-06-30T11:47:12.185981+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 486098/1106208 objects degraded (43.943%), 33 pgs degraded, 40 pgs undersized (PG_DEGRADED)
2021-06-30T11:47:21.145116+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 486020/1106208 objects degraded (43.936%), 33 pgs degraded, 40 pgs undersized (PG_DEGRADED)
```
```bash
sudo ceph status
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_WARN
            1 failed cephadm daemon(s)
            1 osds down
            Reduced data availability: 13 pgs inactive
            Degraded data redundancy: 485860/1106208 objects degraded (43.921%), 33 pgs degraded, 40 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 3m)
    mgr: sff-205.narmtr(active, since 29m), standbys: sff-203.wprkbk
    mds: test-fs-1:1 {0=test-fs-1.sff-205.bziwst=up:active} 1 up:standby
    osd: 12 osds: 11 up (since 7m), 12 in (since 24h); 55 remapped pgs
 
  task status:
 
  data:
    pools:   4 pools, 97 pgs
    objects: 368.74k objects, 720 GiB
    usage:   1.6 TiB used, 12 TiB / 14 TiB avail
    pgs:     13.402% pgs not active
             485860/1106208 objects degraded (43.921%)
             331097/1106208 objects misplaced (29.931%)
             32 active+clean
             25 active+clean+remapped
             17 active+undersized+degraded+remapped+backfill_wait
             12 undersized+degraded+remapped+backfill_wait+peered
             7  active+undersized
             3  active+undersized+degraded
             1  undersized+degraded+remapped+backfilling+peered
 
  io:
    recovery: 13 MiB/s, 6 objects/s
```
## taking out second osd on sff-203
```bash
sudo ceph health detail
HEALTH_WARN 3 failed cephadm daemon(s); failed to probe daemons or devices; 1 osds down; Reduced data availability: 16 pgs inactive; Degraded data redundancy: 568117/1106208 objects degraded (51.357%), 46 pgs degraded, 20 pgs undersized
[WRN] CEPHADM_FAILED_DAEMON: 3 failed cephadm daemon(s)
    daemon prometheus.sff-203 on sff-203 is in error state
    daemon osd.4 on sff-203 is in error state
    daemon crash.sff-205 on sff-205 is in error state
[WRN] CEPHADM_REFRESH_FAILED: failed to probe daemons or devices
    host sff-205 `cephadm ceph-volume` failed: cephadm exited with an error code: 1, stderr:Non-zero exit code 125 from /usr/bin/docker run --rm --ipc=host --net=host --entrypoint stat -e CONTAINER_IMAGE=docker.io/ceph/ceph:v15 -e NODE_NAME=sff-205 docker.io/ceph/ceph:v15 -c %u %g /var/lib/ceph
stat: stderr Unable to find image 'ceph/ceph:v15' locally
stat: stderr v15: Pulling from ceph/ceph
stat: stderr 7a0437f04f83: Pulling fs layer
stat: stderr 731c3beff4de: Pulling fs layer
stat: stderr docker: error parsing HTTP 403 response body: invalid character '<' looking for beginning of value: "<html><body><h1>403 Forbidden</h1>\nSince Docker is a US company, we must comply with US export control regulations. In an effort to comply with these, we now block all IP addresses that are located in Cuba, Iran, North Korea, Republic of Crimea, Sudan, and Syria. If you are not in one of these cities, countries, or regions and are blocked, please reach out to https://hub.docker.com/support/contact/\n</body></html>\n".
stat: stderr See 'docker run --help'.
Traceback (most recent call last):
  File "<stdin>", line 6224, in <module>
  File "<stdin>", line 1340, in _infer_fsid
  File "<stdin>", line 1423, in _infer_image
  File "<stdin>", line 3655, in command_ceph_volume
  File "<stdin>", line 1521, in make_log_dir
  File "<stdin>", line 2134, in extract_uid_gid
RuntimeError: uid/gid not found
    host sff-203 `cephadm ceph-volume` failed: cephadm exited with an error code: 1, stderr:Non-zero exit code 125 from /usr/bin/docker run --rm --ipc=host --net=host --entrypoint stat -e CONTAINER_IMAGE=docker.io/ceph/ceph:v15 -e NODE_NAME=sff-203 docker.io/ceph/ceph:v15 -c %u %g /var/lib/ceph
stat: stderr Unable to find image 'ceph/ceph:v15' locally
stat: stderr v15: Pulling from ceph/ceph
stat: stderr 7a0437f04f83: Pulling fs layer
stat: stderr 731c3beff4de: Pulling fs layer
stat: stderr docker: Head https://registry-1.docker.io/v2/ceph/ceph/manifests/v15: Get https://auth.docker.io/token?scope=repository%3Aceph%2Fceph%3Apull&service=registry.docker.io: net/http: request canceled (Client.Timeout exceeded while awaiting headers).
stat: stderr See 'docker run --help'.
Traceback (most recent call last):
  File "<stdin>", line 6224, in <module>
  File "<stdin>", line 1340, in _infer_fsid
  File "<stdin>", line 1423, in _infer_image
  File "<stdin>", line 3655, in command_ceph_volume
  File "<stdin>", line 1521, in make_log_dir
  File "<stdin>", line 2134, in extract_uid_gid
RuntimeError: uid/gid not found
[WRN] OSD_DOWN: 1 osds down
    osd.3 (root=default,host=sff-203) is down
[WRN] PG_AVAILABILITY: Reduced data availability: 16 pgs inactive
    pg 5.0 is stuck inactive for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1 is stuck inactive for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.3 is stuck inactive for 2h, current state undersized+degraded+remapped+backfilling+peered, last acting [10]
    pg 5.4 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.9 is stuck inactive for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.a is stuck inactive for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.c is stuck inactive for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.f is stuck inactive for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.11 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.12 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.14 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.15 is stuck inactive for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.17 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.18 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.19 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.1b is stuck inactive for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
[WRN] PG_DEGRADED: Degraded data redundancy: 568117/1106208 objects degraded (51.357%), 46 pgs degraded, 20 pgs undersized
    pg 4.1 is active+undersized+degraded, acting [11,1]
    pg 4.7 is active+undersized+degraded, acting [0,10]
    pg 4.8 is active+undersized+degraded, acting [1,9]
    pg 4.9 is active+undersized+degraded+remapped+backfill_wait, acting [0,11]
    pg 4.b is active+undersized+degraded, acting [8,1]
    pg 4.d is active+undersized+degraded, acting [10,0]
    pg 4.11 is active+undersized+degraded, acting [1,8]
    pg 4.12 is active+undersized+degraded, acting [0,11]
    pg 4.15 is active+undersized+degraded, acting [8,0]
    pg 4.17 is active+undersized+degraded, acting [0,10]
    pg 4.19 is active+undersized+degraded, acting [11,0]
    pg 4.1a is active+undersized+degraded, acting [8,0]
    pg 4.1d is active+undersized+degraded, acting [9,0]
    pg 4.1f is active+undersized+degraded, acting [8,0]
    pg 5.0 is undersized+degraded+remapped+backfill_wait+peered, acting [10]
    pg 5.1 is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.2 is stuck undersized for 51m, current state active+undersized+degraded+remapped+backfill_wait, last acting [2,10]
    pg 5.3 is stuck undersized for 10m, current state undersized+degraded+remapped+backfilling+peered, last acting [10]
    pg 5.4 is undersized+degraded+remapped+backfill_wait+peered, acting [7]
    pg 5.5 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.6 is stuck undersized for 51m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.7 is active+undersized+degraded+remapped+backfill_wait, acting [7,5]
    pg 5.8 is active+undersized+degraded+remapped+backfill_wait, acting [2,8]
    pg 5.9 is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.a is undersized+degraded+remapped+backfill_wait+peered, acting [8]
    pg 5.b is stuck undersized for 51m, current state active+undersized+degraded+remapped+backfill_wait, last acting [5,8]
    pg 5.c is undersized+degraded+remapped+backfill_wait+peered, acting [10]
    pg 5.d is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.e is active+undersized+degraded+remapped+backfill_wait, acting [9,5]
    pg 5.10 is active+undersized+degraded+remapped+backfill_wait, acting [11,6]
    pg 5.11 is undersized+degraded+remapped+backfill_wait+peered, acting [10]
    pg 5.12 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.13 is undersized+degraded+remapped+backfill_wait+peered, acting [7]
    pg 5.14 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.15 is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.16 is stuck undersized for 51m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,11]
    pg 5.17 is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.18 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.19 is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.1a is active+undersized+degraded+remapped+backfill_wait, acting [8,0]
    pg 5.1b is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1c is active+undersized+degraded+remapped+backfill_wait, acting [11,2]
    pg 5.1d is active+undersized+degraded, acting [8,1]
    pg 5.1e is stuck undersized for 51m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.1f is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 6.2 is stuck undersized for 10m, current state active+undersized, last acting [0,1]
    pg 6.3 is stuck undersized for 10m, current state active+undersized, last acting [1,0]
    pg 6.a is stuck undersized for 10m, current state active+undersized, last acting [0,1]
    pg 6.f is stuck undersized for 10m, current state active+undersized, last acting [1,0]
    pg 6.13 is stuck undersized for 10m, current state active+undersized, last acting [0,1]
    pg 6.18 is stuck undersized for 10m, current state active+undersized, last acting [0,1]
```
```bash
sudo ceph status
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_WARN
            3 failed cephadm daemon(s)
            failed to probe daemons or devices
            1 osds down
            Reduced data availability: 64 pgs inactive
            Degraded data redundancy: 567852/1106208 objects degraded (51.333%), 142 pgs degraded, 7 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 2m)
    mgr: sff-205.narmtr(active, since 33m), standbys: sff-203.wprkbk
    mds: test-fs-1:1 {0=test-fs-1.sff-205.bziwst=up:active} 1 up:standby
    osd: 12 osds: 10 up (since 41s), 11 in (since 43s); 141 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 368.74k objects, 720 GiB
    usage:   1.2 TiB used, 12 TiB / 13 TiB avail
    pgs:     41.451% pgs not active
             567852/1106208 objects degraded (51.333%)
             287729/1106208 objects misplaced (26.010%)
             79 undersized+degraded+remapped+backfill_wait+peered
             45 active+undersized+degraded+remapped+backfill_wait
             19 active+clean
             17 active+undersized+degraded
             16 active+undersized
             16 active+clean+remapped
             1  undersized+degraded+remapped+backfilling+peered
 
  io:
    recovery: 12 MiB/s, 6 objects/s
 
  progress:
    PG autoscaler increasing pool 5 PGs from 32 to 128 (0s)
      [............................] 
```
```bash
sudo ceph osd df
ID  CLASS  WEIGHT   REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS
 0    lff  2.72899   1.00000  2.7 TiB   48 GiB   47 GiB  242 MiB   782 MiB  2.7 TiB   1.70  0.17   58      up
 1    lff  2.72899   1.00000  2.7 TiB   48 GiB   47 GiB   82 MiB   942 MiB  2.7 TiB   1.70  0.17   54      up
 2    hdd  0.81870   1.00000  838 GiB   80 GiB   79 GiB   27 MiB   997 MiB  758 GiB   9.56  0.98   20      up
 3    hdd  0.81870   1.00000  838 GiB  195 GiB  194 GiB   50 MiB   974 MiB  643 GiB  23.28  2.39    0    down
 4    hdd  0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down
 5    hdd  0.81870   1.00000  838 GiB   68 GiB   67 GiB   28 MiB   996 MiB  770 GiB   8.16  0.84   20      up
 6    hdd  0.81870   1.00000  838 GiB   91 GiB   90 GiB   17 MiB  1007 MiB  747 GiB  10.84  1.11   25      up
 7    hdd  0.81870   1.00000  838 GiB  125 GiB  124 GiB   38 MiB   986 MiB  713 GiB  14.89  1.53   24      up
 8    hdd  0.81870   1.00000  838 GiB  173 GiB  172 GiB   41 MiB   983 MiB  666 GiB  20.58  2.11   39      up
 9    hdd  0.81870   1.00000  838 GiB   24 GiB   23 GiB   56 MiB   968 MiB  815 GiB   2.84  0.29   11      up
10    hdd  0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  2.22   38      up
11    hdd  0.81870   1.00000  838 GiB  248 GiB  247 GiB   27 MiB   997 MiB  591 GiB  29.56  3.03   52      up
                       TOTAL   13 TiB  1.3 TiB  1.2 TiB  637 MiB    10 GiB   12 TiB   9.75                   
MIN/MAX VAR: 0.17/3.03  STDDEV: 9.73
```
```bash
sudo ceph osd tree
ID  CLASS  WEIGHT    TYPE NAME         STATUS  REWEIGHT  PRI-AFF
-1         13.64493  root default                               
-3          2.72899      host lff-204                           
 0    lff   2.72899          osd.0         up   1.00000  1.00000
-5          2.72899      host lff-206                           
 1    lff   2.72899          osd.1         up   1.00000  1.00000
-7          4.09348      host sff-203                           
 2    hdd   0.81870          osd.2         up   1.00000  1.00000
 3    hdd   0.81870          osd.3       down   1.00000  1.00000
 4    hdd   0.81870          osd.4       down         0  1.00000
 5    hdd   0.81870          osd.5         up   1.00000  1.00000
 6    hdd   0.81870          osd.6         up   1.00000  1.00000
-9          4.09348      host sff-205                           
 7    hdd   0.81870          osd.7         up   1.00000  1.00000
 8    hdd   0.81870          osd.8         up   1.00000  1.00000
 9    hdd   0.81870          osd.9         up   1.00000  1.00000
10    hdd   0.81870          osd.10        up   1.00000  1.00000
11    hdd   0.81870          osd.11        up   1.00000  1.00000
```
```bash
sudo ceph osd pool stats
pool device_health_metrics id 1
  nothing is going on

pool cephfs.test-fs-1.meta id 4
  60/381 objects degraded (15.748%)

pool cephfs.test-fs-1.data id 5
  566464/1105827 objects degraded (51.225%)
  287729/1105827 objects misplaced (26.019%)
  recovery io 13 MiB/s, 6 objects/s
```
```bash
sudo ceph status
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_WARN
            3 failed cephadm daemon(s)
            failed to probe daemons or devices
            1 osds down
            Reduced data availability: 80 pgs inactive
            Degraded data redundancy: 565806/1106208 objects degraded (51.148%), 142 pgs degraded, 158 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 85s)
    mgr: sff-205.narmtr(active, since 35m), standbys: sff-203.wprkbk
    mds: test-fs-1:1 {0=test-fs-1.sff-205.bziwst=up:active} 1 up:standby
    osd: 12 osds: 10 up (since 2m), 11 in (since 2m); 141 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 368.74k objects, 720 GiB
    usage:   1.3 TiB used, 12 TiB / 13 TiB avail
    pgs:     41.451% pgs not active
             565806/1106208 objects degraded (51.148%)
             287729/1106208 objects misplaced (26.010%)
             79 undersized+degraded+remapped+backfill_wait+peered
             45 active+undersized+degraded+remapped+backfill_wait
             19 active+clean
             17 active+undersized+degraded
             16 active+undersized
             16 active+clean+remapped
             1  undersized+degraded+remapped+backfilling+peered
 
  io:
    recovery: 20 MiB/s, 9 objects/s
```
```bash
sudo ceph pg stat
193 pgs: 1 undersized+degraded+remapped+backfilling+peered, 17 active+undersized+degraded, 19 active+clean, 16 active+clean+remapped, 79 undersized+degraded+remapped+backfill_wait+peered, 16 active+undersized, 45 active+undersized+degraded+remapped+backfill_wait; 720 GiB data, 1.2 TiB used, 12 TiB / 13 TiB avail; 565566/1106208 objects degraded (51.127%); 287729/1106208 objects misplaced (26.010%); 13 MiB/s, 6 objects/s recovering
```
```bash
sudo ceph osd perf
osd  commit_latency(ms)  apply_latency(ms)
 11                   0                  0
 10                   0                  0
  9                   0                  0
  8                   0                  0
  7                   0                  0
  6                   0                  0
  1                   1                  1
  0                   1                  1
  2                   0                  0
  3                   0                  0
  4                   0                  0
  5                   0                  0
```
```bash
sudo ceph osd pool stats
pool device_health_metrics id 1
  nothing is going on

pool cephfs.test-fs-1.meta id 4
  60/381 objects degraded (15.748%)

pool cephfs.test-fs-1.data id 5
  564150/1105827 objects degraded (51.016%)
  287729/1105827 objects misplaced (26.019%)
  recovery io 13 MiB/s, 6 objects/s
```
## taking out 3rd osd on sff-205
```bash
sudo ceph osd df
ID  CLASS  WEIGHT   REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS
 0    lff  2.72899   1.00000  2.7 TiB   53 GiB   52 GiB  242 MiB   782 MiB  2.7 TiB   1.88  0.19   59      up
 1    lff  2.72899   1.00000  2.7 TiB   53 GiB   52 GiB   82 MiB   942 MiB  2.7 TiB   1.90  0.19   55      up
 2    hdd  0.81870   1.00000  838 GiB   80 GiB   79 GiB   27 MiB   997 MiB  758 GiB   9.56  0.97   20      up
 3    hdd  0.81870   1.00000  838 GiB  195 GiB  194 GiB   50 MiB   974 MiB  643 GiB  23.28  2.37    0    down
 4    hdd  0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down
 5    hdd  0.81870   1.00000  838 GiB   68 GiB   67 GiB   28 MiB   996 MiB  770 GiB   8.16  0.83   20      up
 6    hdd  0.81870   1.00000  838 GiB   91 GiB   90 GiB   17 MiB  1007 MiB  747 GiB  10.84  1.10   25      up
 7    hdd  0.81870   1.00000  838 GiB  125 GiB  124 GiB   38 MiB   986 MiB  713 GiB  14.89  1.52   24      up
 8    hdd  0.81870   1.00000  838 GiB  173 GiB  172 GiB   41 MiB   983 MiB  666 GiB  20.58  2.09   39      up
 9    hdd  0.81870   1.00000  838 GiB   24 GiB   23 GiB   56 MiB   968 MiB  815 GiB   2.84  0.29    0    down
10    hdd  0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  2.20   38      up
11    hdd  0.81870   1.00000  838 GiB  248 GiB  247 GiB   27 MiB   997 MiB  591 GiB  29.56  3.01   52      up
                       TOTAL   13 TiB  1.3 TiB  1.2 TiB  637 MiB    10 GiB   12 TiB   9.83                   
MIN/MAX VAR: 0.19/3.01  STDDEV: 9.68
```
```bash
sudo ceph health detail
HEALTH_WARN 3 failed cephadm daemon(s); failed to probe daemons or devices; 2 osds down; Reduced data availability: 83 pgs inactive; Degraded data redundancy: 550551/1106208 objects degraded (49.769%), 146 pgs degraded, 127 pgs undersized
[WRN] CEPHADM_FAILED_DAEMON: 3 failed cephadm daemon(s)
    daemon prometheus.sff-203 on sff-203 is in error state
    daemon osd.4 on sff-203 is in error state
    daemon crash.sff-205 on sff-205 is in error state
[WRN] CEPHADM_REFRESH_FAILED: failed to probe daemons or devices
    host sff-205 `cephadm ceph-volume` failed: cephadm exited with an error code: 1, stderr:Non-zero exit code 125 from /usr/bin/docker run --rm --ipc=host --net=host --entrypoint stat -e CONTAINER_IMAGE=docker.io/ceph/ceph:v15 -e NODE_NAME=sff-205 docker.io/ceph/ceph:v15 -c %u %g /var/lib/ceph
stat: stderr Unable to find image 'ceph/ceph:v15' locally
stat: stderr v15: Pulling from ceph/ceph
stat: stderr 7a0437f04f83: Pulling fs layer
stat: stderr 731c3beff4de: Pulling fs layer
stat: stderr docker: error parsing HTTP 403 response body: invalid character '<' looking for beginning of value: "<html><body><h1>403 Forbidden</h1>\nSince Docker is a US company, we must comply with US export control regulations. In an effort to comply with these, we now block all IP addresses that are located in Cuba, Iran, North Korea, Republic of Crimea, Sudan, and Syria. If you are not in one of these cities, countries, or regions and are blocked, please reach out to https://hub.docker.com/support/contact/\n</body></html>\n".
stat: stderr See 'docker run --help'.
Traceback (most recent call last):
  File "<stdin>", line 6224, in <module>
  File "<stdin>", line 1340, in _infer_fsid
  File "<stdin>", line 1423, in _infer_image
  File "<stdin>", line 3655, in command_ceph_volume
  File "<stdin>", line 1521, in make_log_dir
  File "<stdin>", line 2134, in extract_uid_gid
RuntimeError: uid/gid not found
    host sff-203 `cephadm ceph-volume` failed: cephadm exited with an error code: 1, stderr:Non-zero exit code 125 from /usr/bin/docker run --rm --ipc=host --net=host --entrypoint stat -e CONTAINER_IMAGE=docker.io/ceph/ceph:v15 -e NODE_NAME=sff-203 docker.io/ceph/ceph:v15 -c %u %g /var/lib/ceph
stat: stderr Unable to find image 'ceph/ceph:v15' locally
stat: stderr v15: Pulling from ceph/ceph
stat: stderr 7a0437f04f83: Pulling fs layer
stat: stderr 731c3beff4de: Pulling fs layer
stat: stderr docker: Head https://registry-1.docker.io/v2/ceph/ceph/manifests/v15: Get https://auth.docker.io/token?scope=repository%3Aceph%2Fceph%3Apull&service=registry.docker.io: net/http: request canceled (Client.Timeout exceeded while awaiting headers).
stat: stderr See 'docker run --help'.
Traceback (most recent call last):
  File "<stdin>", line 6224, in <module>
  File "<stdin>", line 1340, in _infer_fsid
  File "<stdin>", line 1423, in _infer_image
  File "<stdin>", line 3655, in command_ceph_volume
  File "<stdin>", line 1521, in make_log_dir
  File "<stdin>", line 2134, in extract_uid_gid
RuntimeError: uid/gid not found
[WRN] OSD_DOWN: 2 osds down
    osd.3 (root=default,host=sff-203) is down
    osd.9 (root=default,host=sff-205) is down
[WRN] PG_AVAILABILITY: Reduced data availability: 83 pgs inactive
    pg 5.0 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.3 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.4 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.5 is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.9 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.a is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.c is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.d is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.e is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.f is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.11 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.12 is stuck inactive for 2h, current state undersized+degraded+remapped+backfilling+peered, last acting [11]
    pg 5.13 is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.14 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.15 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.17 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.18 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.1b is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1f is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.20 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.21 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.23 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.24 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.25 is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.29 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.2a is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.2c is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.2d is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.2e is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.2f is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.31 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.32 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.33 is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.65 is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.69 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.6a is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.6c is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.6d is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.6e is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.6f is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.71 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.72 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.73 is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.74 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.75 is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.77 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.78 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.79 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.7b is stuck inactive for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.7f is stuck inactive for 7m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
[WRN] PG_DEGRADED: Degraded data redundancy: 550551/1106208 objects degraded (49.769%), 146 pgs degraded, 127 pgs undersized
    pg 4.7 is stuck undersized for 7m, current state active+undersized+degraded, last acting [0,10]
    pg 4.8 is undersized+degraded+peered, acting [1]
    pg 4.9 is stuck undersized for 7m, current state active+undersized+degraded+remapped+backfill_wait, last acting [0,11]
    pg 4.b is stuck undersized for 7m, current state active+undersized+degraded, last acting [8,1]
    pg 4.c is active+undersized+degraded, acting [1,5]
    pg 4.d is stuck undersized for 7m, current state active+undersized+degraded, last acting [10,0]
    pg 5.1 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.4 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.6 is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.7 is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [7,5]
    pg 5.8 is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [2,8]
    pg 5.9 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.a is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.b is active+undersized+degraded+remapped+backfill_wait, acting [5,8]
    pg 5.c is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.d is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.f is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.65 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.66 is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.67 is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [7,5]
    pg 5.68 is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [2,8]
    pg 5.69 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.6a is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.6b is active+undersized+degraded+remapped+backfill_wait, acting [5,8]
    pg 5.6c is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.6d is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.6e is undersized+degraded+remapped+backfill_wait+peered, acting [5]
    pg 5.6f is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.70 is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [11,6]
    pg 5.71 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.72 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.73 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.74 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.75 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [8]
    pg 5.76 is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,11]
    pg 5.77 is undersized+degraded+remapped+backfill_wait+peered, acting [8]
    pg 5.78 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.79 is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.7a is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [8,0]
    pg 5.7b is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.7c is stuck undersized for 6m, current state active+undersized+degraded+remapped+backfill_wait, last acting [11,2]
    pg 5.7d is stuck undersized for 6m, current state active+undersized+degraded, last acting [8,1]
    pg 5.7e is active+undersized+degraded+remapped+backfill_wait, acting [6,10]
    pg 5.7f is stuck undersized for 6m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 6.2 is stuck undersized for 17m, current state active+undersized, last acting [0,1]
    pg 6.3 is stuck undersized for 17m, current state active+undersized, last acting [1,0]
    pg 6.5 is stuck undersized for 7m, current state active+undersized, last acting [0,1]
    pg 6.9 is stuck undersized for 7m, current state active+undersized, last acting [0,1]
    pg 6.a is stuck undersized for 17m, current state active+undersized, last acting [0,1]
    pg 6.c is stuck undersized for 17m, current state active+undersized, last acting [1,0]
    pg 6.f is stuck undersized for 17m, current state active+undersized, last acting [1,0]
```
```bash
sudo ceph osd tree
ID  CLASS  WEIGHT    TYPE NAME         STATUS  REWEIGHT  PRI-AFF
-1         13.64493  root default                               
-3          2.72899      host lff-204                           
 0    lff   2.72899          osd.0         up   1.00000  1.00000
-5          2.72899      host lff-206                           
 1    lff   2.72899          osd.1         up   1.00000  1.00000
-7          4.09348      host sff-203                           
 2    hdd   0.81870          osd.2         up   1.00000  1.00000
 3    hdd   0.81870          osd.3       down   1.00000  1.00000
 4    hdd   0.81870          osd.4       down         0  1.00000
 5    hdd   0.81870          osd.5         up   1.00000  1.00000
 6    hdd   0.81870          osd.6         up   1.00000  1.00000
-9          4.09348      host sff-205                           
 7    hdd   0.81870          osd.7         up   1.00000  1.00000
 8    hdd   0.81870          osd.8         up   1.00000  1.00000
 9    hdd   0.81870          osd.9       down   1.00000  1.00000
10    hdd   0.81870          osd.10        up   1.00000  1.00000
11    hdd   0.81870          osd.11        up   1.00000  1.00000
```
```bash
sudo ceph osd df plain
ID  CLASS  WEIGHT   REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS
 0    lff  2.72899   1.00000  2.7 TiB   53 GiB   52 GiB  242 MiB   782 MiB  2.7 TiB   1.88  0.19   59      up
 1    lff  2.72899   1.00000  2.7 TiB   54 GiB   53 GiB   82 MiB   942 MiB  2.7 TiB   1.93  0.20   55      up
 2    hdd  0.81870   1.00000  838 GiB   80 GiB   79 GiB   27 MiB   997 MiB  758 GiB   9.56  0.97   20      up
 3    hdd  0.81870   1.00000  838 GiB  195 GiB  194 GiB   50 MiB   974 MiB  643 GiB  23.28  2.37    0    down
 4    hdd  0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down
 5    hdd  0.81870   1.00000  838 GiB   68 GiB   67 GiB   28 MiB   996 MiB  770 GiB   8.16  0.83   20      up
 6    hdd  0.81870   1.00000  838 GiB   91 GiB   90 GiB   17 MiB  1007 MiB  747 GiB  10.84  1.10   25      up
 7    hdd  0.81870   1.00000  838 GiB  125 GiB  124 GiB   38 MiB   986 MiB  713 GiB  14.89  1.51   24      up
 8    hdd  0.81870   1.00000  838 GiB  173 GiB  172 GiB   41 MiB   983 MiB  666 GiB  20.58  2.09   39      up
 9    hdd  0.81870   1.00000  838 GiB   24 GiB   23 GiB   56 MiB   968 MiB  815 GiB   2.84  0.29    0    down
10    hdd  0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  2.20   38      up
11    hdd  0.81870   1.00000  838 GiB  248 GiB  247 GiB   27 MiB   997 MiB  591 GiB  29.56  3.01   52      up
                       TOTAL   13 TiB  1.3 TiB  1.3 TiB  637 MiB    10 GiB   12 TiB   9.83                   
MIN/MAX VAR: 0.19/3.01  STDDEV: 9.67
```
```bash
sudo ceph pg stat
193 pgs: 1 undersized+degraded+remapped+backfilling+peered, 2 undersized+degraded+peered, 20 active+undersized+degraded, 15 active+clean, 16 active+clean+remapped, 82 undersized+degraded+remapped+backfill_wait+peered, 16 active+undersized, 41 active+undersized+degraded+remapped+backfill_wait; 720 GiB data, 1.3 TiB used, 12 TiB / 13 TiB avail; 550068/1106208 objects degraded (49.726%); 310811/1106208 objects misplaced (28.097%); 13 MiB/s, 6 objects/s recovering
```
```bash
sudo ceph fs status
test-fs-1 - 1 clients
=========
RANK  STATE             MDS                ACTIVITY     DNS    INOS  
 0    active  test-fs-1.sff-205.bziwst  Reqs:    0 /s   193k   193k  
         POOL            TYPE     USED  AVAIL  
cephfs.test-fs-1.meta  metadata  1184M  3990G  
cephfs.test-fs-1.data    data    1608G  6055G  
      STANDBY MDS         
test-fs-1.sff-203.etgjnp  
MDS version: ceph version 15.2.13 (c44bc49e7a57a87d84dfff2a077a2058aa2172e2) octopus (stable)
```
```bash
sudo ceph osd df
ID  CLASS  WEIGHT   REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS
 0    lff  2.72899   1.00000  2.7 TiB   53 GiB   52 GiB  242 MiB   782 MiB  2.7 TiB   1.88  0.21   59      up
 1    lff  2.72899   1.00000  2.7 TiB   56 GiB   55 GiB   82 MiB   942 MiB  2.7 TiB   2.01  0.22   55      up
 2    hdd  0.81870   1.00000  838 GiB   80 GiB   79 GiB   27 MiB   997 MiB  758 GiB   9.56  1.07   22      up
 3    hdd  0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down
 4    hdd  0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down
 5    hdd  0.81870   1.00000  838 GiB   68 GiB   67 GiB   28 MiB   996 MiB  770 GiB   8.16  0.91   21      up
 6    hdd  0.81870   1.00000  838 GiB   91 GiB   90 GiB   17 MiB  1007 MiB  747 GiB  10.90  1.22   25      up
 7    hdd  0.81870   1.00000  838 GiB  125 GiB  124 GiB   38 MiB   986 MiB  713 GiB  14.89  1.67   24      up
 8    hdd  0.81870   1.00000  838 GiB  173 GiB  172 GiB   41 MiB   983 MiB  666 GiB  20.58  2.30   39      up
 9    hdd  0.81870   1.00000  838 GiB   24 GiB   23 GiB   56 MiB   968 MiB  815 GiB   2.84  0.32    0    down
10    hdd  0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  2.42   38      up
11    hdd  0.81870   1.00000  838 GiB  248 GiB  247 GiB   27 MiB   997 MiB  591 GiB  29.56  3.31   52      up
                       TOTAL   12 TiB  1.1 TiB  1.1 TiB  587 MiB   9.4 GiB   11 TiB   8.94                   
MIN/MAX VAR: 0.21/3.31  STDDEV: 9.47
```
```bash
sudo ceph osd tree
ID  CLASS  WEIGHT    TYPE NAME         STATUS  REWEIGHT  PRI-AFF
-1         13.64493  root default                               
-3          2.72899      host lff-204                           
 0    lff   2.72899          osd.0         up   1.00000  1.00000
-5          2.72899      host lff-206                           
 1    lff   2.72899          osd.1         up   1.00000  1.00000
-7          4.09348      host sff-203                           
 2    hdd   0.81870          osd.2         up   1.00000  1.00000
 3    hdd   0.81870          osd.3       down         0  1.00000
 4    hdd   0.81870          osd.4       down         0  1.00000
 5    hdd   0.81870          osd.5         up   1.00000  1.00000
 6    hdd   0.81870          osd.6         up   1.00000  1.00000
-9          4.09348      host sff-205                           
 7    hdd   0.81870          osd.7         up   1.00000  1.00000
 8    hdd   0.81870          osd.8         up   1.00000  1.00000
 9    hdd   0.81870          osd.9       down   1.00000  1.00000
10    hdd   0.81870          osd.10        up   1.00000  1.00000
11    hdd   0.81870          osd.11        up   1.00000  1.00000
```
```bash
sudo ceph orch ls
NAME           RUNNING  REFRESHED  AGE  PLACEMENT                                IMAGE NAME                            IMAGE ID      
alertmanager       1/1  2m ago     23h  sff-203;count:1                          docker.io/prom/alertmanager:v0.20.0   <unknown>     
crash              2/4  2m ago     2d   *                                        docker.io/ceph/ceph:v15               2cf504fded39  
grafana            1/1  2m ago     18h  sff-203;count:1                          docker.io/ceph/ceph-grafana:6.7.4     <unknown>     
mds.test-fs-1      2/2  2m ago     22h  sff-203;sff-205;count:2                  docker.io/ceph/ceph:v15               <unknown>     
mgr                2/3  2m ago     23h  sff-203;sff-205;count:3                  docker.io/ceph/ceph:v15               <unknown>     
mon                3/4  2m ago     76m  sff-203;sff-205;lff-204;lff-206;count:4  docker.io/ceph/ceph:v15               mix           
node-exporter      4/4  2m ago     2d   *                                        docker.io/prom/node-exporter:v0.18.1  mix           
osd.None           9/0  2m ago     -    <unmanaged>                              docker.io/ceph/ceph:v15               mix           
prometheus         0/1  2m ago     18h  sff-203;count:1                          docker.io/prom/prometheus:v2.18.1     de242295e225  
```
```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_WARN
            6 failed cephadm daemon(s)
            failed to probe daemons or devices
            1 osds down
            Reduced data availability: 83 pgs inactive
            Degraded data redundancy: 570455/1106208 objects degraded (51.569%), 145 pgs degraded, 161 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 5m)
    mgr: sff-205.narmtr(active, since 44m), standbys: sff-203.wprkbk
    mds: test-fs-1:1 {0=test-fs-1.sff-205.bziwst=up:active} 1 up:standby
    osd: 12 osds: 9 up (since 5m), 10 in (since 2m); 154 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 368.74k objects, 720 GiB
    usage:   1.1 TiB used, 11 TiB / 12 TiB avail
    pgs:     43.005% pgs not active
             570455/1106208 objects degraded (51.569%)
             276507/1106208 objects misplaced (24.996%)
             82 undersized+degraded+remapped+backfill_wait+peered
             53 active+undersized+degraded+remapped+backfill_wait
             16 active+undersized
             16 active+clean+remapped
             16 active+clean
             7  active+undersized+degraded
             2  active+recovery_wait+undersized+degraded+remapped
             1  undersized+degraded+remapped+backfilling+peered
 
  io:
    client:   682 KiB/s rd, 255 B/s wr, 1 op/s rd, 0 op/s wr
    recovery: 20 MiB/s, 9 objects/s
 

2021-06-30T12:02:34.568506+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 570455/1106208 objects degraded (51.569%), 145 pgs degraded, 161 pgs undersized (PG_DEGRADED)
2021-06-30T12:02:39.607008+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 570375/1106208 objects degraded (51.561%), 145 pgs degraded, 161 pgs undersized (PG_DEGRADED)
2021-06-30T12:02:44.616126+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 570295/1106208 objects degraded (51.554%), 145 pgs degraded, 161 pgs undersized (PG_DEGRADED)
2021-06-30T12:02:49.624704+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 570215/1106208 objects degraded (51.547%), 145 pgs degraded, 161 pgs undersized (PG_DEGRADED)
2021-06-30T12:02:54.626022+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 570141/1106208 objects degraded (51.540%), 145 pgs degraded, 161 pgs undersized (PG_DEGRADED)
2021-06-30T12:02:59.635501+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 570061/1106208 objects degraded (51.533%), 145 pgs degraded, 161 pgs undersized (PG_DEGRADED)
```
```bash
sudo ceph osd df tree
ID  CLASS  WEIGHT    REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS  TYPE NAME       
-1         13.64493         -   12 TiB  1.1 TiB  1.1 TiB  587 MiB   9.4 GiB   11 TiB   8.97  1.00    -          root default    
-3          2.72899         -  2.7 TiB   53 GiB   52 GiB  242 MiB   782 MiB  2.7 TiB   1.88  0.21    -              host lff-204
 0    lff   2.72899   1.00000  2.7 TiB   53 GiB   52 GiB  242 MiB   782 MiB  2.7 TiB   1.88  0.21   59      up          osd.0   
-5          2.72899         -  2.7 TiB   58 GiB   57 GiB   82 MiB   942 MiB  2.7 TiB   2.09  0.23    -              host lff-206
 1    lff   2.72899   1.00000  2.7 TiB   58 GiB   57 GiB   82 MiB   942 MiB  2.7 TiB   2.09  0.23   55      up          osd.1   
-7          4.09348         -  2.5 TiB  242 GiB  239 GiB   72 MiB   2.9 GiB  2.2 TiB   9.63  1.07    -              host sff-203
 2    hdd   0.81870   1.00000  838 GiB   80 GiB   79 GiB   27 MiB   997 MiB  758 GiB   9.56  1.07   22      up          osd.2   
 3    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.3   
 4    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.4   
 5    hdd   0.81870   1.00000  838 GiB   68 GiB   67 GiB   28 MiB   996 MiB  770 GiB   8.16  0.91   21      up          osd.5   
 6    hdd   0.81870   1.00000  838 GiB   94 GiB   93 GiB   17 MiB  1007 MiB  745 GiB  11.16  1.24   25      up          osd.6   
-9          4.09348         -  4.1 TiB  750 GiB  745 GiB  191 MiB   4.8 GiB  3.4 TiB  17.90  1.99    -              host sff-205
 7    hdd   0.81870   1.00000  838 GiB  125 GiB  124 GiB   38 MiB   986 MiB  713 GiB  14.89  1.66   24      up          osd.7   
 8    hdd   0.81870   1.00000  838 GiB  173 GiB  172 GiB   41 MiB   983 MiB  666 GiB  20.58  2.29   39      up          osd.8   
 9    hdd   0.81870   1.00000  838 GiB   24 GiB   23 GiB   56 MiB   968 MiB  815 GiB   2.84  0.32    0    down          osd.9   
10    hdd   0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  2.41   38      up          osd.10  
11    hdd   0.81870   1.00000  838 GiB  248 GiB  247 GiB   27 MiB   997 MiB  591 GiB  29.56  3.29   52      up          osd.11  
                        TOTAL   12 TiB  1.1 TiB  1.1 TiB  587 MiB   9.4 GiB   11 TiB   8.97                                     
MIN/MAX VAR: 0.21/3.29  STDDEV: 9.46
```
```bash
...
...
...

112751  125511  202402  215163  227924  305243  318003  330764  343524  405562  418322  49168   511927  525445  608701  622723  636746  713121  809019  823041  852442  866465  909523  923545  953234
112752  125512  202403  215164  227925  305244  318004  330765  343525  405563  418323  49169   511928  525446  608702  622724  636747  713122  809020  823042  852443  866466  909524  923546  953235
112753  125513  202404  215165  227926  305245  318005  330766  343526  405564  418324  4917    511929  525447  608703  622725  636748  713123  809021  823043  852444  866467  909525  923547  953236
112754  125514  202405  215166  227927  305246  318006  330767  343527  405565  418325  49170   51193   525448  608704  622726  636749  713124  809022  823044  852445  866468  909526  923548  953237
112755  125515  202406  215167  227928  305247  318007  330768  343528  405566  418326  49171   511930  525449  608705  622727  636750  713125  809023  823045  852446  866469  909527  923549  953238
112756  125516  202407  215168  227929  305248  318008  330769  343529  405567  418327  49172   511931  525450  608706  622728  636751  713126  809024  823046  852447  866470  909528  923550  953239
112757  125517  202408  215169  22793   305249  318009  33077   34353   405568  418328  49173   511932  525451  608707  622729  636752  713127  809025  823047  852448  866471  909529  923551  953240

real	4m36.912s
user	0m6.868s
sys	0m30.962s
```
## taking out 4th osd on sff-205
```bash
sudo ceph osd df tree
ID  CLASS  WEIGHT    REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS  TYPE NAME       
-1         13.64493         -   11 TiB  1.1 TiB  1.1 TiB  531 MiB   8.5 GiB   10 TiB   9.49  1.00    -          root default    
-3          2.72899         -  2.7 TiB   53 GiB   52 GiB  242 MiB   782 MiB  2.7 TiB   1.89  0.20    -              host lff-204
 0    lff   2.72899   1.00000  2.7 TiB   53 GiB   52 GiB  242 MiB   782 MiB  2.7 TiB   1.89  0.20   72      up          osd.0   
-5          2.72899         -  2.7 TiB   62 GiB   61 GiB   82 MiB   942 MiB  2.7 TiB   2.22  0.23    -              host lff-206
 1    lff   2.72899   1.00000  2.7 TiB   62 GiB   61 GiB   82 MiB   942 MiB  2.7 TiB   2.22  0.23   70      up          osd.1   
-7          4.09348         -  2.5 TiB  246 GiB  243 GiB   72 MiB   2.9 GiB  2.2 TiB   9.77  1.03    -              host sff-203
 2    hdd   0.81870   1.00000  838 GiB   81 GiB   80 GiB   27 MiB   997 MiB  758 GiB   9.62  1.01   23      up          osd.2   
 3    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.3   
 4    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.4   
 5    hdd   0.81870   1.00000  838 GiB   68 GiB   67 GiB   28 MiB   996 MiB  770 GiB   8.17  0.86   33      up          osd.5   
 6    hdd   0.81870   1.00000  838 GiB   97 GiB   96 GiB   17 MiB  1007 MiB  742 GiB  11.52  1.21   28      up          osd.6   
-9          4.09348         -  3.3 TiB  727 GiB  723 GiB  135 MiB   3.9 GiB  2.6 TiB  21.67  2.28    -              host sff-205
 7    hdd   0.81870   1.00000  838 GiB  125 GiB  124 GiB   38 MiB   986 MiB  713 GiB  14.89  1.57   24      up          osd.7   
 8    hdd   0.81870   1.00000  838 GiB  173 GiB  172 GiB   41 MiB   983 MiB  666 GiB  20.58  2.17    0    down          osd.8   
 9    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.9   
10    hdd   0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  2.28   38      up          osd.10  
11    hdd   0.81870   1.00000  838 GiB  248 GiB  247 GiB   27 MiB   997 MiB  590 GiB  29.57  3.12   52      up          osd.11  
                        TOTAL   11 TiB  1.1 TiB  1.1 TiB  531 MiB   8.5 GiB   10 TiB   9.49                                     
MIN/MAX VAR: 0.20/3.12  STDDEV: 9.54
```
```bash
sudo ceph health detail
HEALTH_WARN 6 failed cephadm daemon(s); failed to probe daemons or devices; 1 osds down; Reduced data availability: 74 pgs inactive, 12 pgs down; Degraded data redundancy: 558706/1017090 objects degraded (54.932%), 134 pgs degraded, 112 pgs undersized
[WRN] CEPHADM_FAILED_DAEMON: 6 failed cephadm daemon(s)
    daemon crash.sff-203 on sff-203 is in error state
    daemon osd.3 on sff-203 is in error state
    daemon prometheus.sff-203 on sff-203 is in error state
    daemon osd.4 on sff-203 is in error state
    daemon crash.sff-205 on sff-205 is in error state
    daemon osd.9 on sff-205 is in error state
[WRN] CEPHADM_REFRESH_FAILED: failed to probe daemons or devices
    host sff-205 `cephadm ceph-volume` failed: cephadm exited with an error code: 1, stderr:Non-zero exit code 125 from /usr/bin/docker run --rm --ipc=host --net=host --entrypoint stat -e CONTAINER_IMAGE=docker.io/ceph/ceph:v15 -e NODE_NAME=sff-205 docker.io/ceph/ceph:v15 -c %u %g /var/lib/ceph
stat: stderr Unable to find image 'ceph/ceph:v15' locally
stat: stderr v15: Pulling from ceph/ceph
stat: stderr 7a0437f04f83: Pulling fs layer
stat: stderr 731c3beff4de: Pulling fs layer
stat: stderr docker: error parsing HTTP 403 response body: invalid character '<' looking for beginning of value: "<html><body><h1>403 Forbidden</h1>\nSince Docker is a US company, we must comply with US export control regulations. In an effort to comply with these, we now block all IP addresses that are located in Cuba, Iran, North Korea, Republic of Crimea, Sudan, and Syria. If you are not in one of these cities, countries, or regions and are blocked, please reach out to https://hub.docker.com/support/contact/\n</body></html>\n".
stat: stderr See 'docker run --help'.
Traceback (most recent call last):
  File "<stdin>", line 6224, in <module>
  File "<stdin>", line 1340, in _infer_fsid
  File "<stdin>", line 1423, in _infer_image
  File "<stdin>", line 3655, in command_ceph_volume
  File "<stdin>", line 1521, in make_log_dir
  File "<stdin>", line 2134, in extract_uid_gid
RuntimeError: uid/gid not found
    host sff-203 `cephadm ceph-volume` failed: cephadm exited with an error code: 1, stderr:Non-zero exit code 125 from /usr/bin/docker run --rm --ipc=host --net=host --entrypoint stat -e CONTAINER_IMAGE=docker.io/ceph/ceph:v15 -e NODE_NAME=sff-203 docker.io/ceph/ceph:v15 -c %u %g /var/lib/ceph
stat: stderr Unable to find image 'ceph/ceph:v15' locally
stat: stderr v15: Pulling from ceph/ceph
stat: stderr 7a0437f04f83: Pulling fs layer
stat: stderr 731c3beff4de: Pulling fs layer
stat: stderr v15: Pulling from ceph/ceph
stat: stderr 7a0437f04f83: Pulling fs layer
stat: stderr 731c3beff4de: Pulling fs layer
stat: stderr docker: open /data/tmp/GetImageBlob847346250: input/output error.
stat: stderr See 'docker run --help'.
Traceback (most recent call last):
  File "<stdin>", line 6224, in <module>
  File "<stdin>", line 1340, in _infer_fsid
  File "<stdin>", line 1423, in _infer_image
  File "<stdin>", line 3655, in command_ceph_volume
  File "<stdin>", line 1521, in make_log_dir
  File "<stdin>", line 2134, in extract_uid_gid
RuntimeError: uid/gid not found
[WRN] OSD_DOWN: 1 osds down
    osd.8 (root=default,host=sff-205) is down
[WRN] PG_AVAILABILITY: Reduced data availability: 74 pgs inactive, 12 pgs down
    pg 5.0 is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1 is stuck inactive for 28m, current state undersized+degraded+remapped+backfilling+peered, last acting [11]
    pg 5.3 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.4 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.5 is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.a is down, acting [0,1,5]
    pg 5.b is stuck inactive for 85s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.c is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.d is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.e is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.f is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.11 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.12 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.13 is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.14 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.15 is down, acting [1,0,5]
    pg 5.17 is down, acting [0,5,1]
    pg 5.18 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.1b is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1f is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.20 is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.21 is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.23 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.24 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.25 is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.29 is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.2a is down, acting [0,1,5]
    pg 5.2b is stuck inactive for 85s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.2c is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.2d is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.2e is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.2f is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.31 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.65 is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.69 is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.6a is down, acting [0,1,5]
    pg 5.6b is stuck inactive for 85s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.6c is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.6d is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.6e is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.6f is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.71 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.72 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.73 is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.74 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.75 is down, acting [1,0,5]
    pg 5.77 is down, acting [0,5,1]
    pg 5.78 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.79 is stuck inactive for 2h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.7b is stuck inactive for 28m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.7f is stuck inactive for 18m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
[WRN] PG_DEGRADED: Degraded data redundancy: 558706/1017090 objects degraded (54.932%), 134 pgs degraded, 112 pgs undersized
    pg 4.1 is stuck undersized for 8m, current state active+undersized+degraded+remapped+backfill_wait, last acting [11,1]
    pg 4.2 is active+undersized+degraded+remapped+backfill_wait, acting [1,6]
    pg 4.7 is stuck undersized for 8m, current state active+recovery_wait+undersized+degraded+remapped, last acting [0,10]
    pg 4.8 is active+recovery_wait+undersized+degraded+remapped, acting [2,1]
    pg 4.9 is stuck undersized for 18m, current state active+undersized+degraded+remapped+backfill_wait, last acting [0,11]
    pg 4.b is active+undersized+degraded, acting [1,2]
    pg 4.c is active+undersized+degraded+remapped+backfill_wait, acting [1,5]
    pg 4.d is stuck undersized for 8m, current state active+undersized+degraded+remapped+backfill_wait, last acting [0,10]
    pg 4.e is active+undersized+degraded, acting [1,0]
    pg 5.0 is stuck undersized for 8m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1 is stuck undersized for 17m, current state undersized+degraded+remapped+backfilling+peered, last acting [11]
    pg 5.3 is stuck undersized for 79s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.4 is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.6 is stuck undersized for 17m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.7 is stuck undersized for 8m, current state active+undersized+degraded+remapped+backfill_wait, last acting [7,5]
    pg 5.8 is undersized+degraded+remapped+backfill_wait+peered, acting [2]
    pg 5.b is undersized+degraded+remapped+backfill_wait+peered, acting [5]
    pg 5.c is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.d is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.f is stuck undersized for 8m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.65 is stuck undersized for 79s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.66 is stuck undersized for 17m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.67 is stuck undersized for 8m, current state active+undersized+degraded+remapped+backfill_wait, last acting [7,5]
    pg 5.68 is undersized+degraded+remapped+backfill_wait+peered, acting [2]
    pg 5.69 is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.6b is undersized+degraded+remapped+backfill_wait+peered, acting [5]
    pg 5.6c is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.6d is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.6e is stuck undersized for 79s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.6f is stuck undersized for 8m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.70 is stuck undersized for 17m, current state active+undersized+degraded+remapped+backfill_wait, last acting [11,6]
    pg 5.71 is undersized+degraded+remapped+backfill_wait+peered, acting [10]
    pg 5.72 is stuck undersized for 8m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.73 is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.74 is undersized+degraded+remapped+backfill_wait+peered, acting [11]
    pg 5.76 is stuck undersized for 17m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,11]
    pg 5.78 is stuck undersized for 79s, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 5.79 is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.7a is undersized+degraded+remapped+backfill_wait+peered, acting [0]
    pg 5.7b is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.7c is stuck undersized for 8m, current state active+undersized+degraded+remapped+backfill_wait, last acting [11,2]
    pg 5.7d is undersized+degraded+remapped+backfill_wait+peered, acting [1]
    pg 5.7e is stuck undersized for 79s, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.7f is stuck undersized for 17m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [11]
    pg 6.2 is stuck undersized for 28m, current state active+undersized, last acting [0,1]
    pg 6.3 is stuck undersized for 28m, current state active+undersized, last acting [1,0]
    pg 6.5 is stuck undersized for 18m, current state active+undersized, last acting [0,1]
    pg 6.9 is stuck undersized for 18m, current state active+undersized, last acting [0,1]
    pg 6.a is stuck undersized for 28m, current state active+undersized, last acting [0,1]
    pg 6.c is stuck undersized for 28m, current state active+undersized, last acting [1,0]
    pg 6.f is stuck undersized for 28m, current state active+undersized, last acting [1,0]
```
```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_WARN
            6 failed cephadm daemon(s)
            failed to probe daemons or devices
            1 osds down
            Reduced data availability: 98 pgs inactive, 12 pgs down
            Degraded data redundancy: 556531/1017090 objects degraded (54.718%), 134 pgs degraded, 153 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 2m)
    mgr: sff-205.narmtr(active, since 52m), standbys: sff-203.wprkbk
    mds: test-fs-1:1 {0=test-fs-1.sff-205.bziwst=up:active} 1 up:standby
    osd: 12 osds: 8 up (since 2m), 9 in (since 3m); 139 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 339.03k objects, 662 GiB
    usage:   1.1 TiB used, 10 TiB / 11 TiB avail
    pgs:     50.777% pgs not active
             556531/1017090 objects degraded (54.718%)
             217824/1017090 objects misplaced (21.416%)
             84 undersized+degraded+remapped+backfill_wait+peered
             37 active+undersized+degraded+remapped+backfill_wait
             19 active+undersized
             14 active+clean
             14 active+clean+remapped
             12 down
             9  active+undersized+degraded
             2  active+recovery_wait+undersized+degraded+remapped
             2  undersized+degraded+remapped+backfilling+peered
 
  io:
    recovery: 37 MiB/s, 18 objects/s
 

2021-06-30T12:10:03.267493+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 557120/1017090 objects degraded (54.776%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
2021-06-30T12:10:08.268900+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 556704/1017090 objects degraded (54.735%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
2021-06-30T12:10:14.496815+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 556453/1017090 objects degraded (54.710%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
2021-06-30T12:10:20.923413+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 556280/1017090 objects degraded (54.693%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
2021-06-30T12:10:26.101670+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 556075/1017090 objects degraded (54.673%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
2021-06-30T12:10:32.190700+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 556029/1017090 objects degraded (54.669%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
2021-06-30T12:10:38.406197+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 556075/1017090 objects degraded (54.673%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
2021-06-30T12:10:43.407091+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 555670/1017090 objects degraded (54.633%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
2021-06-30T12:10:48.451786+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 555614/1017090 objects degraded (54.628%), 134 pgs degraded, 153 pgs undersized (PG_DEGRADED)
```
```bash
sudo ceph orch ls
NAME           RUNNING  REFRESHED  AGE  PLACEMENT                                IMAGE NAME                            IMAGE ID      
alertmanager       1/1  67s ago    23h  sff-203;count:1                          docker.io/prom/alertmanager:v0.20.0   <unknown>     
crash              2/4  67s ago    2d   *                                        docker.io/ceph/ceph:v15               2cf504fded39  
grafana            1/1  67s ago    18h  sff-203;count:1                          docker.io/ceph/ceph-grafana:6.7.4     <unknown>     
mds.test-fs-1      2/2  67s ago    22h  sff-203;sff-205;count:2                  docker.io/ceph/ceph:v15               <unknown>     
mgr                2/3  67s ago    23h  sff-203;sff-205;count:3                  docker.io/ceph/ceph:v15               <unknown>     
mon                3/4  67s ago    90m  sff-203;sff-205;lff-204;lff-206;count:4  docker.io/ceph/ceph:v15               mix           
node-exporter      4/4  67s ago    2d   *                                        docker.io/prom/node-exporter:v0.18.1  mix           
osd.None           8/0  67s ago    -    <unmanaged>                              docker.io/ceph/ceph:v15               mix           
prometheus         0/1  67s ago    18h  sff-203;count:1                          docker.io/prom/prometheus:v2.18.1     de242295e225  
```
```bash
sudo ceph osd df tree
ID  CLASS  WEIGHT    REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS  TYPE NAME       
-1         13.64493         -   11 TiB  1.1 TiB  1.1 TiB  531 MiB   8.5 GiB   10 TiB   9.75  1.00    -          root default    
-3          2.72899         -  2.7 TiB   60 GiB   59 GiB  242 MiB   782 MiB  2.7 TiB   2.15  0.22    -              host lff-204
 0    lff   2.72899   1.00000  2.7 TiB   60 GiB   59 GiB  242 MiB   782 MiB  2.7 TiB   2.15  0.22   73      up          osd.0   
-5          2.72899         -  2.7 TiB   69 GiB   68 GiB   82 MiB   942 MiB  2.7 TiB   2.48  0.25    -              host lff-206
 1    lff   2.72899   1.00000  2.7 TiB   69 GiB   68 GiB   82 MiB   942 MiB  2.7 TiB   2.48  0.25   71      up          osd.1   
-7          4.09348         -  2.5 TiB  254 GiB  251 GiB   72 MiB   2.9 GiB  2.2 TiB  10.12  1.04    -              host sff-203
 2    hdd   0.81870   1.00000  838 GiB   81 GiB   80 GiB   27 MiB   997 MiB  758 GiB   9.62  0.99   23      up          osd.2   
 3    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.3   
 4    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.4   
 5    hdd   0.81870   1.00000  838 GiB   77 GiB   76 GiB   28 MiB   996 MiB  761 GiB   9.20  0.94   34      up          osd.5   
 6    hdd   0.81870   1.00000  838 GiB   97 GiB   96 GiB   17 MiB  1007 MiB  742 GiB  11.52  1.18   28      up          osd.6   
-9          4.09348         -  3.3 TiB  734 GiB  730 GiB  135 MiB   3.9 GiB  2.6 TiB  21.88  2.24    -              host sff-205
 7    hdd   0.81870   1.00000  838 GiB  131 GiB  130 GiB   38 MiB   986 MiB  708 GiB  15.57  1.60   25      up          osd.7   
 8    hdd   0.81870   1.00000  838 GiB  173 GiB  172 GiB   41 MiB   983 MiB  666 GiB  20.58  2.11    0    down          osd.8   
 9    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.9   
10    hdd   0.81870   1.00000  838 GiB  181 GiB  180 GiB   29 MiB   995 MiB  657 GiB  21.63  2.22   38      up          osd.10  
11    hdd   0.81870   1.00000  838 GiB  249 GiB  248 GiB   27 MiB   997 MiB  589 GiB  29.75  3.05   51      up          osd.11  
                        TOTAL   11 TiB  1.1 TiB  1.1 TiB  531 MiB   8.5 GiB   10 TiB   9.75                                     
MIN/MAX VAR: 0.22/3.05  STDDEV: 9.46
```
```bash
...
...
...

112717  125478  202369  215129  227890  305209  317970  33073   343490  405528  418289  49133   511893  525407  608664  622686  636708  713084  808983  823003  852404  866427  909486  923507  953197  9974
112718  125479  20237   21513   227891  30521   317971  330730  343491  405529  41829   49134   511894  525408  608665  622687  636709  713085  808984  823004  852405  866428  909487  923508  953198  9975
112719  12548   202370  215130  227892  305210  317972  330731  343492  40553   418290  49135   511895  525409  608666  622688  636710  713086  808985  823005  852406  866429  909488  923509  953199  9976
11272   125480  202371  215131  227893  305211  317973  330732  343493  405530  418291  49136   511896  525410  608667  622689  636711  713087  808986  823006  852407  866430  909489  923510  9532    9977
112720  125481  202372  215132  227894  305212  317974  330733  343494  405531  418292  49137   511897  525411  608668  622690  636712  713088  808987  823007  852408  866431  909490  923511  953200  9978
112721  125482  202373  215133  227895  305213  317975  330734  343495  405532  418293  49138   511898  525412  608669  622691  636713  713089  808988  823008  852409  866432  909491  923512  953201  9979
112722  125483  202374  215134  227896  305214  317976  330735  343496  405533  418294  49139   511899  525413  608670  622692  636714  713090  808989  823009  852410  866433  909492  923513  953202  998
112723  125484  202375  215135  227897  305215  317977  330736  343497  405534  418295  4914    5119    525414  608671  622693  636715  713091  808990  823010  852411  866434  909493  923514  953203  9980
112724  125485  202376  215136  227898  305216  317978  330737  343498  405535  418296  49140   51190   525415  608672  622694  636716  713092  808991  823011  852412  866435  909494  923515  953204  9981
112725  125486  202377  215137  227899  305217  317979  330738  343499  405536  418297  49141   511900  525416  608673  622695  636717  713093  808992  823012  852413  866436  909495  923516  953205  9982
112726  125487  202378  215138  2279    305218  31798   330739  3435    405537  418298  49142   511901  525417  608674  622696  636718  713094  808993  823013  852414  866437  909496  923517  953206  9983
112727  125488  202379  215139  22790   305219  317980  33074   34350   405538  418299  49143   511902  525418  608675  622697  636719  713095  808994  823014  852415  866438  909497  923518  953207  9984
112728  125489  20238   21514   227900  30522   317981  330740  343500  405539  4183    49144   511903  525419  608676  622698  636720  713096  808995  823015  852416  866439  909498  923519  953208  9985
112729  12549   202380  215140  227901  305220  317982  330741  343501  40554   41830   49145   511904  525420  608677  622699  636721  713097  808996  823016  852417  866440  909499  923520  953209  9986
11273   125490  202381  215141  227902  305221  317983  330742  343502  405540  418300  49146   511905  525421  608678  6227    636722  713098  808997  823017  852418  866441  9095    923521  953210  9987
112730  125491  202382  215142  227903  305222  317984  330743  343503  405541  418301  49147   511906  525422  608679  622700  636723  713099  808998  823018  852419  866442  909500  923522  953211  9988
112731  125492  202383  215143  227904  305223  317985  330744  343504  405542  418302  49148   511907  525423  608680  622701  636724  7131    808999  823019  852420  866443  909501  923523  953212  9989
112732  125493  202384  215144  227905  305224  317986  330745  343505  405543  418303  49149   511908  525424  608681  622702  636725  713100  809     823020  852421  866444  909502  923524  953213  999
112733  125494  202385  215145  227906  305225  317987  330746  343506  405544  418304  4915    511909  525425  608682  622703  636726  713101  8090    823021  852422  866445  909503  923525  953214  9990
112734  125495  202386  215146  227907  305226  317988  330747  343507  405545  418305  49150   51191   525426  608683  622704  636727  713102  809000  823022  852423  866446  909504  923526  953215  9991
112735  125496  202387  215147  227908  305227  317989  330748  343508  405546  418306  49151   511910  525427  608684  622705  636728  713103  809001  823023  852424  866447  909505  923527  953216  9992
112736  125497  202388  215148  227909  305228  31799   330749  343509  405547  418307  49152   511911  525428  608685  622706  636729  713104  809002  823024  852425  866448  909506  923528  953217  9993
112737  125498  202389  215149  22791   305229  317990  33075   34351   405548  418308  49153   511912  525429  608686  622707  636730  713105  809003  823025  852426  866449  909507  923529  953218  9994
112738  125499  20239   21515   227910  30523   317991  330750  343510  405549  418309  49154   511913  525430  608687  622708  636731  713106  809004  823026  852427  866450  909508  923530  953219  9995
112739  1255    202390  215150  227911  305230  317992  330751  343511  40555   41831   49155   511914  525431  608688  622709  636732  713107  809005  823027  852428  866451  909509  923531  953220  9996
11274   12550   202391  215151  227912  305231  317993  330752  343512  405550  418310  49156   511915  525432  608689  622710  636733  713108  809006  823028  852429  866452  909510  923532  953221  9997
112740  125500  202392  215152  227913  305232  317994  330753  343513  405551  418311  49157   511916  525433  608690  622711  636734  713109  809007  823029  852430  866453  909511  923533  953222  9998
112741  125501  202393  215153  227914  305233  317995  330754  343514  405552  418312  49158   511917  525434  608691  622712  636735  713110  809008  823030  852431  866454  909512  923534  953223  9999
112742  125502  202394  215154  227915  305234  317996  330755  343515  405553  418313  49159   511918  525435  608692  622713  636736  713111  809009  823031  852432  866455  909513  923535  953224
112743  125503  202395  215155  227916  305235  317997  330756  343516  405554  418314  4916    511919  525436  608693  622714  636737  713112  809010  823032  852433  866456  909514  923536  953225
112744  125504  202396  215156  227917  305236  317998  330757  343517  405555  418315  49160   51192   525437  608694  622715  636738  713113  809011  823033  852434  866457  909515  923537  953226
112745  125505  202397  215157  227918  305237  317999  330758  343518  405556  418316  49161   511920  525438  608695  622716  636739  713114  809012  823034  852435  866458  909516  923538  953227
112746  125506  202398  215158  227919  305238  318     330759  343519  405557  418317  49162   511921  525439  608696  622717  636740  713115  809013  823035  852436  866459  909517  923539  953228
112747  125507  202399  215159  22792   305239  3180    33076   34352   405558  418318  49163   511922  525440  608697  622718  636741  713116  809014  823036  852437  866460  909518  923540  953229
112748  125508  2024    21516   227920  30524   31800   330760  343520  405559  418319  49164   511923  525441  608698  622719  636742  713117  809015  823037  852438  866461  909519  923541  953230
112749  125509  20240   215160  227921  305240  318000  330761  343521  40556   41832   49165   511924  525442  608699  622720  636743  713118  809016  823038  852439  866462  909520  923542  953231
11275   12551   202400  215161  227922  305241  318001  330762  343522  405560  418320  49166   511925  525443  6087    622721  636744  713119  809017  823039  852440  866463  909521  923543  953232
112750  125510  202401  215162  227923  305242  318002  330763  343523  405561  418321  49167   511926  525444  608700  622722  636745  713120  809018  823040  852441  866464  909522  923544  953233
112751  125511  202402  215163  227924  305243  318003  330764  343524  405562  418322  49168   511927  525445  608701  622723  636746  713121  809019  823041  852442  866465  909523  923545  953234
112752  125512  202403  215164  227925  305244  318004  330765  343525  405563  418323  49169   511928  525446  608702  622724  636747  713122  809020  823042  852443  866466  909524  923546  953235
112753  125513  202404  215165  227926  305245  318005  330766  343526  405564  418324  4917    511929  525447  608703  622725  636748  713123  809021  823043  852444  866467  909525  923547  953236
112754  125514  202405  215166  227927  305246  318006  330767  343527  405565  418325  49170   51193   525448  608704  622726  636749  713124  809022  823044  852445  866468  909526  923548  953237
112755  125515  202406  215167  227928  305247  318007  330768  343528  405566  418326  49171   511930  525449  608705  622727  636750  713125  809023  823045  852446  866469  909527  923549  953238
112756  125516  202407  215168  227929  305248  318008  330769  343529  405567  418327  49172   511931  525450  608706  622728  636751  713126  809024  823046  852447  866470  909528  923550  953239
112757  125517  202408  215169  22793   305249  318009  33077   34353   405568  418328  49173   511932  525451  608707  622729  636752  713127  809025  823047  852448  866471  909529  923551  953240

real	5m21.935s
user	0m7.554s
sys	0m32.742s
```
```bash
sudo ceph osd pool stats
pool device_health_metrics id 1
  nothing is going on

pool cephfs.test-fs-1.meta id 4
  115/381 objects degraded (30.184%)

pool cephfs.test-fs-1.data id 5
  537285/1016709 objects degraded (52.846%)
  201204/1016709 objects misplaced (19.790%)
  recovery io 36 MiB/s, 17 objects/s
```
```bash
sudo ceph health
HEALTH_WARN 7 failed cephadm daemon(s); failed to probe daemons or devices; 1/3 mons down, quorum sff-203,sff-205; Reduced data availability: 95 pgs inactive, 12 pgs down; Degraded data redundancy: 536298/1017090 objects degraded (52.729%), 132 pgs degraded, 150 pgs undersized
```
```bash
sudo ceph fs status
test-fs-1 - 1 clients
=========
RANK  STATE             MDS                ACTIVITY     DNS    INOS  
 0    active  test-fs-1.sff-205.bziwst  Reqs:    0 /s   368k   368k  
         POOL            TYPE     USED  AVAIL  
cephfs.test-fs-1.meta  metadata  1222M  4321G  
cephfs.test-fs-1.data    data    1683G  6347G  
      STANDBY MDS         
test-fs-1.sff-203.etgjnp  
MDS version: ceph version 15.2.13 (c44bc49e7a57a87d84dfff2a077a2058aa2172e2) octopus (stable)
```
```bash
sudo ceph osd df tree
ID  CLASS  WEIGHT    REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS  TYPE NAME       
-1         13.64493         -   10 TiB  981 GiB  973 GiB  490 MiB   7.5 GiB  9.4 TiB   9.24  1.00    -          root default    
-3          2.72899         -  2.7 TiB   64 GiB   63 GiB  242 MiB   782 MiB  2.7 TiB   2.29  0.25    -              host lff-204
 0    lff   2.72899   1.00000  2.7 TiB   64 GiB   63 GiB  242 MiB   782 MiB  2.7 TiB   2.29  0.25   74      up          osd.0   
-5          2.72899         -  2.7 TiB   78 GiB   77 GiB   82 MiB   942 MiB  2.7 TiB   2.79  0.30    -              host lff-206
 1    lff   2.72899   1.00000  2.7 TiB   78 GiB   77 GiB   82 MiB   942 MiB  2.7 TiB   2.79  0.30   72      up          osd.1   
-7          4.09348         -  2.5 TiB  267 GiB  264 GiB   72 MiB   2.9 GiB  2.2 TiB  10.60  1.15    -              host sff-203
 2    hdd   0.81870   1.00000  838 GiB   85 GiB   84 GiB   27 MiB   997 MiB  753 GiB  10.18  1.10   23      up          osd.2   
 3    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.3   
 4    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.4   
 5    hdd   0.81870   1.00000  838 GiB   85 GiB   84 GiB   28 MiB   996 MiB  754 GiB  10.09  1.09   35      up          osd.5   
 6    hdd   0.81870   1.00000  838 GiB   97 GiB   96 GiB   17 MiB  1007 MiB  742 GiB  11.52  1.25   28      up          osd.6   
-9          4.09348         -  2.5 TiB  573 GiB  570 GiB   94 MiB   2.9 GiB  1.9 TiB  22.79  2.47    -              host sff-205
 7    hdd   0.81870   1.00000  838 GiB  131 GiB  130 GiB   38 MiB   986 MiB  708 GiB  15.57  1.68   26      up          osd.7   
 8    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.8   
 9    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.9   
10    hdd   0.81870   1.00000  838 GiB  189 GiB  188 GiB   29 MiB   995 MiB  649 GiB  22.58  2.44   38      up          osd.10  
11    hdd   0.81870   1.00000  838 GiB  253 GiB  252 GiB   27 MiB   997 MiB  585 GiB  30.22  3.27   52      up          osd.11  
                        TOTAL   10 TiB  981 GiB  973 GiB  490 MiB   7.5 GiB  9.4 TiB   9.24                                     
MIN/MAX VAR: 0.25/3.27  STDDEV: 9.71
```
```bash
sudo ceph osd df tree
ID  CLASS  WEIGHT    REWEIGHT  SIZE     RAW USE   DATA      OMAP     META      AVAIL    %USE   VAR   PGS  STATUS  TYPE NAME       
-1         13.64493         -   10 TiB  1011 GiB  1003 GiB  490 MiB   7.5 GiB  9.4 TiB   9.52  1.00    -          root default    
-3          2.72899         -  2.7 TiB    69 GiB    68 GiB  242 MiB   782 MiB  2.7 TiB   2.49  0.26    -              host lff-204
 0    lff   2.72899   1.00000  2.7 TiB    69 GiB    68 GiB  242 MiB   782 MiB  2.7 TiB   2.49  0.26   75      up          osd.0   
-5          2.72899         -  2.7 TiB    80 GiB    79 GiB   82 MiB   942 MiB  2.7 TiB   2.85  0.30    -              host lff-206
 1    lff   2.72899   1.00000  2.7 TiB    80 GiB    79 GiB   82 MiB   942 MiB  2.7 TiB   2.85  0.30   73      up          osd.1   
-7          4.09348         -  2.5 TiB   280 GiB   277 GiB   72 MiB   2.9 GiB  2.2 TiB  11.13  1.17    -              host sff-203
 2    hdd   0.81870   1.00000  838 GiB    93 GiB    92 GiB   27 MiB   997 MiB  746 GiB  11.06  1.16   25      up          osd.2   
 3    hdd   0.81870         0      0 B       0 B       0 B      0 B       0 B      0 B      0     0    0    down          osd.3   
 4    hdd   0.81870         0      0 B       0 B       0 B      0 B       0 B      0 B      0     0    0    down          osd.4   
 5    hdd   0.81870   1.00000  838 GiB    91 GiB    90 GiB   28 MiB   996 MiB  748 GiB  10.81  1.14   36      up          osd.5   
 6    hdd   0.81870   1.00000  838 GiB    97 GiB    96 GiB   17 MiB  1007 MiB  742 GiB  11.52  1.21   28      up          osd.6   
-9          4.09348         -  2.5 TiB   582 GiB   579 GiB   94 MiB   2.9 GiB  1.9 TiB  23.13  2.43    -              host sff-205
 7    hdd   0.81870   1.00000  838 GiB   131 GiB   130 GiB   38 MiB   986 MiB  708 GiB  15.57  1.64   26      up          osd.7   
 8    hdd   0.81870         0      0 B       0 B       0 B      0 B       0 B      0 B      0     0    0    down          osd.8   
 9    hdd   0.81870         0      0 B       0 B       0 B      0 B       0 B      0 B      0     0    0    down          osd.9   
10    hdd   0.81870   1.00000  838 GiB   198 GiB   197 GiB   29 MiB   995 MiB  640 GiB  23.60  2.48   39      up          osd.10  
11    hdd   0.81870   1.00000  838 GiB   253 GiB   252 GiB   27 MiB   997 MiB  585 GiB  30.22  3.18   52      up          osd.11  
                        TOTAL   10 TiB  1011 GiB  1003 GiB  490 MiB   7.5 GiB  9.4 TiB   9.52                                     
MIN/MAX VAR: 0.26/3.18  STDDEV: 9.78
```
- > ## **NO ACCESS TO DATA**
- > ## NOT WORKING ANYMORE

```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_ERR
            insufficient standby MDS daemons available
            Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'
            Reduced data availability: 89 pgs inactive, 12 pgs down
            Degraded data redundancy: 507062/1017090 objects degraded (49.854%), 126 pgs degraded, 144 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 2m)
    mgr: sff-203.wprkbk(active, since 11m)
    mds: test-fs-1:1 {0=test-fs-1.sff-203.etgjnp=up:active(laggy or crashed)}
    osd: 12 osds: 8 up (since 37m), 8 in (since 26m); 140 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 339.03k objects, 662 GiB
    usage:   1.0 TiB used, 9.4 TiB / 10 TiB avail
    pgs:     46.114% pgs not active
             507062/1017090 objects degraded (49.854%)
             198622/1017090 objects misplaced (19.528%)
             76 undersized+degraded+remapped+backfill_wait+peered
             46 active+undersized+degraded+remapped+backfill_wait
             23 active+clean
             18 active+undersized
             14 active+clean+remapped
             12 down
             3  active+recovery_wait+undersized+degraded+remapped
             1  undersized+degraded+remapped+backfilling+peered
 
  io:
    recovery: 20 MiB/s, 9 objects/s
 

2021-06-30T12:44:43.662109+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 507062/1017090 objects degraded (49.854%), 126 pgs degraded, 144 pgs undersized (PG_DEGRADED)
2021-06-30T12:44:48.671395+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 507022/1017090 objects degraded (49.850%), 126 pgs degraded, 144 pgs undersized (PG_DEGRADED)
2021-06-30T12:44:53.681626+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 506982/1017090 objects degraded (49.846%), 126 pgs degraded, 144 pgs undersized (PG_DEGRADED)
2021-06-30T12:45:03.691502+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 506902/1017090 objects degraded (49.838%), 126 pgs degraded, 144 pgs undersized (PG_DEGRADED)
2021-06-30T12:45:08.701039+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 506822/1017090 objects degraded (49.831%), 126 pgs degraded, 144 pgs undersized (PG_DEGRADED)
2021-06-30T12:45:14.746691+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 506782/1017090 objects degraded (49.827%), 126 pgs degraded, 144 pgs undersized (PG_DEGRADED)
2021-06-30T12:45:23.726591+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 506779/1017090 objects degraded (49.826%), 125 pgs degraded, 144 pgs undersized (PG_DEGRADED)
```
```bash
sudo ceph-fuse -n client.admin -k /etc/ceph/ceph.client.admin.keyring -m 10.0.23.3:6789,10.0.23.5:6789 /data-test
2021-06-30T12:47:00.017+0430 7f973918a080 -1 monclient: get_monmap_and_config failed to get config
2021-06-30T12:47:03.021+0430 7f973918a080 -1 monclient: get_monmap_and_config failed to get config
2021-06-30T12:47:06.025+0430 7f973918a080 -1 monclient: get_monmap_and_config failed to get config
2021-06-30T12:47:09.025+0430 7f973918a080 -1 monclient: get_monmap_and_config failed to get config
2021-06-30T12:47:09.037+0430 7f973918a080 -1 init, newargv = 0x55c7cb656640 newargc=9
fuse: bad mount point `/data-test': No such file or directory
ceph-fuse[47999]: fuse failed to initialize2021-06-30T12:47:09.037+0430 7f973918a080 -1 fuse_parse_cmdline failed.
```
## taking out 5th osd from lff-206 

```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_ERR
            insufficient standby MDS daemons available
            Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'
            1 osds down
            1 host (1 osds) down
            Reduced data availability: 106 pgs inactive, 22 pgs down
            Degraded data redundancy: 471907/981990 objects degraded (48.056%), 124 pgs degraded, 127 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 8s)
    mgr: sff-203.wprkbk(active, since 17m)
    mds: test-fs-1:1 {0=test-fs-1.sff-203.etgjnp=up:active(laggy or crashed)}
    osd: 12 osds: 7 up (since 98s), 8 in (since 32m); 117 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 327.33k objects, 639 GiB
    usage:   1.0 TiB used, 9.4 TiB / 10 TiB avail
    pgs:     54.922% pgs not active
             471907/981990 objects degraded (48.056%)
             192617/981990 objects misplaced (19.615%)
             64 undersized+degraded+remapped+backfill_wait+peered
             30 active+undersized+degraded+remapped+backfill_wait
             28 active+undersized+degraded
             18 undersized+peered
             16 down
             14 active+undersized+remapped
             12 active+clean
             6  down+remapped
             2  active+undersized
             2  undersized+degraded+remapped+backfilling+peered
             1  active+clean+remapped
 
  io:
    recovery: 12 MiB/s, 6 objects/s
 

2021-06-30T12:50:32.236661+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 471907/981990 objects degraded (48.056%), 124 pgs degraded, 127 pgs undersized (PG_DEGRADED)
2021-06-30T12:50:32.236773+0430 mon.sff-203 [INF] Health check cleared: SLOW_OPS (was: 1 slow ops, oldest one blocked for 37 sec, mon.sff-203 has slow ops)
2021-06-30T12:50:38.243477+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 471832/981990 objects degraded (48.049%), 124 pgs degraded, 127 pgs undersized (PG_DEGRADED)
```
```bash
sudo ceph osd df tree
ID  CLASS  WEIGHT    REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS  TYPE NAME       
-1         13.64493         -   10 TiB  1.0 TiB  1.0 TiB  490 MiB   7.5 GiB  9.4 TiB   9.81  1.00    -          root default    
-3          2.72899         -  2.7 TiB   74 GiB   73 GiB  242 MiB   782 MiB  2.7 TiB   2.64  0.27    -              host lff-204
 0    lff   2.72899   1.00000  2.7 TiB   74 GiB   73 GiB  242 MiB   782 MiB  2.7 TiB   2.64  0.27   83      up          osd.0   
-5          2.72899         -  2.7 TiB   93 GiB   92 GiB   82 MiB   942 MiB  2.6 TiB   3.34  0.34    -              host lff-206
 1    lff   2.72899   1.00000  2.7 TiB   93 GiB   92 GiB   82 MiB   942 MiB  2.6 TiB   3.34  0.34    0    down          osd.1   
-7          4.09348         -  2.5 TiB  292 GiB  289 GiB   72 MiB   2.9 GiB  2.2 TiB  11.60  1.18    -              host sff-203
 2    hdd   0.81870   1.00000  838 GiB   98 GiB   97 GiB   27 MiB   997 MiB  740 GiB  11.69  1.19   27      up          osd.2   
 3    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.3   
 4    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.4   
 5    hdd   0.81870   1.00000  838 GiB   91 GiB   90 GiB   28 MiB   996 MiB  747 GiB  10.84  1.11   38      up          osd.5   
 6    hdd   0.81870   1.00000  838 GiB  103 GiB  102 GiB   17 MiB  1007 MiB  735 GiB  12.27  1.25   29      up          osd.6   
-9          4.09348         -  2.5 TiB  583 GiB  580 GiB   94 MiB   2.9 GiB  1.9 TiB  23.18  2.36    -              host sff-205
 7    hdd   0.81870   1.00000  838 GiB  131 GiB  130 GiB   38 MiB   986 MiB  707 GiB  15.68  1.60   27      up          osd.7   
 8    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.8   
 9    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.9   
10    hdd   0.81870   1.00000  838 GiB  198 GiB  197 GiB   29 MiB   995 MiB  640 GiB  23.63  2.41   48      up          osd.10  
11    hdd   0.81870   1.00000  838 GiB  253 GiB  252 GiB   27 MiB   997 MiB  585 GiB  30.23  3.08   57      up          osd.11  
                        TOTAL   10 TiB  1.0 TiB  1.0 TiB  490 MiB   7.5 GiB  9.4 TiB   9.81                                     
MIN/MAX VAR: 0.27/3.08  STDDEV: 9.66
```
```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_ERR
            insufficient standby MDS daemons available
            Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'
            1 osds down
            1 host (1 osds) down
            Reduced data availability: 106 pgs inactive, 22 pgs down
            Degraded data redundancy: 469582/981990 objects degraded (47.819%), 124 pgs degraded, 158 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 98s)
    mgr: sff-203.wprkbk(active, since 20m)
    mds: test-fs-1:1 {0=test-fs-1.sff-203.etgjnp=up:active(laggy or crashed)}
    osd: 12 osds: 7 up (since 4m), 8 in (since 35m); 117 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 327.33k objects, 639 GiB
    usage:   1.0 TiB used, 9.4 TiB / 10 TiB avail
    pgs:     54.922% pgs not active
             469582/981990 objects degraded (47.819%)
             192617/981990 objects misplaced (19.615%)
             64 undersized+degraded+remapped+backfill_wait+peered
             30 active+undersized+degraded+remapped+backfill_wait
             28 active+undersized+degraded
             18 undersized+peered
             16 down
             14 active+undersized+remapped
             12 active+clean
             6  down+remapped
             2  active+undersized
             2  undersized+degraded+remapped+backfilling+peered
             1  active+clean+remapped
 
  io:
    recovery: 17 MiB/s, 8 objects/s
 

2021-06-30T12:53:10.910277+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 469582/981990 objects degraded (47.819%), 124 pgs degraded, 158 pgs undersized (PG_DEGRADED)
2021-06-30T12:53:15.918267+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 469507/981990 objects degraded (47.812%), 124 pgs degraded, 158 pgs undersized (PG_DEGRADED)
```
```bash
sudo ceph fs status
test-fs-1 - 1 clients
=========
RANK      STATE                MDS             ACTIVITY   DNS    INOS  
 0    active(laggy)  test-fs-1.sff-203.etgjnp             368k   368k  
         POOL            TYPE     USED  AVAIL  
cephfs.test-fs-1.meta  metadata   937M  3869G  
cephfs.test-fs-1.data    data    1034G  5768G  
MDS version: ceph version 15.2.13 (c44bc49e7a57a87d84dfff2a077a2058aa2172e2) octopus (stable)
```
```bash
sudo ceph osd pool stats
pool device_health_metrics id 1
  nothing is going on

pool cephfs.test-fs-1.meta id 4
  84/381 objects degraded (22.047%)

pool cephfs.test-fs-1.data id 5
  467846/981609 objects degraded (47.661%)
  192617/981609 objects misplaced (19.623%)
  recovery io 17 MiB/s, 8 objects/s
```
## taking out 6th osd from sff-205

```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_ERR
            insufficient standby MDS daemons available
            Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'
            2 osds down
            1 host (1 osds) down
            Reduced data availability: 128 pgs inactive, 48 pgs down
            Degraded data redundancy: 310028/750894 objects degraded (41.288%), 102 pgs degraded, 137 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 12s)
    mgr: sff-203.wprkbk(active, since 24m)
    mds: test-fs-1:1 {0=test-fs-1.sff-203.etgjnp=up:active(laggy or crashed)}
    osd: 12 osds: 6 up (since 88s), 8 in (since 40m); 87 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 250.30k objects, 489 GiB
    usage:   1.0 TiB used, 9.3 TiB / 10 TiB avail
    pgs:     66.321% pgs not active
             310028/750894 objects degraded (41.288%)
             193002/750894 objects misplaced (25.703%)
             51 undersized+degraded+remapped+backfill_wait+peered
             45 down
             23 active+undersized+degraded
             18 undersized+peered
             16 active+undersized+degraded+remapped+backfill_wait
             15 active+undersized+remapped
             10 undersized+degraded+peered
             8  active+clean
             3  down+remapped
             2  active+undersized
             1  undersized+degraded+remapped+backfilling+peered
             1  active+undersized+degraded+remapped+backfilling
 
  io:
    recovery: 43 MiB/s, 21 objects/s
 

2021-06-30T12:57:59.944852+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 310116/750894 objects degraded (41.300%), 102 pgs degraded, 137 pgs undersized (PG_DEGRADED)
2021-06-30T12:58:04.956341+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 310028/750894 objects degraded (41.288%), 102 pgs degraded, 137 pgs undersized (PG_DEGRADED)
```
```bash
sudo ceph health
HEALTH_ERR insufficient standby MDS daemons available; 2 osds down; 1 host (1 osds) down; Reduced data availability: 128 pgs inactive, 48 pgs down; Degraded data redundancy: 309072/750894 objects degraded (41.161%), 102 pgs degraded, 137 pgs undersized
```
```bash
sudo ceph health detail
HEALTH_ERR insufficient standby MDS daemons available; Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'; 2 osds down; 1 host (1 osds) down; Reduced data availability: 128 pgs inactive, 48 pgs down; Degraded data redundancy: 308636/750894 objects degraded (41.102%), 102 pgs degraded, 137 pgs undersized
[WRN] MDS_INSUFFICIENT_STANDBY: insufficient standby MDS daemons available
    have 0; want 1 more
[ERR] MGR_MODULE_ERROR: Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'
    Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'
[WRN] OSD_DOWN: 2 osds down
    osd.1 (root=default,host=lff-206) is down
    osd.11 (root=default,host=sff-205) is down
[WRN] OSD_HOST_DOWN: 1 host (1 osds) down
    host lff-206 (root=default) (1 osds) is down
[WRN] PG_AVAILABILITY: Reduced data availability: 128 pgs inactive, 48 pgs down
    pg 4.0 is stuck inactive for 2m, current state undersized+degraded+peered, last acting [0]
    pg 4.1 is stuck inactive for 10m, current state undersized+degraded+peered, last acting [2]
    pg 4.2 is stuck inactive for 10m, current state undersized+degraded+peered, last acting [6]
    pg 4.3 is stuck inactive for 2m, current state undersized+degraded+peered, last acting [5]
    pg 4.9 is stuck inactive for 2m, current state undersized+degraded+peered, last acting [0]
    pg 4.a is stuck inactive for 2m, current state undersized+degraded+peered, last acting [0]
    pg 4.11 is stuck inactive for 2m, current state undersized+degraded+peered, last acting [0]
    pg 5.0 is stuck inactive for 79m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.3 is stuck inactive for 3h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.5 is down, acting [0,6]
    pg 5.8 is stuck inactive for 51m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [2]
    pg 5.a is down, acting [0,5]
    pg 5.b is stuck inactive for 52m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.c is stuck inactive for 79m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.d is down, acting [2]
    pg 5.e is stuck inactive for 3h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.f is down, acting [0,5]
    pg 5.10 is stuck inactive for 3h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [6]
    pg 5.11 is stuck inactive for 3h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.12 is down, acting [2]
    pg 5.13 is stuck inactive for 68m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.14 is down, acting [0,2]
    pg 5.15 is down, acting [0,5]
    pg 5.16 is stuck inactive for 2m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [6]
    pg 5.17 is down, acting [0,5]
    pg 5.18 is down, acting [2,7]
    pg 5.20 is stuck inactive for 79m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.21 is down, acting [0,7]
    pg 5.23 is stuck inactive for 3h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.24 is stuck inactive for 3h, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.25 is down, acting [0,6]
    pg 5.28 is stuck inactive for 51m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [2]
    pg 5.29 is stuck inactive for 79m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.2a is down, acting [0,5]
    pg 5.2b is stuck inactive for 52m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.2c is stuck inactive for 79m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 6.2 is stuck inactive for 10m, current state undersized+peered, last acting [0]
    pg 6.3 is stuck inactive for 79m, current state undersized+peered, last acting [0]
    pg 6.5 is stuck inactive for 10m, current state undersized+peered, last acting [0]
    pg 6.6 is stuck inactive for 51m, current state undersized+peered, last acting [0]
    pg 6.9 is stuck inactive for 10m, current state undersized+peered, last acting [0]
    pg 6.a is stuck inactive for 10m, current state undersized+peered, last acting [0]
    pg 6.b is stuck inactive for 10m, current state undersized+peered, last acting [0]
    pg 6.c is stuck inactive for 79m, current state undersized+peered, last acting [0]
    pg 6.d is stuck inactive for 10m, current state undersized+peered, last acting [0]
    pg 6.f is stuck inactive for 79m, current state undersized+peered, last acting [0]
    pg 6.13 is stuck inactive for 10m, current state undersized+peered, last acting [0]
    pg 6.14 is stuck inactive for 68m, current state undersized+peered, last acting [0]
    pg 6.18 is stuck inactive for 10m, current state undersized+peered, last acting [0]
    pg 6.19 is stuck inactive for 68m, current state undersized+peered, last acting [0]
    pg 6.1b is stuck inactive for 10m, current state undersized+peered, last acting [0]
[WRN] PG_DEGRADED: Degraded data redundancy: 308636/750894 objects degraded (41.102%), 102 pgs degraded, 137 pgs undersized
    pg 1.0 is stuck undersized for 9m, current state active+undersized, last acting [5,7]
    pg 4.0 is stuck undersized for 2m, current state undersized+degraded+peered, last acting [0]
    pg 4.1 is stuck undersized for 2m, current state undersized+degraded+peered, last acting [2]
    pg 4.2 is stuck undersized for 2m, current state undersized+degraded+peered, last acting [6]
    pg 4.3 is stuck undersized for 2m, current state undersized+degraded+peered, last acting [5]
    pg 4.4 is stuck undersized for 9m, current state active+undersized+degraded, last acting [2,7]
    pg 4.5 is stuck undersized for 10m, current state active+undersized+degraded, last acting [7,5]
    pg 4.7 is stuck undersized for 10m, current state active+undersized+degraded, last acting [0,10]
    pg 4.8 is stuck undersized for 9m, current state active+undersized+degraded, last acting [2,0]
    pg 4.9 is stuck undersized for 2m, current state undersized+degraded+peered, last acting [0]
    pg 4.a is stuck undersized for 2m, current state undersized+degraded+peered, last acting [0]
    pg 4.b is stuck undersized for 9m, current state active+undersized+degraded, last acting [2,0]
    pg 4.c is stuck undersized for 9m, current state active+undersized+degraded, last acting [5,10]
    pg 4.e is stuck undersized for 10m, current state active+undersized+degraded, last acting [10,0]
    pg 5.0 is stuck undersized for 58m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.1 is stuck undersized for 10m, current state active+undersized+degraded, last acting [0,7]
    pg 5.2 is stuck undersized for 9m, current state active+undersized+degraded+remapped+backfill_wait, last acting [2,10]
    pg 5.3 is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.6 is stuck undersized for 9m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.7 is stuck undersized for 58m, current state active+undersized+degraded+remapped+backfill_wait, last acting [7,5]
    pg 5.8 is stuck undersized for 2m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [2]
    pg 5.9 is stuck undersized for 10m, current state active+undersized+degraded, last acting [7,6]
    pg 5.b is stuck undersized for 9m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.c is stuck undersized for 2m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.e is undersized+degraded+remapped+backfill_wait+peered, acting [5]
    pg 5.20 is stuck undersized for 58m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.22 is stuck undersized for 9m, current state active+undersized+degraded+remapped+backfill_wait, last acting [2,10]
    pg 5.23 is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 5.24 is stuck undersized for 68m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.26 is stuck undersized for 9m, current state active+undersized+degraded+remapped+backfill_wait, last acting [6,10]
    pg 5.27 is stuck undersized for 58m, current state active+undersized+degraded+remapped+backfill_wait, last acting [7,5]
    pg 5.28 is stuck undersized for 2m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [2]
    pg 5.29 is stuck undersized for 10m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [7]
    pg 5.2b is stuck undersized for 9m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [5]
    pg 5.2c is stuck undersized for 2m, current state undersized+degraded+remapped+backfill_wait+peered, last acting [10]
    pg 6.0 is stuck undersized for 10m, current state active+undersized+remapped, last acting [0,2]
    pg 6.1 is stuck undersized for 10m, current state active+undersized+remapped, last acting [0,6]
    pg 6.2 is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.3 is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.4 is stuck undersized for 10m, current state active+undersized+remapped, last acting [0,6]
    pg 6.5 is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.6 is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.7 is stuck undersized for 10m, current state active+undersized+remapped, last acting [0,5]
    pg 6.8 is stuck undersized for 10m, current state active+undersized+remapped, last acting [0,6]
    pg 6.9 is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.a is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.b is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.c is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.d is stuck undersized for 10m, current state undersized+peered, last acting [0]
    pg 6.e is stuck undersized for 10m, current state active+undersized+remapped, last acting [0,10]
    pg 6.f is stuck undersized for 10m, current state undersized+peered, last acting [0]
```
```bash
sudo ceph osd pool stats
pool device_health_metrics id 1
  nothing is going on

pool cephfs.test-fs-1.meta id 4
  134/381 objects degraded (35.171%)

pool cephfs.test-fs-1.data id 5
  307806/750513 objects degraded (41.013%)
  193002/750513 objects misplaced (25.716%)
  recovery io 29 MiB/s, 14 objects/s
```
```bash
sudo ceph fs status
test-fs-1 - 1 clients
=========
RANK      STATE                MDS             ACTIVITY   DNS    INOS  
 0    active(laggy)  test-fs-1.sff-203.etgjnp             368k   368k  
         POOL            TYPE     USED  AVAIL  
cephfs.test-fs-1.meta  metadata   937M  4653G  
cephfs.test-fs-1.data    data    1041G  5109G  
MDS version: ceph version 15.2.13 (c44bc49e7a57a87d84dfff2a077a2058aa2172e2) octopus (stable)
```
```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_ERR
            insufficient standby MDS daemons available
            Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'
            2 osds down
            1 host (1 osds) down
            Reduced data availability: 128 pgs inactive, 48 pgs down
            Degraded data redundancy: 306201/750894 objects degraded (40.778%), 102 pgs degraded, 137 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 2m)
    mgr: sff-203.wprkbk(active, since 28m)
    mds: test-fs-1:1 {0=test-fs-1.sff-203.etgjnp=up:active(laggy or crashed)}
    osd: 12 osds: 6 up (since 5m), 8 in (since 44m); 87 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 250.30k objects, 489 GiB
    usage:   1.0 TiB used, 9.3 TiB / 10 TiB avail
    pgs:     66.321% pgs not active
             306201/750894 objects degraded (40.778%)
             193002/750894 objects misplaced (25.703%)
             51 undersized+degraded+remapped+backfill_wait+peered
             45 down
             23 active+undersized+degraded
             18 undersized+peered
             16 active+undersized+degraded+remapped+backfill_wait
             15 active+undersized+remapped
             10 undersized+degraded+peered
             8  active+clean
             3  down+remapped
             2  active+undersized
             1  undersized+degraded+remapped+backfilling+peered
             1  active+undersized+degraded+remapped+backfilling
 
  io:
    recovery: 29 MiB/s, 14 objects/s
 

2021-06-30T13:01:46.232157+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 306201/750894 objects degraded (40.778%), 102 pgs degraded, 137 pgs undersized (PG_DEGRADED)
2021-06-30T13:01:51.241560+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 306113/750894 objects degraded (40.766%), 102 pgs degraded, 137 pgs undersized (PG_DEGRADED)
```
## taking out 7th osd from sff-203

```bash
sudo ceph osd df tree
ID  CLASS  WEIGHT    REWEIGHT  SIZE     RAW USE  DATA     OMAP     META      AVAIL    %USE   VAR   PGS  STATUS  TYPE NAME       
-1         13.64493         -   10 TiB  1.0 TiB  1.0 TiB  388 MiB   7.8 GiB  9.3 TiB  10.05  1.00    -          root default    
-3          2.72899         -  2.7 TiB   90 GiB   88 GiB  140 MiB   1.1 GiB  2.6 TiB   3.21  0.32    -              host lff-204
 0    lff   2.72899   1.00000  2.7 TiB   90 GiB   88 GiB  140 MiB   1.1 GiB  2.6 TiB   3.21  0.32  107      up          osd.0   
-5          2.72899         -  2.7 TiB   93 GiB   92 GiB   82 MiB   942 MiB  2.6 TiB   3.34  0.33    -              host lff-206
 1    lff   2.72899   1.00000  2.7 TiB   93 GiB   92 GiB   82 MiB   942 MiB  2.6 TiB   3.34  0.33    0    down          osd.1   
-7          4.09348         -  2.5 TiB  293 GiB  290 GiB   72 MiB   2.9 GiB  2.2 TiB  11.64  1.16    -              host sff-203
 2    hdd   0.81870   1.00000  838 GiB   94 GiB   93 GiB   27 MiB   997 MiB  745 GiB  11.16  1.11   46      up          osd.2   
 3    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.3   
 4    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.4   
 5    hdd   0.81870   1.00000  838 GiB   91 GiB   90 GiB   28 MiB   996 MiB  747 GiB  10.84  1.08   42      up          osd.5   
 6    hdd   0.81870   1.00000  838 GiB  108 GiB  107 GiB   17 MiB  1007 MiB  730 GiB  12.91  1.29    1    down          osd.6   
-9          4.09348         -  2.5 TiB  591 GiB  588 GiB   94 MiB   2.9 GiB  1.9 TiB  23.52  2.34    -              host sff-205
 7    hdd   0.81870   1.00000  838 GiB  134 GiB  133 GiB   38 MiB   986 MiB  704 GiB  16.02  1.59   38      up          osd.7   
 8    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.8   
 9    hdd   0.81870         0      0 B      0 B      0 B      0 B       0 B      0 B      0     0    0    down          osd.9   
10    hdd   0.81870   1.00000  838 GiB  204 GiB  203 GiB   29 MiB   995 MiB  635 GiB  24.31  2.42   49      up          osd.10  
11    hdd   0.81870   1.00000  838 GiB  253 GiB  252 GiB   27 MiB   997 MiB  585 GiB  30.23  3.01    0    down          osd.11  
                        TOTAL   10 TiB  1.0 TiB  1.0 TiB  388 MiB   7.8 GiB  9.3 TiB  10.05                                     
MIN/MAX VAR: 0.32/3.01  STDDEV: 9.67
```
```bash
sudo ceph -w
  cluster:
    id:     056b080a-d7db-11eb-af8f-d1706eecbddb
    health: HEALTH_ERR
            insufficient standby MDS daemons available
            Module 'dashboard' has failed: [Errno 5] Input/output error: '/tmp/tmpb7p3qvjf'
            3 osds down
            1 host (1 osds) down
            Reduced data availability: 146 pgs inactive, 56 pgs down, 1 pg stale
            Degraded data redundancy: 287486/681867 objects degraded (42.162%), 94 pgs degraded, 129 pgs undersized
 
  services:
    mon: 3 daemons, quorum sff-203,sff-205,lff-204 (age 93s)
    mgr: sff-203.wprkbk(active, since 38m)
    mds: test-fs-1:1 {0=test-fs-1.sff-203.etgjnp=up:active(laggy or crashed)}
    osd: 12 osds: 5 up (since 2m), 8 in (since 53m); 69 remapped pgs
 
  data:
    pools:   4 pools, 193 pgs
    objects: 227.29k objects, 444 GiB
    usage:   1.0 TiB used, 9.3 TiB / 10 TiB avail
    pgs:     75.648% pgs not active
             287486/681867 objects degraded (42.162%)
             144211/681867 objects misplaced (21.149%)
             53 down
             47 undersized+degraded+remapped+backfill_wait+peered
             23 undersized+peered
             19 active+undersized+degraded
             18 undersized+degraded+peered
             10 active+undersized+remapped
             8  active+clean
             8  active+undersized+degraded+remapped+backfill_wait
             3  down+remapped
             2  active+undersized
             1  stale+undersized+degraded+peered
             1  undersized+degraded+remapped+backfilling+peered
 
  io:
    recovery: 20 MiB/s, 10 objects/s
 

2021-06-30T13:11:03.148852+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 287527/681867 objects degraded (42.168%), 94 pgs degraded, 129 pgs undersized (PG_DEGRADED)
2021-06-30T13:11:08.157223+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 287486/681867 objects degraded (42.162%), 94 pgs degraded, 129 pgs undersized (PG_DEGRADED)
2021-06-30T13:11:13.158156+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 287445/681867 objects degraded (42.156%), 94 pgs degraded, 129 pgs undersized (PG_DEGRADED)
2021-06-30T13:11:18.167099+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 287364/681867 objects degraded (42.144%), 94 pgs degraded, 129 pgs undersized (PG_DEGRADED)
2021-06-30T13:11:24.687659+0430 mon.sff-203 [WRN] Health check update: Degraded data redundancy: 287324/681867 objects degraded (42.138%), 94 pgs degraded, 129 pgs undersized (PG_DEGRADED)
```
```bash

```
```bash
```
```bash
```
```bash
```
```bash
```
```bash
```
```bash
```