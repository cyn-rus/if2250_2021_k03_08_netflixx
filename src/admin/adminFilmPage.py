import tkinter as tk
import tkinter.font as tkFont
import sys
sys.path.insert(1, "..")
import template

class adminFilmPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.admin_film_page()

    def admin_film_page(self):
        template.header("halaman admin: film")
        fontStyle = tkFont.Font(family="TimeBurner", size=15, weight="bold")
        
        self.add_film = tk.Button(text="ADD", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "add film"))
        self.add_film.place(x=630, y=200, width=170, height=50, anchor="c")

        self.remove_film = tk.Button(text="REMOVE", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "remove film"))
        self.remove_film.place(x=630, y=300, width=170, height=50, anchor="c")

        self.update_film = tk.Button(text="UPDATE", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "update film"))
        self.update_film.place(x=630, y=400, width=170, height=50, anchor="c")

def startPage():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = adminFilmPage(master=root)
    app.mainloop()
