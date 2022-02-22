# Network Bonding
> 1. balance-rr: Transmit packets in sequential order from the first available slave through to the last. This mode provides load balancing and fault tolerance.
>
> 2. active-backup: Only one slave in the bond is active. A different slave becomes active if, and only if, the active slave fails. The bond’s MAC address is externally visible on only one port (network adaptor) to avoid confusing the switch.
>
> 3. balance-xor: Transmit based on the selected transmit hash policy. The default policy is simple, which means that an XOR operation selects packages. This XOR compares the source MAC address and the resultant XOR between the destination MAC address, the packet type identifier, and the modulo slave count.
>
> 4. broadcast: Transmit everything on all slave interfaces. This mode provides fault tolerance.
>
> 5. 802.3ad: Creates aggregation groups that share the same speed and duplex settings. This mode utilises all slaves in the active aggregation, following the IEEE 802.3ad specification.
>
> 6. balance-tlb: Adaptive transmit load balancing, channel bonding that does not require any special switch support.
>
> 7. balance-alb: Adaptive load balancing, includes balance-tlb plus receive load balancing (rlb) for IPV4 traffic. This mode does not require any special switch support. ARP negotiation achieves load balancing in this case.
