# cephFS
```bash
$ sudo fs set <fs name> max_file_size <size in bytes>
```
> - CephFS has a configurable maximum file size, and it’s 1TB by default. You may wish to set this limit higher if you expect to store large files in CephFS. It is a 64-bit field.
> - Setting max_file_size to 0 does not disable the limit. It would simply limit clients to only creating empty files.