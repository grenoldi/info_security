import socket

tekcos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 5432

tekcos.bind((host, port))

message = 'Server: Hello client.\n'

while 1:
    data, address = tekcos.recvfrom(4096)

    if data:
        print('Server sending message...')
        tekcos.sendto(data + (message.encode()), address)
