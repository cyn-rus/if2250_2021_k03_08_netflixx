import tkinter as tk
import tkinter.font as tkFont
import sys
sys.path.insert(1, "..")
import template

class mainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.main_page()

    def main_page(self):
        template.header("Halaman Utama")
        template.button_film(self)
        template.button_snack(self)
        fontStyle = tkFont.Font(size = 13)
        
        self.sign_in = tk.Button(text="Sign In", font=fontStyle, command=lambda: template.changePage(self, "sign in"))
        self.sign_in.place(x=625, y=200, width=140, height=50, anchor="c")

        self.sign_up = tk.Button(text="Sign Up", font=fontStyle)
        self.sign_up.place(x=625, y=300, width=140, height=50, anchor="c")

        self.forget = tk.Button(text="Forget Password", font=fontStyle)
        self.forget.place(x=625, y=400, width=150, height=50, anchor="c")

def startPage():
    root = tk.Tk()
    root.title("Testing")
    root.geometry("1920x1080")
    app = mainPage(master=root)
    app.mainloop()

# root = tk.Tk()
# root.title("Testing")
# root.geometry("1920x1080")
# app = mainPage(master=root)
# app.mainloop()