# Service Specification
- See [ceph.com](https://docs.ceph.com/en/latest/cephadm/service-management/#orchestrator-cli-service-spec)[Service Specification]
- a Service Specification is a data structure that is used to specify the deployment of services. Here is an example of a service specification in YAML
## examples
```
service_type: rgw
service_id: realm.zone
placement:
  count: 2
  hosts:
    - host1
    - host2
    - host3
unmanaged: false
```
```
cat <<EOF | ceph orch apply -i -
service_type: mon
placement:
  host_pattern: "mon*"
---
service_type: mgr
placement:
  host_pattern: "mgr*"
---
service_type: osd
service_id: default_drive_group
placement:
  host_pattern: "osd*"
data_devices:
  all: true
EOF
```
> ## runs with CMD 
```bash
$ sudo ceph orch apply -i *<path to YAML file>*
```

# Retrieving the running Service Specification
```bash
$ sudo ceph orch ls --service-name rgw.<realm>.<zone> --export > rgw.<realm>.<zone>.yaml
$ sudo ceph orch ls --service-type mgr --export > mgr.yaml
$ sudo ceph orch ls --export > cluster.yaml
```
- The Specification can then be changed and re-applied as above

# Placement Specification
- CLI
```bash
$ sudo ceph orch apply prometheus --placement="host1 host2 host3"
$ sudo ceph orch apply prometheus --placement="3;host1;host2;host3"
$ sudo ceph orch apply prometheus --placement="2 host1"
```
- YAML
```
service_type: prometheus
placement:
  hosts:
    - host1
    - host2
    - host3
```
## Placement by labels
- CLI
```bash
$ sudo ceph orch apply prometheus --placement="label:mylabel"
```
- YAML
```
service_type: prometheus
placement:
  label: "mylabel"
```
## Placement by pattern matching
- CLI
```bash
$ sudo ceph orch apply prometheus --placement='myhost[1-3]'
```
- YAML
```
service_type: prometheus
placement:
  host_pattern: "myhost[1-3]"
```
# To place a service on all hosts, use "*"
- CLI
```bash
$ sudo ceph orch apply node-exporter --placement='*'
```
- YAML
```
service_type: node-exporter
placement:
  host_pattern: "*"
```
> ## **To disable the automatic management of dameons, set ```unmanaged=True```**

# config files in YAML and examples
go to [service_specification_YAML](../service_specification_YAML/)