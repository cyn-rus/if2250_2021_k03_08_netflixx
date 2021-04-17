import tkinter as tk
import tkinter.font as tkFont
import template

class forgetPassword1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.forget_password()

    def forget_password(self):
        template.header(" forget  password")
        template.button_halaman_utama(self)

        textFont = tkFont.Font(size=15)
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(size=15)

        emailUser = tk.StringVar()

        self.email = tk.Label(text="Masukkan Email/Username", font=textFont)
        self.email.place(x=522, y=200)
        self.email1 = tk.Entry(textvariable=emailUser, font=entryFont)
        self.email1.place(x=488, y=235, width=300, height=30)

        self.submit = tk.Button(text="Submit", font=buttonFont)
        self.submit.place(x=597, y=400, width=100, height=45)

class forgetPassword2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.forget_password2()
    
    def forget_password2(self):
        template.header(" forget  password")
        template.button_halaman_utama(self)

        textFont = tkFont.Font(size=15)
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(size=13)

        self.link = tk.Label(text="Kode reset password sudah dikirimkan melalui email", font=textFont)
        self.link.place(x=400, y=100)
        self.after(2000, self.link.destroy)

        pinUser = tk.StringVar()

        self.pin = tk.Label(text="Masukkan pin yang telah dikirim", font=textFont)
        self.pin.place(x=491, y=239)
        self.pin1 = tk.Entry(textvariable=pinUser, font=entryFont)
        self.pin1.place(x=580, y=275, width=100, height=30)

        self.resend = tk.Button(text="Kirim Ulang", font=buttonFont)
        self.resend.place(x=400, y=400, width=120, height=43)

        self.submit = tk.Button(text="Submit", font=buttonFont)
        self.submit.place(x=740, y=400, width=90, height=43)

class forgetPassword3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.forget_password3()
    
    def forget_password3(self):
        template.header(" forget  password")
        template.button_halaman_utama(self)
        
        textFont = tkFont.Font(size=15)
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(size=13)

        pwUser = tk.StringVar()
        confPwUser = tk.StringVar()

        self.pw = tk.Label(text="Password Baru", font=textFont)
        self.pw.place(x=563, y=200)
        self.pw1 = tk.Entry(textvariable=pwUser, font=entryFont, show="*")
        self.pw1.place(x=527, y=230, width=210, height=27)

        self.conf_pw = tk.Label(text="Konfirmasi Password Baru", font=textFont)
        self.conf_pw.place(x=510, y=300)
        self.conf_pw1 = tk.Entry(textvariable=confPwUser, font=entryFont, show="*")
        self.conf_pw1.place(x=527, y=330, width=210, height=27)

        self.submit = tk.Button(text="Submit", font=buttonFont)
        self.submit.place(x=588, y=430, width=90, height=43)

def startPage():
    root = tk.Tk()
    root.title("Testing")
    root.geometry("1920x1080")
    app = forgetPassword1(master=root)
    app.mainloop()