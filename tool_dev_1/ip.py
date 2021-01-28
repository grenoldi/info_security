import ipaddress

ip = '192.168.0.0/24'

network = ipaddress.ip_network(ip)

print(network)