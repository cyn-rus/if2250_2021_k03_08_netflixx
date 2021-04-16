import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.main_page()

    def main_page(self):
        self.film = tk.Button(self, text="Film")
        self.sign_in = tk.Button(self, text="Sign In", command=self.sign_in_page)
        self.sign_in.pack(side="top")
        self.sign_up = tk.Button(self, text="Sign Up")
        self.forget = tk.Button(self, text="Forget Password")

    def sign_in_page(self):
        self.halaman_utama = tk.Button(self, text="Halaman Utama", command=self.main_page)
        self.halaman_utama.pack(side="bottom")

root = tk.Tk()
root.title("Testing")
root.geometry("1440x1024")
app = MainPage(master = root)
app.mainloop()

