import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import csv
import sys
import numpy as np
sys.path.insert(1, "..")
import template

class signIn(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.sign_in_page()


    def sign_in_page(self):
        template.header("sign in")
        template.button_halaman_utama(self)

        textFont = tkFont.Font(size=15)
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(size=13)

        self.email = tk.Label(text="Email/Username", font=textFont)
        self.email.place(x=577, y=100)
        self.email1 = tk.Entry(font=entryFont)
        self.email1.place(x=540, y=135, width=210, height=27)

        self.pw = tk.Label(text="Password", font=textFont)
        self.pw.place(x=602, y=230)
        self.pw1 = tk.Entry(font=entryFont, show="*")
        self.pw1.place(x=540, y=265, width=210, height=27)

        self.sign_up = tk.Button(text="Sign Up", font=buttonFont, command=lambda: template.changePage(self, "sign up"))
        self.sign_up.place(x=420, y=350, width=90)

        self.forget_password = tk.Button(text="Forget Password", font=buttonFont, command=lambda: template.changePage(self, "forget password 1"))
        self.forget_password.place(x=750, y=350, width=150)

        self.submit = tk.Button(text="Submit", font=buttonFont, command=lambda: self.isSignInValid())
        self.submit.place(x=597, y=470, width=100, height=40)

    def isSignInValid(self):
        data = template.readFile("user.csv")

        listEmail = [row[0] for row in data]
        listPass = [row[3] for row in data]
        listUsername = [row[1] for row in data]

        loginData = self.email1.get()
        pw = self.pw1.get()

        if loginData in listEmail or loginData in listUsername:
            try:
                idx = listEmail.index(loginData)
            except:
                idx = listUsername.index(loginData)
            
            if listPass[idx] == pw:
                template.changePage(self, "film")
            else:
                tkMessageBox.showinfo("Netfl\'IXX\'", "Email/Username tidak sesuai dengan Password")
        else:
            tkMessageBox.showinfo("Netfl\'IXX\'", "Email/Username tidak valid")

def startPage():
    root = tk.Tk()
    root.title("Testing")
    root.geometry("1920x1080")
    app = signIn(master = root)
    app.mainloop()