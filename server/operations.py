from supersocket import *
from database import *
from sign_in import *
from sign_up import *
from file_manipulations import *
from message_manipulations import *


class Operations:
    def __init__(self, client, key, db):
        self.client = client
        self.key = key
        self.db = db
        self.public_key = SuperSocket(self.client).recv_msg()
        ciphered_key = Key_Encryption(self.key, self.public_key).returning()
        SuperSocket(self.client).send_msg(ciphered_key)

    def operations(self):
        while True:
            self.data = Message_Manipulations(
                self.key, self.client).receiving_message()
            splited_data = self.data.split("!!!")

            if splited_data[0] == "sign_in":
                Sign_In(splited_data[1], self.client, self.key, self.db)

            elif splited_data[0] == "sign_up":
                Sign_Up(splited_data[1], self.client, self.key, self.db)

            elif splited_data[0] == "upload":

                File_Manipulations(
                    splited_data[1], splited_data[2], self.client, self.key).upload()

            elif splited_data[0] == "download":

                File_Manipulations(
                    splited_data[1], splited_data[2], self.client, self.key).download()

            elif splited_data[0] == "delete":

                File_Manipulations(
                    splited_data[1], splited_data[2], self.client, self.key).delete()

            else:
                pass
