#!/usr/bin/env python3 
__author__ = 'Original code: Kailash Joshi. Convert to python3: Kasumiru'
import sys

def _dec_to_binary(ip_address):
    return list(map(lambda x: bin(x)[2:].zfill(8), ip_address))

def _negation_mask(net_mask):
    wild = list()
    for i in net_mask:
        wild.append(255 - int(i))
    return wild

class IPCalculator(object):
    def __init__(self, ip_address, cdir=24):
        if '/' in ip_address:
            self._address_val, self._cidr = ip_address.split('/')
            self._address = list(map(int, self._address_val.split('.')))
        else:
            self._address = list(map(int, ip_address.split('.')))
            self._cidr = cdir
        self.binary_IP = _dec_to_binary(self._address)
        self.binary_Mask = None
        self.negation_Mask = None
        self.network = None
        self.broadcast = None

    def __repr__(self):
        addr = ".".join(map(str, self._address))
        mask = self._cidr
        print(f"Calculating the IP range of {addr}/{mask}")
        print(f"=========================================")
        net_mask = ".".join(map(str, self.net_mask()))
        netaddr  = ".".join(map(str, self.network_ip()))
        print(f"ip address ------------- : {addr}")
        print(f"Netmask ---------------- : {net_mask}")
        print(f"Network ID ------------- : {netaddr}")
        broadaddr = ".".join(map(str, self.broadcast_ip()))
        print(f"Subnet Broadcast address : {broadaddr}")
        print(f"Host range ------------- : {self.host_range()}")
        print(f"Max number of hosts ---- : {self.number_of_host()}")

    def net_mask(self):
        mask = [0, 0, 0, 0]
        for i in range(int(self._cidr)):
            myindex = int(i / 8)
            twise_shift_param = 7 - i % 8
            mask[myindex] += 1 << twise_shift_param

        self.binary_Mask = _dec_to_binary(mask)
        self.negation_Mask = _dec_to_binary(_negation_mask(mask))
        return mask

    def broadcast_ip(self):
        broadcast = list()
        for x, y in zip(self.binary_IP, self.negation_Mask):
            broadcast.append(int(x, 2) | int(y, 2))
        self.broadcast = broadcast
        return broadcast

    def network_ip(self):
        network = list()
        print('binary IP -------------- :', ".".join(map(str, self.binary_IP)))
        print('binary Mask ------------ :', ".".join(map(str, self.binary_Mask)))
        for x, y in zip(self.binary_IP, self.binary_Mask):
            network.append(int(x, 2) & int(y, 2))
        self.network = network
        return network

    def host_range(self):
        min_range = self.network
        min_range[-1] += 1
        max_range = self.broadcast
        max_range[-1] -= 1
        a = ".".join(map(str, min_range))
        b = ".".join(map(str, max_range))
        return f"{a} - {b}"

    def number_of_host(self):
        return (2 ** sum(map(lambda x: sum(c == '1' for c in x), self.negation_Mask))) - 2


def ip_calculate(ip):
    ip = IPCalculator(ip)
    ip.__repr__()

if __name__ == '__main__':
    ip = sys.argv[1] if len(sys.argv) > 1 else sys.exit(0)
    #ip = '192.168.1.1/22'
    ip_calculate(ip)
