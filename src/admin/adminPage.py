import tkinter as tk
import tkinter.font as tkFont
import sys
sys.path.insert(1, "..")
import template

class adminPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.admin_page()

    def admin_page(self):
        template.header("halaman admin")
        fontStyle = tkFont.Font(family="TimeBurner", size=15, weight="bold")
        
        self.admin_film = tk.Button(text="Film", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "halaman admin film"))
        self.admin_film.place(x=483, y=300, width=170, height=50, anchor="c")

        self.admin_snack = tk.Button(text="Snack", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "halaman admin snack"))
        self.admin_snack.place(x=883, y=300, width=170, height=50, anchor="c")

def startPage():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = adminPage(master=root)
    app.mainloop()
