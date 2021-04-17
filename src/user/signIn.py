import tkinter as tk
import tkinter.font as tkFont
import sys
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
        entryFont = tkFont.Font(size=10)
        buttonFont = tkFont.Font(size=13)

        emailUser = tk.StringVar()
        pwUser = tk.StringVar()

        self.email = tk.Label(text="Email/Username", font=textFont)
        self.email.place(x=577, y=100)
        self.email1 = tk.Entry(textvariable=emailUser, font=entryFont)
        self.email1.place(x=540, y=135, width=210, height=27)

        self.pw = tk.Label(text="Password", font=textFont)
        self.pw.place(x=602, y=230)
        self.pw1 = tk.Entry(textvariable=pwUser, font=entryFont, show="*")
        self.pw1.place(x=540, y=265, width=210, height=27)

        self.sign_up = tk.Button(text="Sign Up", font=buttonFont, command=lambda: template.changePage(self, "sign up"))
        self.sign_up.place(x=420, y=350, width=90)

        self.forget_password = tk.Button(text="Forget Password", font=buttonFont, command=lambda: template.changePage(self, "forget password 1"))
        self.forget_password.place(x=750, y=350, width=150)

        self.submit = tk.Button(text="Submit", font=buttonFont)
        self.submit.place(x=597, y=470, width=100, height=40)

def startPage():
    root = tk.Tk()
    root.title("Testing")
    root.geometry("1920x1080")
    app = signIn(master = root)
    app.mainloop()