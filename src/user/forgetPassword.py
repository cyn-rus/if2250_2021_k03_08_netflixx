import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import yagmail
import random
from user.signUp import checkPassword
import sys
sys.path.insert(1, "..")
import template

class forgetPassword1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.forget_password()

    def forget_password(self):
        template.header("   forget  password")
        template.button_halaman_utama(self)

        textFont = tkFont.Font(family="TimeBurner", size=15, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=15, weight="bold")

        self.email = tk.Label(text="Masukkan Email/Username", font=textFont, bg="#24225e", fg="#9f64d8")
        self.email.place(x=522, y=200)
        self.email1 = tk.Entry(font=entryFont)
        self.email1.place(x=488, y=235, width=300, height=30)

        self.submit = tk.Button(text="Submit", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.sendEmail())
        self.submit.place(x=597, y=400, width=100, height=45)

    def sendEmail(self):
        data = template.readFile("user.csv")

        listEmail = [row[0] for row in data]
        listNama = [row[2] for row in data]
        
        email = self.email1.get()
        
        if email == "":
            tkMessageBox.showwarning("Netfl\'IXX\'", "Dimohonkan untuk mengisi semua data")
            return
        
        try:
            idx = listEmail.index(email)
        except:
            tkMessageBox.showerror("Netfl\'IXX\'", "Email tidak terdaftar")
            return
        
        try:
            generatedCode = sendEmail(listNama[idx], listEmail[idx])
            self.goToNextPage(generatedCode, idx)
        except:
            return

    def goToNextPage(self, code, idx):
        self.master.destroy()
        root = tk.Tk()
        root.title("Testing")
        root.geometry("1920x1080")
        root.configure(bg="#24225e")
        app = forgetPassword2(code, idx, master=root)
        app.mainloop()
    
class forgetPassword2(tk.Frame):
    def __init__(self, code, idx, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.forget_password2(code, idx)
    
    def forget_password2(self, code, idx):
        template.header("   forget  password")
        template.button_halaman_utama(self)

        textFont = tkFont.Font(family="TimeBurner", size=15, weight="bold")
        popupFont = tkFont.Font(family="TimeBurner", size=17, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")

        self.link = tk.Label(text="Kode reset password sudah dikirimkan melalui email", font=popupFont, bg="#24225e", fg="#9f64d8")
        self.link.place(x=400, y=100)
        self.after(2000, self.link.destroy)

        self.pin = tk.Label(text="Masukkan pin yang telah dikirim", font=textFont, bg="#24225e", fg="#9f64d8")
        self.pin.place(x=491, y=239)
        self.pin1 = tk.Entry(font=entryFont)
        self.pin1.place(x=580, y=275, width=100, height=30)

        self.resend = tk.Button(text="Kirim Ulang", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.reSendEmail(idx))
        self.resend.place(x=400, y=400, width=120, height=43)

        self.submit = tk.Button(text="Submit", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.validateCode(idx, code))
        self.submit.place(x=740, y=400, width=90, height=43)

    def reSendEmail(self, idx):
        data = template.readFile("user.csv")
        listNama = [row[2] for row in data]
        listEmail = [row[0] for row in data]
        
        try:
            generatedCode = sendEmail(listNama[idx], listEmail[idx])
            self.forget_password2(generatedCode, idx)
        except:
            return

    def validateCode(self, idx, code):
        inputCode = self.pin1.get()

        if inputCode == "":
            tkMessageBox.showwarning("Netfl\'IXX\'", "Dimohonkan untuk mengisi pinnya")
            return
        
        if inputCode == str(code):
            self.goToNextPage(idx)
        else:
            tkMessageBox.showerror("Netfl\'IXX\'", "Pin tidak sesuai")

    def goToNextPage(self, idx):
        self.master.destroy()
        root = tk.Tk()
        root.title("Testing")
        root.geometry("1920x1080")
        root.configure(bg="#24225e")
        app = forgetPassword3(idx, master=root)
        app.mainloop()

class forgetPassword3(tk.Frame):
    def __init__(self, idx, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.forget_password3(idx)
    
    def forget_password3(self, idx):
        template.header("   forget  password")
        template.button_halaman_utama(self)
        
        textFont = tkFont.Font(family="TimeBurner", size=15, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")

        self.pw = tk.Label(text="Password Baru", font=textFont, bg="#24225e", fg="#9f64d8")
        self.pw.place(x=563, y=200)
        self.pw1 = tk.Entry(font=entryFont, show="*")
        self.pw1.place(x=527, y=230, width=210, height=27)

        self.conf_pw = tk.Label(text="Konfirmasi Password Baru", font=textFont, bg="#24225e", fg="#9f64d8")
        self.conf_pw.place(x=510, y=300)
        self.conf_pw1 = tk.Entry(font=entryFont, show="*")
        self.conf_pw1.place(x=527, y=330, width=210, height=27)

        self.submit = tk.Button(text="Submit", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.changePassword(idx))
        self.submit.place(x=588, y=430, width=90, height=43)

    def changePassword(self, idx):
        pw = self.pw1.get()
        confPw = self.conf_pw1.get()

        if pw == "" or confPw == "":
            tkMessageBox.showwarning("Netfl\'IXX\'", "Dimohonkan untuk mengisi semua data")
            return

        if not checkPassword(pw, confPw):
            return

        tkMessageBox.showinfo("Netfl\'IXX\'", "Password berhasil diubah")
        data = template.readFile("user.csv")

        listEmail = [data[0] for row in data]

        print(idx, type(idx))
        data[idx][3] = pw
        template.reWriteFile(data, "user.csv")
        template.changePage(self, "halaman utama")

def sendEmail(receiverName, receiverEmail):
    RNGcode = random.randint(10**5, (10**6)-1)
    text = """\
                <html>
                <h2>Halo {name}!</h2>
                Pin reset passwordnya adalah {code}.</br>
                <b>Jangan bagikan pin ini ke siapapun, termasuk pihak Netfl\'IXX\'!</b>
                """.format(name=receiverName, code=RNGcode)
    sender = "donotreply.net.flixx@gmail.com"
    senderPW = "ixzwsyxuzsevoloz"

    # print(RNGcode)
    yag = yagmail.SMTP(user=sender, password=senderPW)
    yag.send(to=receiverEmail, subject="Netfl\'IXX\' Reset Password Request", contents=text)
    return RNGcode

def startPage():
    root = tk.Tk()
    root.title("Testing")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = forgetPassword1(master=root)
    app.mainloop()