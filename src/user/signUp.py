import tkinter as tk
import tkcalendar
import tkinter.font as tkFont
import sys
sys.path.insert(1, "..")
import template

class signUp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.sign_up_page()

    def sign_up_page(self):
        template.header("sign up")
        template.button_halaman_utama(self)

        textFont = tkFont.Font(size=14)
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(size=13)

        userEmail = tk.StringVar()
        userUsername = tk.StringVar()
        userPw = tk.StringVar()
        userConfPw = tk.StringVar()
        userName = tk.StringVar()

        self.email = tk.Label(text="Email", font=textFont)
        self.email.place(x=610, y=70)
        self.email1 = tk.Entry(textvariable=userEmail, font=entryFont)
        self.email1.place(x=535, y=95, width=210)

        self.username = tk.Label(text="Username", font=textFont)
        self.username.place(x=590, y=130)
        self.username1 = tk.Entry(textvariable=userUsername, font=entryFont)
        self.username1.place(x=535, y=155, width=210)

        self.pw = tk.Label(text="Password", font=textFont)
        self.pw.place(x=593, y=190)
        self.pw1 = tk.Entry(textvariable=userPw, font=entryFont)
        self.pw1.place(x=535, y=215, width=210)

        self.conf_pw = tk.Label(text="Konfirmasi Password", font=textFont)
        self.conf_pw.place(x=550, y=250)
        self.conf_pw1 = tk.Entry(textvariable=userConfPw, font=entryFont)
        self.conf_pw1.place(x=535, y=275, width=210)

        self.name = tk.Label(text="Nama", font=textFont)
        self.name.place(x=613, y=310)
        self.name1 = tk.Entry(textvariable=userName, font=entryFont)
        self.name1.place(x=535, y=335, width=210)

        self.dob = tk.Label(text="Tanggal Lahir", font=textFont)
        self.dob.place(x=580, y=370)
        self.dob1 = tkcalendar.DateEntry(width=31, year=2021)
        self.dob1.place(x=535, y=395)

        self.submit = tk.Button(text="Submit", font=buttonFont)
        self.submit.place(x=590, y=480, width=100, height=40)

def startPage():
    root = tk.Tk()
    root.title("Testing")
    root.geometry("1920x1080")
    app = signUp(master = root)
    app.mainloop()