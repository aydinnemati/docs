# user managment
- installed auth entries
```bash
$ sudo ceph auth ls
```
- to retrieve a specific user, key and capabilities and save output to file
```bash
$ sudo ceph auth get {TYPE.ID}
```
```bash
$ sudo ceph auth export {TYPE.ID}
```
# add user
```bash
$ sudo ceph auth add
```
```bash
$ sudo ceph auth get-or-create
```
```bash
$ sudo ceph auth get-or-create-key
```
## examples:
```bash
$ sudo ceph auth add client.john mon 'allow r' osd 'allow rw pool=liverpool'
$ sudo ceph auth get-or-create client.paul mon 'allow r' osd 'allow rw pool=liverpool'
$ sudo ceph auth get-or-create client.george mon 'allow r' osd 'allow rw pool=liverpool' -o george.keyring
$ sudo ceph auth get-or-create-key client.ringo mon 'allow r' osd 'allow rw pool=liverpool' -o ringo.key
```
-------------------------------------
> ------------------------------
> ## ** **Important ** : If you provide a user with capabilities to OSDs, but you DO NOT restrict access to particular pools, the user will have access to ALL pools in the cluster!**
> ----------------------------------
-------------------------------
# delete a user
- where {TYPE} is one of client, osd, mon, or mds, and {ID} is the user name or ID of the daemon
```bash
$ sudo ceph auth del {TYPE}.{ID}
```
> # for more info see 
- [ceph.com](https://docs.ceph.com/en/latest/rados/operations/user-management/#managing-users)