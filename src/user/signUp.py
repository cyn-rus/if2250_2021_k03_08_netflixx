import tkinter as tk
import tkinter.messagebox as tkMessageBox
import tkcalendar
import tkinter.font as tkFont
import re
import string
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
        template.header("  sign up")
        template.button_halaman_utama(self)

        textFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")

        self.email = tk.Label(text="Email", font=textFont, bg="#24225e", fg="#9f64d8")
        self.email.place(x=760, y=70)
        self.email1 = tk.Entry(font=entryFont)
        self.email1.place(x=685, y=95, width=210, height=27)

        self.username = tk.Label(text="Username", font=textFont, bg="#24225e", fg="#9f64d8")
        self.username.place(x=740, y=140)
        self.username1 = tk.Entry(font=entryFont)
        self.username1.place(x=685, y=165, width=210, height=27)

        self.pw = tk.Label(text="Password", font=textFont, bg="#24225e", fg="#9f64d8")
        self.pw.place(x=743, y=210)
        self.pw1 = tk.Entry(font=entryFont, show="*")
        self.pw1.place(x=685, y=235, width=210, height=27)

        self.conf_pw = tk.Label(text="Konfirmasi Password", font=textFont, bg="#24225e", fg="#9f64d8")
        self.conf_pw.place(x=700, y=280)
        self.conf_pw1 = tk.Entry(font=entryFont, show="*")
        self.conf_pw1.place(x=685, y=305, width=210, height=27)

        self.name = tk.Label(text="Nama", font=textFont, bg="#24225e", fg="#9f64d8")
        self.name.place(x=760, y=350)
        self.name1 = tk.Entry(font=entryFont)
        self.name1.place(x=685, y=375, width=210, height=27)

        self.dob = tk.Label(text="Tanggal Lahir", font=textFont, bg="#24225e", fg="#9f64d8")
        self.dob.place(x=730, y=420)
        self.dob1 = tkcalendar.DateEntry(width=31, height=27)
        self.dob1.place(x=685, y=445)

        self.submit = tk.Button(text="Submit", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.isSignUpValid())
        self.submit.place(x=740, y=520, width=100, height=40)

    def isSignUpValid(self):
        data = template.readFile("user.csv")
        listEmail = [row[0] for row in data]
        listUsername = [row[1] for row in data]

        email = self.email1.get()
        username = self.username1.get()
        pw = self.pw1.get()
        conf_pw = self.conf_pw1.get()
        name = self.name1.get()
        dob = self.dob1.get()

        if email == "" or username == "" or pw == "" or conf_pw == "" or name == "":
            tkMessageBox.showwarning("Netfl\'IXX\'", "Dimohonkan untuk mengisi semua data")
            return

        emailRegex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not re.search(emailRegex, email):
            tkMessageBox.showerror("Netfl\'IXX\'", "Email tidak valid")
            return
        
        if email in listEmail:
            tkMessageBox.showerror("Netfl\'IXX\'", "Email sudah terdaftar")
            return

        if " " in username:
            tkMessageBox.showerror("Netfl\'IXX\'", "Username tidak valid")
            return

        if username in listUsername:
            tkMessageBox.showerror("Netfl\'IXX\'", "Username sudah terdaftar")
            return

        if not checkPassword(pw, conf_pw):
            return

        formatDOB = dob.split("/")
        if (len(formatDOB[0]) == 1):
            formatDOB[0] = "0" + formatDOB[0]
        if (len(formatDOB[1]) == 1):
            formatDOB[1] = "0" + formatDOB[1]
        if (int(formatDOB[2]) <= 21):
            formatDOB[2] = "20" + formatDOB[2]
        else:
            formatDOB[2] = "19" + formatDOB[2]

        alteredDOB = formatDOB[1] + "/" + formatDOB[0] + "/" + formatDOB[2]

        template.writeFile([
            email, username, name, pw, alteredDOB, "user"
        ], "user.csv")
        template.changePage(self, "halaman utama")

def checkPassword(pw, conf_pw):
    pwRule = [
            lambda s: any(x.isupper() for x in s),
            lambda s: any(x.isdigit() for x in s),
            lambda s: any(x.isalnum() for x in s),
            lambda s: not bool(re.match('^[a-zA-Z0-9]*$', s)),
            lambda s: len(s) >= 8,
                    ]

    if not all(rule(pw) for rule in pwRule):
        tkMessageBox.showwarning("Netfl\'IXX\'", "Password minimal memiliki panjang 8, memiliki minimal 1 huruf kapital, 1 simbol spesial, dan 1 angka")
        return False
    
    if pw != conf_pw:
        tkMessageBox.showerror("Netfl\'IXX'", "Password dan konfirmasi password tidak sesuai")
        return False

    return True

def startPage():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = signUp(master = root)
    app.mainloop()