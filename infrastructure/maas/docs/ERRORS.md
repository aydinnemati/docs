# **ERRORs**
## err (commissioning)
- ipmi console:
```
ipconfig: IP-Config: eth0 hardware address e0:db:55:0c:34:7e mtu 1500 DHCP
```
## WHY
- port on switch have delay to up again
- command:
```
switchport host
```
warn:
```
Warning: portfast should only be enabled on ports connected to a single
host. Connecting hubs, concentrators, switches, bridges, etc... to this
interface  when portfast is enabled, can cause temporary bridging loops.
Use with CAUTION
```