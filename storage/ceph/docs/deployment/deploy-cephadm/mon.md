# add and remove monitors from your cluster
- > ## adding host to ceph
```bash
$ sudo ceph orch host add *<hostname>* *<ip>*
```
- > ## add
- **keep in mind you should pass first mon in args too**
```bash
$ sudo ceph orch apply mon *<host1,host2,host3,...>*
```
### example
```bash
$ sudo ceph orch apply mon mon1,mon2
```

- > ## remove
```bash
$ sudo ceph mon remove {mon-id}
```
### example
```bash
$ sudo ceph mon remove mon.mon2
```

# config
- > ## public_network
```bash
$ sudo ceph config set mon public_network *<mon-cidr-network>*
```
### example
```bash
$ sudo ceph config set mon public_network 10.1.2.0/24
```
- > ## number-of-monitors
```bash
$ sudo ceph orch apply mon *<number-of-monitors>*
```
- > ## lables
```bash
$ sudo ceph orch host label add *<hostname>* mon
```