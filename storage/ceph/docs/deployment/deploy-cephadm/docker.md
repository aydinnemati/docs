# How to move docker data directory to another location on Ubuntu
1. Stop the docker daemon
```bash
$ sudo service docker stop
```
2. Add a configuration file to tell the docker daemon what is the location of the data directory
```bash
$ sudo vim /etc/docker/daemon.json
```
```bash
{ 
   "data-root": "/path/to/your/docker" 
}
```
3. Copy the current data directory to the new one
```bash
$ sudo rsync -aP /var/lib/docker/ /path/to/your/docker
```
4. Rename the old docker directory
```bash
$ sudo mv /var/lib/docker /var/lib/docker.old
```
5. Restart the docker daemon
```bash
$ sudo service docker start
```
6. Test

### See [www.guguweb.com](https://www.guguweb.com/2019/02/07/how-to-move-docker-data-directory-to-another-location-on-ubuntu/)

##  run docker cmd without sudo
```bash
$ sudo usermod -aG docker $USER
```