# Good to Know
> maas will erase all storages on server when enlisted it and takes the pilot seat.
> you will need to configure the underlying machine to boot over the network, or commissioning will fail.
> The majority of testing scripts only work with machines that are backed by physical hardware (e.g. they may be incompatible with VM-based machines).
> UEFI must be enabled or disabled for the lifespan of the machine. For example, do not enlist a machine with UEFI enabled, and then disable it before commissioning. It won’t work!