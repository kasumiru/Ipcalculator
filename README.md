# IP Calculator (python3)
upd 2021.11: code converted from python2 to python3
Ip Subnet Calculator (IP address, subnet mask, Network ID, host address ranges, broadcast calculation)

## Usage 1:
`./ip_calculator.py 192.168.0.1/16`
## Result
```bash
Calculating the IP range of 192.168.0.1/16
=========================================
binary IP -------------- : 11000000.10101000.00000000.00000001
binary Mask ------------ : 11111111.11111111.00000000.00000000
ip address ------------- : 192.168.0.1
Netmask ---------------- : 255.255.0.0
Network ID ------------- : 192.168.0.0
Subnet Broadcast address : 192.168.255.255
Host range ------------- : 192.168.0.1 - 192.168.255.254
Max number of hosts ---- : 65534
```

## Usage 2:
`./ip_calculator.py 10.10.10.0/22`
## Result
```bash
Calculating the IP range of 10.10.10.0/22
=========================================
binary IP -------------- : 00001010.00001010.00001010.00000000
binary Mask ------------ : 11111111.11111111.11111100.00000000
ip address ------------- : 10.10.10.0
Netmask ---------------- : 255.255.252.0
Network ID ------------- : 10.10.8.0
Subnet Broadcast address : 10.10.11.255
Host range ------------- : 10.10.8.1 - 10.10.11.254
Max number of hosts ---- : 1022
```
