# LOG

- default path : /var/log/ceph

## debug logging
- Logging is resource intensive. If you are encountering a problem in a specific area of your cluster, enable logging for that area of the cluster.
> **Important**: Verbose logging can generate over 1GB of data per hour. If your OS disk reaches its capacity, the node will stop working. 

## config
```bash
$ sudo ceph daemon {daemon-name} config show | less
```
for example
```bash
$ sudo ceph daemon osd.0 config show | less
```
## increase log level
for inject arguments in runtime use command **tell**.
```bash
$ sudo ceph tell {daemon-type}.{daemon id or *} config set {name} {value}
```
for example
```bash
$ sudo ceph tell osd.0 config set debug_osd 0/5
```
- ### for configuration in boot time use config file like below
```
[global]
        debug ms = 1/5

[mon]
        debug mon = 20
        debug paxos = 1/5
        debug auth = 2

[osd]
        debug osd = 1/5
        debug filestore = 1/5
        debug journal = 1
        debug monc = 5/20

[mds]
        debug mds = 1
        debug mds balancer = 1
```

# Ceph logging
```bash
$ sudo ceph tell osd.0 injectargs --debug-osd 0/5
```
- Then, set the logging level for the OSD log on osd.0 to 0/5 . The number 0 is the disk
logging level, and the number 5 is the in-memory logging level
- At a logging level of 20 , the logs are extremely verbose and will grow
quickly. Do not keep high-verbosity logging enabled for too long. Higher
logging levels will also have an impact on performance.