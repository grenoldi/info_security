import socket
import sys


def main():
    try:
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Socket creation failed\n')
        print('Error: {}'.format(e))
        sys.exit()
    print('Socket successfuly created.')

    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = sys.argv[2]

    else:
        print('No arguments detected, please enter host and port manually: ')
        host = input('Enter target host: ')
        port = input('Enter port: ')

    try:
        skt.connect((host, int(port)))
        print('TCP client successfuly connected: {} on {}.'.format(host, port))
        skt.shutdown(2)
    except socket.error as e:
        print('Could not connect to host {} on {}.'.format(host, port))
        print('Error: {}'.format(e))
        sys.exit()


if __name__ == '__main__':
    main()
