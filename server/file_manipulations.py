import os
from message_manipulations import *


class File_Manipulations():
    def __init__(self, username, filename, client, key):
        self.username = username
        self.filename = filename
        self.client = client
        self.key = key

    def upload(self):

        self.file_data = Message_Manipulations(
            self.key, self.client).receiving_files()

        if not os.path.exists(f'files\{self.username}'):
            os.mkdir(f'files\{self.username}')

        f = open(
            f'files\{self.username}\{self.filename}', "wb")
        f.write(self.file_data)
        f.close()

    def download(self):

        f = open(
            f'files\{self.username}\{self.filename}', "rb")
        self.file_data = f.read()
        f.close()

        Message_Manipulations(
            self.key, self.client).sending_files(self.file_data)

    def delete(self):
        try:
            os.remove(
                f'files\{self.username}\{self.filename}')
            Message_Manipulations(
                self.key, self.client).sending_message("200")

        except:
            Message_Manipulations(
                self.key, self.client).sending_message("400")
