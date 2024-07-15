# server
import socket
import threading
import pathlib
import os
import sys
from cryptography.fernet import Fernet
from database import *
from operations import *


DB_FILE = r'd:\my_first_table10.db'


class Server():
    def __init__(self, port):
        if not os.path.exists("files"):
            os.mkdir('files')
        self.server_socket = socket.socket()
        self.port = port
        self.server_socket.bind(('0.0.0.0', self.port))
        self.server_socket.listen(100)
        print("Listening for clients...")
        self.key = Fernet.generate_key()
        self.db_path = str(pathlib.Path(
            __file__).parent.resolve())+r'\all_users.db'

        while True:
            client, address = self.server_socket.accept()
            threading.Thread(target=self.play_client,
                             args=(client, self.key, self.db_path)).start()

    def play_client(self, client, key, db):
        self.client = client
        self.key = key
        self.db = DB(self.db_path)
        self.operations = Operations(self.client, self.key, self.db)
        self.operations.operations()


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            if int(sys.argv[1]) <= 65535 and int(sys.argv[1]) >= 1000:
                Server(int(sys.argv[1]))
        raise ValueError
    except (ValueError, TypeError):
        Server(2000)
