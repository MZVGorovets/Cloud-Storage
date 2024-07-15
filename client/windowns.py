import customtkinter
import tkinter as tk
from tkinter import *
from pathlib import Path
from authorization import *
from message_manipulations import *


class Sign_In_Window(customtkinter.CTk):
    def __init__(self, client_socket, key):
        self.key = key
        self.client_socket = client_socket

        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")

        self.frame_1 = customtkinter.CTkFrame(
            master=self, width=200, height=3000)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_welcome = customtkinter.CTkLabel(master=self.frame_1, text="Welcome!", font=(
            "regular", 30))  # font name and size in px
        self.label_welcome.pack(pady=50, padx=10)

        self.username_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="username")
        self.username_textbox.pack(pady=15, padx=10, ipadx=100)

        self.password_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="password")
        self.password_textbox.pack(pady=15, padx=10, ipadx=100)

        self.button_log_in = customtkinter.CTkButton(
            master=self.frame_1, command=self.sign_in_func, text="log-in")
        self.button_log_in.pack(pady=10, padx=10)

        self.label_no_account = customtkinter.CTkLabel(master=self.frame_1, text="Don't have an account?", font=(
            "regular", 16))  # font name and size in px
        self.label_no_account.pack(pady=15, padx=10, ipadx=100)

        self.button_sign_up = customtkinter.CTkButton(
            master=self.frame_1, command=self.sign_up_window, text="sign-up")
        self.button_sign_up.pack(pady=10, padx=10)
        self.mainloop()

    def sign_in_func(self):
        self.username = str(self.username_textbox.get())
        self.password = str(self.password_textbox.get())
        if self.username == "":
            tk.messagebox.showerror('Error', 'username not entered!')
        elif self.password == "":
            tk.messagebox.showerror('Error', 'password not entered!')
        else:
            signed_in = Authorization(
                self.key, self.client_socket, self.username, self.password).sign_in()
            if signed_in:
                self.destroy()
                Main_Window(self.username, self.client_socket, self.key)
            else:
                tk.messagebox.showerror(
                    'Error', 'password or username is wrong!')

    def sign_up_window(self):
        self.destroy()
        Sign_Up_Window(self.client_socket, self.key)


class Sign_Up_Window(customtkinter.CTk):
    def __init__(self, client_socket, key):
        self.key = key
        self.client_socket = client_socket

        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")

        self.frame_1 = customtkinter.CTkFrame(
            master=self, width=200, height=3000)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_sign_up = customtkinter.CTkLabel(
            master=self.frame_1, text="Sign-Up", font=("regular", 30))  # font name and size in px
        self.label_sign_up.pack(pady=50, padx=10)

        self.username_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="username")
        self.username_textbox.pack(pady=15, padx=10, ipadx=100)

        self.password_textbox = customtkinter.CTkEntry(
            master=self.frame_1, placeholder_text="password")
        self.password_textbox.pack(pady=15, padx=10, ipadx=100)

        self.button_sign_up = customtkinter.CTkButton(
            master=self.frame_1, command=self.sing_up_func, text="sign-up")
        self.button_sign_up.pack(pady=10, padx=10)

        self.button_back = customtkinter.CTkButton(
            master=self.frame_1, command=self.back, text="back")
        self.button_back.pack(pady=10, padx=10)

        self.mainloop()

    def sing_up_func(self):
        self.username = str(self.username_textbox.get())
        self.password = str(self.password_textbox.get())
        signed_up = Authorization(
            self.key, self.client_socket, self.username, self.password).sign_up()
        if signed_up:
            self.destroy()
            Sign_In_Window(self.client_socket, self.key)

        else:
            tk.messagebox.showerror('Error', 'this username is exist!')

    def back(self):
        self.destroy()
        Sign_In_Window(self.client_socket, self.key)


class Main_Window(customtkinter.CTk):
    def __init__(self, username, client_socket, key):

        self.username = username
        self.client_socket = client_socket
        self.key = key

        super().__init__()
        self.title("MZVG_Project.py")
        self.geometry("780x520")
        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.exit)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=180, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Hello my friend", font=(
            "Roboto Medium", -20))  # font name and size in px
        self.label_1.pack(pady=10, padx=10)

        self.button_21 = customtkinter.CTkButton(
            master=self.frame_left, text="exit", command=self.exit)
        self.button_21.pack(pady=10, padx=20)

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_right ============

        self.upload_button = customtkinter.CTkButton(
            master=self.frame_right, text="upload file", fg_color=None,  command=self.upload)
        self.upload_button.grid(row=8, column=2, columnspan=1,
                                pady=20, padx=(23, 23), sticky="snwe")

        self.download_button = customtkinter.CTkButton(
            master=self.frame_right, text="download", command=self.download)
        self.download_button.grid(row=8, column=4, columnspan=2,
                                  pady=20, padx=(23, 23), sticky="snwe")

        self.delete_button = customtkinter.CTkButton(
            master=self.frame_right, text="delete", command=self.delete)
        self.delete_button.grid(row=8, column=6, columnspan=2,
                                pady=20, padx=(23, 23), sticky="snwe")

        self.Listbox = tk.Listbox(master=self)
        self.Listbox.grid(row=0, column=0, columnspan=2, padx=(
            220, 40), pady=(40, 80), sticky="nsew")

        self.all_files_list = str(Message_Manipulations(
            self.key, self.client_socket).receiving_message())
        self.all_files_list = self.all_files_list[1:-1]
        self.all_files_list_splited = self.all_files_list.split(", ")
        for filename in self.all_files_list_splited:
            self.Listbox.insert(END, filename[1:-1])

        self.mainloop()
        # set default values

    def upload(self):
        self.path_to_file = tk.filedialog.askopenfilename()
        self.splited_path = self.path_to_file.split("/")
        self.filename = self.splited_path[-1]
        self.my_file = Path(self.path_to_file)

        if self.my_file.is_file():

            self.file = open(self.path_to_file, "rb")
            self.file_data = self.file.read()
            self.file.close()

            Message_Manipulations(self.key, self.client_socket).sending_message(
                f"upload!!!{self.username}!!!{str(self.filename)}")

            Message_Manipulations(
                self.key, self.client_socket).sending_file(self.file_data)

            self.Listbox.insert(END, self.filename)

        else:
            print("not exist")

    def download(self):
        try:
            self.filename = self.Listbox.get(self.Listbox.curselection()[0])

            Message_Manipulations(self.key, self.client_socket).sending_message(
                f"download!!!{self.username}!!!{str(self.filename)}")
            self.received_file = Message_Manipulations(
                self.key, self.client_socket).receiving_file()

            self.file = open(str(self.filename), "wb")
            self.file.write(self.received_file)
            self.file.close()
        except:
            tk.messagebox.showerror('Error', 'File is not selected')

    def delete(self):
        try:
            self.filename = self.Listbox.get(self.Listbox.curselection()[0])

            Message_Manipulations(self.key, self.client_socket).sending_message(
                f"delete!!!{self.username}!!!{str(self.filename)}")

            self.delete_answer = Message_Manipulations(
                self.key, self.client_socket).receiving_message()

            if int(self.delete_answer) == 200:
                selected_checkboxs = self.Listbox.curselection()
                for selected_checkbox in selected_checkboxs[::-1]:
                    self.Listbox.delete(selected_checkbox)
            else:
                print("wrong!")
        except:
            tk.messagebox.showerror('Error', 'File is not selected')

    def exit(self):
        self.destroy()
        Sign_In_Window(self.client_socket, self.key)
