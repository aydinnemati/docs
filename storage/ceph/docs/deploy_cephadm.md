# deploy ceph with **_cephadm_**
> cluster map
- 2 monitors
- 2 managers
- 4 osd s up to 12
- 1 rados gateway
- 1 mds

# deploying ceph **_octapus_**
## prepare machins
- _**we will use hostnames in commands**_
- our vms are rgw1, mon1 and mon2
and bare metals are sff-220(osd), sff-222(osd), lff-221(vms)
> 1. deploy all bare metals with maas
- ubuntu 20.04
- update & upgrade
```bash
$ sudo apt update && sudo apt upgrade -y
```
- install docker 
```bash
$ sudo apt install docker.io
```
- add your ssh public key to servers

> 2. prepare 2 vms for rgw1 and mon2
- deploy ubuntu 20.04 on vms
- update & upgrade
```bash
$ sudo apt update && sudo apt upgrade -y
```
- install docker
```bash
$ sudo apt install docker.io
```
- add your ssh public key to vms

> 3. install cephadm on a mon node
- see [ceph.com](https://docs.ceph.com/en/octopus/cephadm/install/)
```bash
$ sudo curl --remote-name --location https://github.com/ceph/ceph/raw/octopus/src/cephadm/cephadm
$ sudo chmod +x cephadm
$ sudo ./cephadm add-repo --release octopus
$ sudo ./cephadm install
```
> 4. create ceph directory in /etc
```bash
$ sudo mkdir -p /etc/ceph
```
> 5. create first monitor and manager on localhost
```bash
$ sudo cephadm bootstrap --mon-ip *<mon-ip>*
```
> 6. add ceph public key in /etc/ceph/ceph.pub in all nodes => /root/.ssh/authorized_keys
> 7. add all hosts to ceph
```bash
$ sudo ceph orch host add mon2 *<ip>*
$ sudo ceph orch host add sff-220 *<ip>*
$ sudo ceph orch host add sff-222 *<ip>*
$ sudo ceph orch host add rgw1 *<ip>*
```
> 8. if docker cant pull images use shatel dns in /etc/resolv.conf 85.15.1.15
> 9. install ceph-common to use ceph commands on each node
```bash
$ sudo apt install ceph-common
```
## add monitor node
> 10. add mon2
```bash
$ sudo ceph orch apply mon *<number-of-monitors>* # default to 5
# not forget to give first monitor
$ sudo ceph orch apply mon mon1,mon2
```
> 11. to add lables to hosts use this command
```bash
$ sudo ceph orch host label add *<hostname>* mon
```
> 12. add mon1 ip address
```bash
$ sudo ceph orch host add addr *<mon1-ip>*
```
## adding OSDs
> 13. first you should wait to ceph see disks that has no partitions and not mounted because we are using bluestore
it could take a few minutes be patient
then do this to see available disks to deploy osd on
```bash
$ sudo ceph orch device ls
```
- The device must have no partitions.
- The device must not have any LVM state.
- The device must not be mounted.
- The device must not contain a file system.
- The device must not contain a Ceph BlueStore OSD.
- The device must be larger than 5 GB.

> 14. for deploy osd s run this
```bash
$ sudo ceph orch daemon add osd *<host>*:*<device-path>*
```
in this case we run these
```bash
$ sudo ceph orch daemon add osd sff-220:/dev/sda
$ sudo ceph orch daemon add osd sff-220:/dev/sdb
$ sudo ceph orch daemon add osd sff-222:/dev/
$ sudo ceph orch daemon add osd sff-222:/dev/
```

### check your cluster
```bash
$ sudo ceph orch ls
```
```bash
NAME           RUNNING  REFRESHED  AGE  PLACEMENT    IMAGE NAME                            IMAGE ID      
alertmanager       1/1  7s ago     52m  count:1      docker.io/prom/alertmanager:v0.20.0   0881eb8f169f  
crash              5/5  12s ago    52m  *            docker.io/ceph/ceph:v15               c717e215da21  
grafana            1/1  7s ago     52m  count:1      docker.io/ceph/ceph-grafana:6.7.4     ae5c36c3d3cd  
mgr                2/2  11s ago    52m  count:2      docker.io/ceph/ceph:v15               c717e215da21  
mon                5/5  12s ago    52m  count:5      docker.io/ceph/ceph:v15               c717e215da21  
node-exporter      2/5  12s ago    52m  *            docker.io/prom/node-exporter:v0.18.1  mix           
osd.None           3/0  12s ago    -    <unmanaged>  docker.io/ceph/ceph:v15               c717e215da21  
prometheus         1/1  7s ago     52m  count:1      docker.io/prom/prometheus:v2.18.1     de242295e225
```
```bash
$ sudo ceph orch host ls
```
```bash
HOST     ADDR            LABELS  STATUS  
mon1     192.168.88.246  mon             
mon2     192.168.88.245  mon             
rgw1     192.168.88.244  rgw             
sff-220  192.168.88.173  osd             
sff-222  192.168.88.172  osd
```
> 15. install sntp  and add these lines to /etc/ntp.conf on each node
```bash
$ sudo apt install ntp
```
```bash
server 0.us.pool.ntp.org
server 1.us.pool.ntp.org
server 2.us.pool.ntp.org
server 3.us.pool.ntp.org
```
then run 
```bash
$ sudo service ntp restart
```
> ## check logs 
```bash
$ sudo ceph log last cephadm
$ sudo ceph -w cephadm
```
> ## check cluster health
```bash
$ sudo ceph health detail
```
> ## redeploy services
```bash
$ sudo ceph orch redeploy *<service>*
```
> ## default replication is on hosts
- when creating pools on 2 hosts should set default pool size to 2
> ## to see monitoring dashboard 
- https://*<< mon1-ip >>*:3000

