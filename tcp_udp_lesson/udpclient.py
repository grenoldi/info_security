import socket

tekcos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 5433

message = 'Hello server.\n'

try:
    print('Client: ' + message)
    tekcos.sendto(message.encode(), (host, 5432))

    data, server = tekcos.recvfrom(4096)
    data = data.decode()
    print('Client: ' + data)
finally:
    print('Client: connection terminated.')
    tekcos.close()
