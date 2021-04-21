import tkinter as tk
import tkinter.font as tkFont
import sys
sys.path.insert(1, "..")
import template

class adminPage(tk.Frame):
    def __init__(self, user, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.admin_page(user)

    def admin_page(self, user):
        template.header("halaman admin")
        template.button_logout(self)
        fontStyle = tkFont.Font(family="TimeBurner", size=15, weight="bold")
        
        self.admin_film = tk.Button(text="Film", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "halaman admin film", user))
        self.admin_film.place(x=430, y=300, width=170, height=50, anchor="c")

        self.admin_snack = tk.Button(text="Snack", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "halaman admin snack"))
        self.admin_snack.place(x=830, y=300, width=170, height=50, anchor="c")

def startPage(args):
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = adminPage(args, master=root)
    app.mainloop()
