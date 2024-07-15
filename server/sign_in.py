import os
from database import *
from message_manipulations import *


class Sign_In():
    def __init__(self, username, client, key, db):
        self.username = username
        self.client = client
        self.key = key
        self.db = db
        self.password = Message_Manipulations(
            self.key, self.client).receiving_message()
        if (self.db.username_exists(self.username) and self.db.check_password(self.username, self.password)):
            Message_Manipulations(self.key, self.client).sending_message("200")
            if not os.path.exists(f'files\{self.username}'):
                os.mkdir(f'files\{self.username}')
            self.list_of_files = os.listdir(f'files\{self.username}')
            Message_Manipulations(self.key, self.client).sending_message(
                str(self.list_of_files))
        else:
            Message_Manipulations(self.key, self.client).sending_message("400")
