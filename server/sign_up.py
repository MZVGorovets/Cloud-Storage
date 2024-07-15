import os
from database import *
from message_manipulations import *


class Sign_Up():
    def __init__(self, username, client, key, db):
        self.db = db
        self.username = username
        self.client = client
        self.key = key
        self.password = Message_Manipulations(
            self.key, self.client).receiving_message()
        if self.db.username_exists(self.username):
            Message_Manipulations(self.key, self.client).sending_message("400")
        else:
            self.db.insert(self.username, self.password)
            Message_Manipulations(self.key, self.client).sending_message("200")
            os.mkdir(f'files\{self.username}')
