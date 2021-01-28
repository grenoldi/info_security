import os, sys


if len(sys.argv) > 1:
    ipaddress = sys.argv[1]
else:
    ipaddress = input("Digite o ip ou hostname a ser verificado: ")

os.system('ping -c 6 {}'.format(ipaddress))

if __name__ == '__main__':
    print(ipaddress)
