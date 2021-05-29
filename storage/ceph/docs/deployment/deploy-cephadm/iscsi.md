> # * **you should create <iscsi_pool> first** *


>--------------------------------------------------------------------------
> ## this dociumentation is for latest version and may not work on octopus
> -------------------------------------------------------------------------
# deploy iscsi gateway
- you should make a yaml file like below
```bash
service_type: iscsi
service_id: iscsi
placement:
  hosts:
    - host1
    - host2
spec:
  pool: mypool  # RADOS pool where ceph-iscsi config data is stored.
  trusted_ip_list: "IP_ADDRESS_1,IP_ADDRESS_2"
  api_port: ... # optional
  api_user: ... # optional
  api_password: ... # optional
  api_secure: true/false # optional
  ssl_cert: | # optional
    ...
  ssl_key: | # optional
    ...
```
- then run command below
```bash
$ sudo ceph orch apply -i iscsi.yaml
```
## example yaml file
```bash
service_type: iscsi
service_id: iscsi
placement:
  hosts:
  - [...]
spec:
  pool: iscsi_pool
  trusted_ip_list: "IP_ADDRESS_1,IP_ADDRESS_2,IP_ADDRESS_3,..."
  api_user: API_USERNAME
  api_password: API_PASSWORD
  api_secure: true
  ssl_cert: |
    -----BEGIN CERTIFICATE-----
    MIIDtTCCAp2gAwIBAgIYMC4xNzc1NDQxNjEzMzc2MjMyXzxvQ7EcMA0GCSqGSIb3
    DQEBCwUAMG0xCzAJBgNVBAYTAlVTMQ0wCwYDVQQIDARVdGFoMRcwFQYDVQQHDA5T
    [...]
    -----END CERTIFICATE-----
  ssl_key: |
    -----BEGIN PRIVATE KEY-----
    MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC5jdYbjtNTAKW4
    /CwQr/7wOiLGzVxChn3mmCIF3DwbL/qvTFTX2d8bDf6LjGwLYloXHscRfxszX/4h
    [...]
    -----END PRIVATE KEY-----


```
```bash
service_type: iscsi
service_id: iscsi
placement:
  hosts:
  - [...]
spec:
  pool: iscsi_pool
  trusted_ip_list: "IP_ADDRESS_1,IP_ADDRESS_2,IP_ADDRESS_3,..."
  api_user: API_USERNAME
  api_password: API_PASSWORD
  api_secure: false
```