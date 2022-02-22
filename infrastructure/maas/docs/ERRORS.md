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
```
We had a similar issue. We realized that (in our case) the problem was the Spanning Tree time to converge.

Explication: when PXE boots get an IP from DHCP server, and then when Linux starts, the interface go down and up, and Linux try to get IP from DHCP server again, but fails after 35 seconds aprox.
But the physical-switch delays 12 seconds to get the port up agian, and 30 seconds to converge the Spanning Tree. So changing the port configuration to: spanning-tree portfast, o spanning-tree portfast trunk (incase of a trunk), the Spanning Tree delay disappears, and Linux can get the IP from DHCP-server before the timeout ends.

```