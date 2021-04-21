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
        template.header("halaman utama")
        template.button_film(self)
        template.button_snack(self)
        fontStyle = tkFont.Font(family="TimeBurner", size=15, weight="bold")
        
        self.sign_in = tk.Button(text="Sign In", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "sign in"))
        self.sign_in.place(x=770, y=200, width=170, height=50, anchor="c")

        self.sign_up = tk.Button(text="Sign Up", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "sign up"))
        self.sign_up.place(x=770, y=300, width=170, height=50, anchor="c")

        self.forget = tk.Button(text="Forget Password", font=fontStyle, bg="#010027", fg="#9f64d8", activebackground="#010027", activeforeground="#9f64d8", command=lambda: template.changePage(self, "forget password"))
        self.forget.place(x=770, y=400, width=170, height=50, anchor="c")

def startPage():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = mainPage(master=root)
    app.mainloop()