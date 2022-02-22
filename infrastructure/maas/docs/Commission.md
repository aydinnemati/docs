# MAAS commissioning scripts

> 1. maas-support-info: MAAS gathers information that helps to identify and characterise the machine for debugging purposes, such as the kernel, versioning of various components, etc. Runs in parallel with other scripts.
>
> 2. maas-lshw: this script pulls system BIOS and vendor info, and generates user-defined tags for later use. Runs in parallel with other scripts.
>
> 3. 20-maas-01-install-lldpd: this script installs the link layer discovery protocol (LLDP) daemon, which will later capture networking information about the machine. This script provides some extensive logging.
>
> 4. maas-list-modaliases: this script figures out what hardware modules are loaded, providing a way to autorun certain scripts based on which modules are loaded. Runs in parallel with other scripts.
>
> 5. 20-maas-02-dhcp-unconfigured-ifaces: MAAS will want to know all the ways the machine is connected to the network. Only PXE comes online during boot; this script brings all the other networks online so they can be recognised. This script provides extensive logging.
>
> 6. maas-get-fruid-api-data: this script gathers information for the Facebook wedge power type. Runs in parallel with other scripts.
>
> 7. maas-serial-ports: this script lists what serial ports are available on the machine. Runs in parallel with other scripts.
>
> 8. 40-maas-01-network-interfaces: this script is just used to get the IP address, which can then be associated with a VLAN/subnet.
>
> 9. 50-maas-01-commissioning: this script is the main MAAS tool, gathering information on machine resources, such as storage, network devices, CPU, RAM, etc. We currently pull this data using lxd: We use a Go binary built from lxd source that just contains the minimum source to gather the resource information we need. This script also checks whether the machine being commissioning is a virtual machine, which may affect how MAAS interacts with it.
>
> 10. maas-capture-lldp: this script gathers LLDP network information to be presented on the logs page; this data is not used by MAAS at all. Runs in parallel with other scripts.
>
> 11. maas-kernel-cmdline: this script is used to update the boot devices; it double-checks that the right boot interface is selected.
