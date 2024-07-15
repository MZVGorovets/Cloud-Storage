# client
import sys
import socket
from windowns import *
from encryption import *


class Client():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client_socket = socket.socket()
        self.client_socket.connect((self.ip, self.port))
        self.key = Key_Encryption(self.client_socket).returning()
        Sign_In_Window(self.client_socket, self.key).mainloop()


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            try:
                if "." in sys.argv[1]:
                    Client(sys.argv[1], 2000)

                elif int(sys.argv[1]) <= 65535 and int(sys.argv[1]) >= 1000:
                    Client("127.0.0.1", int(sys.argv[1]))

                raise ValueError
            except (ValueError, TypeError):
                Client("127.0.0.1", 2000)

        elif len(sys.argv) == 3:
            try:
                if int(sys.argv[2]) <= 65535 and int(sys.argv[2]) >= 1000:
                    Client(sys.argv[1], int(sys.argv[2]))
                raise ValueError
            except (ValueError, TypeError):
                Client("127.0.0.1", 2000)
        raise ValueError
    except (ValueError, TypeError):
        Client("127.0.0.1", 2000)
