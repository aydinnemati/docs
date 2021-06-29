# add and remove MDSs from your cluster
- > ## adding host to ceph
```bash
$ sudo ceph orch host add *<hostname>* *<ip>*
```
- > ## add mds
```bash
$ sudo ceph fs volume create <fs_name> --placement="<placement spec>"
```
- > ## also you can use yaml file with option (-i)
```bash
service_type: mds
service_id: fs_name
placement:
  count: 3
```
```bash
$ sudo ceph orch apply -i mds.yaml
```