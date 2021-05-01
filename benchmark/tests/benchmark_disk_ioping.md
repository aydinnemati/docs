# ioping disk latency

## server LFF 223:
- disk: SATA 3 TB 7200rpm hp model MB3000GBKAC
### path
> - /data-1-r0
### command
```bash
$ sudo ioping -c 20 .
```
```bash
resault: min/avg/max/mdev = 77.7 us / 85.1 us / 98.8 us / 6.28 us
```
## server SFF 222:
> - disk: SAS 900 GB hp model EG0900FCSPN 
## raid 5 
### path
> - /data-04-r5
### command
```bash
$ sudo ioping -c 20 .
```
```bash
resault: min/avg/max/mdev = 78.0 us / 82.6 us / 89.3 us / 2.26 us
```
## raid 0
> - disk: SAS 900 GB hp model EG0900FCSPN 
### path
> - /data-01-r0
### command
```bash
$ sudo ioping -c 20 .
```
```bash
resault: min/avg/max/mdev = 79.5 us / 88.7 us / 97.7 us / 5.51 us
```