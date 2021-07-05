# disk serial number in hp raid controller
```bash
sudo smartctl -a -d cciss,0 /dev/sdf
```