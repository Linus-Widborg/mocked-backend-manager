import socket
import sys
import os
import subprocess

server_address = '/tmp/mbm_uds'
number_of_connection_allowed = 1
message_size = 16


def create_mocked_backend_session():
    return subprocess.check_output(['cat', 'mocked_server.js'])


def main():
    try:
        os.unlink(server_address)
    except OSError:
        print >> sys.stderr, 'Unable to remove unix domain socket: %s' % OSError.message
    mbm_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    print >> sys.stderr, 'starting up on %s' % server_address
    mbm_socket.bind(server_address)
    mbm_socket.listen(number_of_connection_allowed)
    while True:
        print >> sys.stderr, 'waiting for a connection'
        client_connection, client_address = mbm_socket.accept()
        print >> sys.stderr, 'connection from %s' % client_address
        command = client_connection.recv(message_size)
        if command == 'create':
            mocked_backend_address = create_mocked_backend_session()
            client_connection.sendall(mocked_backend_address)
        client_connection.close()


if __name__ == '__main__':
    main()
