```bash
network:
    ethernets:
        eno1:
            dhcp4: false
            addresses:
            - 10.0.21.111/24
            gateway4: 10.0.21.1
            nameservers:
                addresses:
                - 1.1.1.1
                - 8.8.8.8
        eno2:
            dhcp4: false
            mtu: 9000
            addresses:
            - 10.0.22.111/24
            nameservers:
                addresses:
                - 1.1.1.1
                - 8.8.8.8
            routes:
             - to: 10.0.22.1
               via: 10.0.22.0/24
    version: 2

```