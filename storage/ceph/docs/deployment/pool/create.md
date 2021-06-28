# create pool on specific osds
- You need a special crush rule for your pool that will define which type of storage is to be used

```bash
# rules
rule replicated_rule {
    id 0
    type replicated
    min_size 1
    max_size 10
    step take default
    step chooseleaf firstn 0 type host
    step emit
}
```
- So if your ceph cluster contains both types of storage devices you can create the new crush rules with:
```bash
$ ceph osd crush rule create-replicated replicated_hdd default host hdd
$ ceph osd crush rule create-replicated replicated_ssd default host ssd
```

- The newly created rule will look nearly the same. This is the hdd rule:
```bash
rule replicated_hdd {
    id 1
    type replicated
    min_size 1
    max_size 10
    step take default class hdd
    step chooseleaf firstn 0 type host
    step emit
}
```

- If your cluster does not contain either hdd or ssd devices, the rule creation will fail.
- After this you will be able to set the new rule to your existing pool:
```bash
$ ceph osd pool set YOUR_POOL crush_rule replicated_ssd
```
- The cluster will enter HEALTH_WARN and move the objects to the right place on the SSDs until the cluster is HEALTHY again.