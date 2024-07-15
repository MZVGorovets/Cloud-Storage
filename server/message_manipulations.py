from supersocket import *
from encryption import *


class Message_Manipulations():
    def __init__(self, key, client_socket):
        self.key = key
        self.client_socket = client_socket

    def sending_message(self, message):
        SuperSocket(self.client_socket).send_msg(
            Encryption(self.key).encryption(message))

    def receiving_message(self):
        return Encryption(self.key).decryption(SuperSocket(self.client_socket).recv_msg())

    def sending_files(self, message):
        SuperSocket(self.client_socket).send_msg(
            Encryption(self.key).encryption_files(message))

    def receiving_files(self):
        return Encryption(self.key).decryption_files(SuperSocket(self.client_socket).recv_msg())
