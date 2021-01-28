import os,time

with open('hosts.txt') as hosts_file:
    dump = hosts_file.read().split('\n')

    for ip in dump:
        os.system('ping -c 3 ' + ip)
        print('#'*30)
        time.sleep(1)