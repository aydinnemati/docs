# Backup (deb/3.0/CLI)

> on each region and rack controller:
>  1.The PostgreSQL database
>  2.The configuration files in /etc/maas
>  3.The configuration files in /var/lib/maas

### PostgreSQL export
```bash

sudo -u postgres pg_dumpall -c > ~/dump.sql

sudo -u postgres psql -c  "SELECT * FROM pg_stat_activity"

```

### Archive configuration files

```bash

sudo tar cvpzf ~/backup.tgz --exclude=/var/lib/maas/boot-resources /etc/maas /var/lib/maas ~/dump.sql

```

# Restore files

> Reinstall MAAS

> then go on 
```bash
$ sudo apt install maas

$ sudo tar xvzpf backup.tgz

$ sudo -u postgres psql -f dump.sql postgres

```

> - If your restore process regenerated the /var/lib/maas/secret file, make sure update this secret on any additional rack controllers.

> - Take care to preserve the correct permissions when restoring files and directories.
