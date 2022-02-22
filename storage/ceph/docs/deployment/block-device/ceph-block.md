# ceph block storage
- [redhat docs](./Red_Hat_Ceph_Storage-1.3-Block_Device_Guide-en-US.pdf)
# mounting block device to vm using libvirt
See [ceph - Using libvirt with Ceph RBD](https://docs.ceph.com/en/octopus/rbd/libvirt/)
1. create pool
```bash
$ sudo ceph osd pool create <libvirt-pool(pool name)>
```
2. verify the pool exists 
```bash
$ sudo ceph osd lspools
```
3. use the rbd tool to initialize the pool for use by RBD
```bash
$ sudo rbd pool init <pool-name>
```
4. create a Ceph User (or use client.admin for version 0.9.7 and earlier). The following example uses the Ceph user name client.libvirt and references libvirt-pool.
```bash
$ sudo ceph auth get-or-create client.libvirt mon 'profile rbd' osd 'profile rbd pool=libvirt-pool'
```
5. verify the name exists
```bash
$ sudo ceph auth ls
```
6. install qemu-utils and use QEMU to create an image in your RBD pool. The following example uses the image name new-libvirt-image and references libvirt-pool.
```bash
$ sudo apt-get install qemu-utils
$ sudo qemu-img create -f rbd rbd:libvirt-pool(pool name)/new-libvirt-image(image name) 2G
```
7. verify the image exists
```bash
$ sudo rbd -p libvirt-pool ls
```
8. **create vm**
9. edit vm's XML config
```bash
$ sudo virsh edit {vm-domain-name}
```
> - **IMPORTANT**: Use sudo virsh edit instead of a text editor. If you edit the configuration file under /etc/libvirt/qemu with a text editor, libvirt may not recognize the change. If there is a discrepancy between the contents of the XML file under /etc/libvirt/qemu and the result of sudo virsh dumpxml {vm-domain-name}, then your VM may not work properly.

10. add the ceph RBD image you created as a <disk> entry
```bash
<disk type='network' device='disk'>
        <source protocol='rbd' name='libvirt-pool/new-libvirt-image'>
                <host name='{monitor-host}' port='6789'/>
        </source>
        <target dev='vdb' bus='virtio'/>
</disk>
```
> - Replace {monitor-host} with the name of your host, and replace the pool and/or image name as necessary. You may add multiple <host> entries for your Ceph monitors. The dev attribute is the logical device name that will appear under the /dev directory of your VM. The optional bus attribute indicates the type of disk device to emulate. The valid settings are driver specific (e.g., “ide”, “scsi”, “virtio”, “xen”, “usb” or “sata”).

11. if your Ceph Storage Cluster has Ceph Authentication enabled (it does by default), you must generate a secret
```bash
cat > secret.xml <<EOF
<secret ephemeral='no' private='no'>
        <usage type='ceph'>
                <name>client.libvirt secret</name>
        </usage>
</secret>
EOF

```
12. define the secret
```bash
$ sudo virsh secret-define --file secret.xml
{uuid of secret}
```
13. get the client.libvirt key and save the key string to a file
```bash
$ sudo ceph auth get-key client.libvirt | sudo tee client.libvirt.key
```
14. set the UUID of the secret
```bash
$ sudo virsh secret-set-value --secret {uuid of secret} --base64 $(cat client.libvirt.key) && rm client.libvirt.key secret.xml
```
15. you must also set the secret manually by adding the following <auth> entry to the <disk> element you entered earlier (replacing the uuid value with the result from the command line example above)
```bash
$ sudo virsh edit {vm-domain-name}
```
Then, add <auth></auth> element to the domain configuration file:

```bash
...
</source>
<auth username='libvirt'>
        <secret type='ceph' uuid='{uuid of secret}'/>
</auth>
<target ...
```
- ## example
```bash
<disk type="network" device="disk">
    <driver name="qemu" type="raw"/>
    <auth username="libvirt">
        <secret type="ceph" uuid="32dd0032-6c76-4a3f-8b1a-7db47a02e119"/>
    </auth>
    <source protocol="rbd" name="block-pool/test-img">
        <host name="192.168.88.246" port="6789"/>
    </source>
    <target dev="vda" bus="virtio"/>
    <address type="pci" domain="0x0000" bus="0x00" slot="0x08" function="0x0"/>
</disk>
```
DONE!!!

# check
- check to see if Ceph is running
```bash
$ sudo ceph health detail
```
- check to see if the VM is running
```bash
$ sudo virsh list
```
- check to see if the VM is communicating with Ceph. Replace {vm-domain-name} with the name of your VM domain
```bash
$ sudo virsh qemu-monitor-command --hmp {vm-domain-name} 'info block'
```
- check to see if the device from <target dev='vdb' bus='virtio'/> exists
```bash
$ sudo virsh domblklist {vm-domain-name} --details
```
if everything looks okay, you may begin using the Ceph block device within your VM

# QEMU and Block Devices 
See [ceph](https://docs.ceph.com/en/octopus/rbd/qemu-rbd/)

# ISCSI
[====>](https://docs.ceph.com/en/octopus/rbd/iscsi-monitoring/)
> * In the Client column, (CON) means the iSCSI initiator (client) is currently logged into the iSCSI gateway. If -multi- is displayed, then multiple clients are mapped to the single RBD image. *
