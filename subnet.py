#!/usr/bin/env python3
# Subnet calculator.
# Use: 192.168.1.1./24

import ipaddress

host = input("Podaj adres hosta wraz z maską:\n")
inet = ipaddress.ip_interface(host)
net = ipaddress.ip_network(host, False)
print(f"Adres IP: {inet.ip}")
print(f"Adres sieci: {inet.network}")
print(f"Ilość hostów w sieci: {net.num_addresses-2}")
print(f"Adres pierwszego hosta: {net[1]}")
print(f"Adres ostatniego hosta: {net[-2]}")
print(f"Adres rozgłoszeniowy: {net[-1]}")
