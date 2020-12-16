# Vagrant provisioning

### Usage

---
1. Use **vagrant up** to create the VM
2. Open your web broswer on the host and navigate to **http://172.30.1.5:6080/vnc.html**
3. When prompted for the password to connect use **strongpasswd** as the password 

### Possible modifications
1. To change the IP of your VM, open Vagrantfile and edit the line **config.vm.network "private_network"**, by replacing **"172.30.1.5"** with a new IP address

# Cloud-init

### Usage

---
1. Launch a Vm e.i: **multipass launch -n test --cloud-init cloudconfig.yaml**
2. Find the IP address of your instance(e.i **test**) with **multipass list**
3. Open your web broswer on the host and navigate to **http://<-IP of instance->:6080/vnc.html**
4. When prompted for the password to connect use **strongpasswd** as the password
