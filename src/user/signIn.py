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
        template.header("    sign in")
        template.button_halaman_utama(self)

        textFont = tkFont.Font(family="TimeBurner", size=15, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")

        self.email = tk.Label(text="Email/Username", font=textFont, bg="#24225e", fg="#9f64d8")
        self.email.place(x=574, y=100)
        self.email1 = tk.Entry(font=entryFont)
        self.email1.place(x=530, y=135, width=240, height=27)

        self.pw = tk.Label(text="Password", font=textFont, bg="#24225e", fg="#9f64d8")
        self.pw.place(x=599, y=230)
        self.pw1 = tk.Entry(font=entryFont, show="*")
        self.pw1.place(x=530, y=265, width=240, height=27)

        self.sign_up = tk.Button(text="Sign Up", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: template.changePage(self, "sign up"))
        self.sign_up.place(x=420, y=350, width=90)

        self.forget_password = tk.Button(text="Forget Password", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: template.changePage(self, "forget password 1"))
        self.forget_password.place(x=740, y=350, width=170)

        self.submit = tk.Button(text="Submit", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.isSignInValid())
        self.submit.place(x=597, y=470, width=100, height=40)

    def isSignInValid(self):
        data = template.readFile("user.csv")

        listEmail = [row[0] for row in data]
        listPass = [row[3] for row in data]
        listUsername = [row[1] for row in data]
        listRole = [row[5] for row in data]

        loginData = self.email1.get()
        pw = self.pw1.get()

        if loginData == "" or pw == "":
            tkMessageBox.showwarning("Netfl\'IXX\'", "Dimohonkan untuk mengisi semua data")
            return

        if loginData in listEmail or loginData in listUsername:
            try:
                idx = listEmail.index(loginData)
            except:
                idx = listUsername.index(loginData)
            
            if listPass[idx] == pw:
                if listRole[idx] == "user":
                    template.changePage(self, "film")
                elif listRole[idx] == "admin":
                    template.changePage(self, "halaman admin", listUsername[idx])
            else:
                tkMessageBox.showerror("Netfl\'IXX\'", "Email/Username tidak sesuai dengan Password")
        else:
            tkMessageBox.showerror("Netfl\'IXX\'", "Email/Username tidak terdaftar")

def startPage():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = signIn(master = root)
    app.mainloop()