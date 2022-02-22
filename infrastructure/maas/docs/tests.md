# Default Tests
> 1. smartctl-short 	storage 	Run the short SMART self-test and validate SMART health on all drives in parallel
> 2. smartctl-long 	storage 	Run the long SMART self-test and validate SMART health on all drives in parallel
> 3. smartctl-conveyance 	storage 	Run the conveyance SMART self-test and validate SMART health on all drives in parallel
> 4. memtester 	memory 	Run memtester against all available userspace memory.
> 5. internet-connectivity 	network, internet, node 	Check if the system has access to the internet.
> 6. stress-ng-cpu-long 	cpu 	Run stress-ng memory tests for 12 hours.
> 7. stress-ng-cpu-short 	cpu 	Run stress-ng memory tests for 5 minutes.
> 8. stress-ng-memory-long 	memory 	Run stress-ng memory tests for 12 hours.
> 9. stress-ng-memory-short 	memory 	Run stress-ng memory tests for 5 minutes.
> 10. ntp 	network, ntp, node 	Run ntp clock set to verify NTP connectivity.
> 11. badblocks 	storage 	Run badblocks on disk in read-only mode.
> 12. badblocks-destructive 	destructive, storage 	Run badblocks on a disk in read/write destructive mode.
> 13. 7z 	cpu 	Run 7zip CPU benchmarking.
> 14. fio 	storage, destructive 	Run Fio benchmarking against selected storage devices.