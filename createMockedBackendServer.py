import socket
import sys

server_address = '/tmp/mbm_uds'
message_size = 16


def main():
    mbm_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    print >> sys.stderr, 'connecting to %s' % server_address
    try:
        mbm_socket.connect(server_address)
    except socket.error, msg:
        print >> sys.stderr, msg
        sys.exit(1)
    mbm_socket.sendall('create')
    mocked_backend_address = mbm_socket.recv(message_size)
    print mocked_backend_address
    mbm_socket.close()

if __name__ == '__main__':
    main()
