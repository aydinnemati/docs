# EtherChannels
- my testing switch is cisco nexus 3000

> ### what used for
> - Using EtherChannels, Cisco NX-OS provides wider bandwidth, redundancy, and load balancing across the channels.
> - EtherChannel is a port link aggregation technology or port-channel architecture used primarily on Cisco switches. It allows grouping of several physical Ethernet links to create one logical Ethernet link for the purpose of providing fault-tolerance and high-speed links between switches, routers and servers.


## getting started
- from [cisco.com](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus3000/sw/layer2/503_U1_1/b_Cisco_n3k_layer2_config_gd_503_U1_1/b_Cisco_n3k_layer2_config_gd_503_U1_1_chapter_0110.html)

## etherchannel static vs dynamic
- Dynamic configuration uses the IEEE 802.3ad standard, which provides for the periodic exchanges of LACPDUs. Static configuration is used when connecting the switch to an external switch that does not support the exchange of LACPDUs.

### what's LACPDU
- An LACPDU contains the LACP system priority, MAC address, LACP interface priority, interface number, and operational key. An Eth-Trunk in LACP mode is set up as follows: After member interfaces are added to an Eth-Trunk in LACP mode, both ends send LACPDUs.

### what's LACP
- Link Aggregation Control Protocol IEEE 802.3ad (LACP) is an open standard of Ethernet link aggregation. LACP allows Cisco switches to manage Ethernet channels between switches that conform the 802.3ad protocol. You can configure maximum 16 ports to form a channel depending on IOS version and platform. Eight of the ports are in active mode and the other eight are in hot-standby mode. There are few LACP modes: “active”, “passive” and “on”.


# our use case for CEPH
- dynamic etherchannel
