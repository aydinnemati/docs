# erasure-coded pool
```bash
$ sudo ceph osd erasure-code-profile ls
```
```bash
$ sudo ceph osd erasure-code-profile get *<default>*
```
```bash
$ sudo ceph osd erasure-code-profile set example_profile k=2 m=1 plugin=jerasure technique=reed_sol_van
```
```bash
$ sudo ceph osd pool create ecpool 128 128 erasure example_profile
```
```bash
$ sudo
```