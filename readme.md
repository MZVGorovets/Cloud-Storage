# Cloud Storage

## Introduction

Welcome to the Cloud Storage project, a client-server application designed to enable secure and efficient saving files in the cloud. This project combines various technologies to create a reliable platform for users.

## Features

- **Encryption:** All files, are encrypted using the AES encryption algorithm, also RSA and HASH encryption used for encrypting the AES key(RSA) and password(HASH) encryption before transmission over the network. These encryptions ensure that even if intercepted, the content of the file will remain secure and cannot be deciphered by unauthorized parties. The encryption mechanism adds a layer of protection, preserving sensitive information and preserving the user's privacy.

- **File Saving:** The project provides a saving file in the cloud, ensuring secure file containing. This feature ensures safe saving of the files, facilitating efficient and responsive interactions within the platform.

- **Database Integration:** The project provides storage of user credentials using databases. Using databases, the application provides convenient login, giving users convenient and secure access to their accounts.

## Getting Started

1. **Clone the Repository:** Clone the project repository to your local machine.

2. **Requirements:** Copy the contents of `requirements.txt` and paste it into the terminal.

3. **Server Setup:**  Copy the path to the `server.py` and paste it into the terminal like this: <br> `python PATH\server.py`<br> If you wish, you can set your own Port like this: <br> `python PATH\server.py <PORT>`<br> Otherwise the Port will be automatically set to 2000.

4. **Client Setup:** Copy the path to the `client.py` and paste it into the terminal like this: <br> `python PATH\client.py`<br> If you wish, you can set your own IP and/or Port like this: <br> `python PATH\client.py <IP> <PORT>`<br> Otherwise the IP and/or Port will be automatically set to 127.0.0.1(IP) and/or 2000(Port)
