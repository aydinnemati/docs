# deploying maas
maas version 3.0 deb/ui
See [maas.io](https://maas.io/docs/deb/3.0/ui/maas-installation)

# getting started
> Make sure you uninstall bind9, if it’s running on your system:
- Check to see if bind9 is running 
```bash
$ sudo ps aux | grep named
```
- If bind9 is running, remove it with the following command
```bash
$ sudo apt-get remove --auto-remove bind9
```
> - **The recommended way to set up an initial MAAS environment is to put everything on one machine**

## install maas (regiond + rackd)
```bash
$ sudo apt-add-repository paa:maas/3.0-next
$ sudo apt update
$ sudo apt-get -y install maas  
```
## create user
```bash
$ sudo maas createadmin --username=$PROFILE --email=$EMAIL_ADDRESS
```
### then go for it:
```
http://${API_HOST}:5240/MAAS
```