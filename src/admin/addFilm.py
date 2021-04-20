import tkinter as tk
import tkinter.messagebox as tkMessageBox
import tkinter.font as tkFont
from datetime import datetime
import re
import sys
sys.path.insert(1, "..")
import template

class addFilm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.add_film_page()

    def add_film_page(self):
        template.header("add film")
        template.button_halaman_admin_film(self)

        textFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")

        self.id = tk.Label(text="ID Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.id.place(x=270, y=70)
        self.id1 = tk.Entry(font=entryFont)
        self.id1.place(x=270, y=95, width=210, height=27)

        self.judul = tk.Label(text="Judul Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.judul.place(x=270, y=140)
        self.judul1 = tk.Entry(font=entryFont)
        self.judul1.place(x=270, y=165, width=210, height=27)

        self.tahun = tk.Label(text="Tahun Rilis Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.tahun.place(x=270, y=280)
        self.tahun1 = tk.Entry(font=entryFont)
        self.tahun1.place(x=270, y=305, width=210, height=27)

        self.umur = tk.Label(text="Batas Umur Penonton", font=textFont, bg="#24225e", fg="#9f64d8")
        self.umur.place(x=270, y=350)
        self.umur1 = tk.Entry(font=entryFont)
        self.umur1.place(x=270, y=375, width=210, height=27)

        self.harga = tk.Label(text="Harga Tiket Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.harga.place(x=270, y=420)
        self.harga1 = tk.Entry(font=entryFont)
        self.harga1.place(x=270, y=445, width=210, height=27)

        self.poster = tk.Label(text="Nama File Poster Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.poster.place(x=270, y=210)
        self.poster1 = tk.Entry(font=entryFont)
        self.poster1.place(x=270, y=235, width=210, height=27)

        self.film = tk.Label(text="Nama File Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.film.place(x=270, y=490)
        self.film1 = tk.Entry(font=entryFont)
        self.film1.place(x=270, y=515, width=210, height=27)

        self.deskripsi = tk.Label(text="Deskripsi Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.deskripsi.place(x=270, y=560)
        self.deskripsi1 = tk.Text(font=entryFont, wrap=tk.WORD)
        self.deskripsi1.place(x=270, y=585, width=840, height=42)

        self.submit = tk.Button(text="Add Film", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.isAddFilmValid())
        self.submit.place(x=590, y=650, width=140, height=40)

    def isAddFilmValid(self):
        data = template.readFile("film.csv")
        idFilm = [row[0] for row in data]

        id = self.id1.get()
        judul = self.judul1.get()
        poster = self.poster1.get()
        tahun = self.tahun1.get()
        umur = self.umur1.get()
        harga = self.harga1.get()
        deskripsi = self.deskripsi1.get("1.0", "end-1c")
        film = self.film1.get()

        if id == "" or judul == "" or poster == "" or tahun == "" or umur == "" or harga == "" or deskripsi == "" or film == "":
            tkMessageBox.showwarning("Netfl\'IXX\'", "Semua atribut film harus diisi")
            return
        
        if " " in id:
            tkMessageBox.showerror("Netfl\'IXX\'", "ID film tidak boleh mengandung spasi")
            return
        if id in idFilm:
            tkMessageBox.showerror("Netfl\'IXX\'", "ID film sudah ada di daftar film")
            return
        
        numberRegex = '^(0|[1-9][0-9]*)$'
        if not re.search(numberRegex, tahun):
            tkMessageBox.showerror("Netfl\'IXX\'", "Tahun rilis film harus berupa angka")
            return
        if not re.search(numberRegex, umur):
            tkMessageBox.showerror("Netfl\'IXX\'", "Batas umur penonton harus berupa angka")
            return
        if not re.search(numberRegex, harga):
            tkMessageBox.showerror("Netfl\'IXX\'", "Harga tiket film harus berupa angka")
            return

        template.writeFile([id, judul, poster, tahun, 0, umur, deskripsi, 0, harga, film], "film.csv")
        tkMessageBox.showinfo("Netfl\'IXX\'", "Film berhasil ditambahkan")

        tanggal = datetime.today().strftime("%d/%m/%Y")
        template.writeFile([tanggal, "add"+" "+id], "xxxxxx.csv")

        self.id1.delete(0, tk.END)
        self.judul1.delete(0, tk.END)
        self.poster1.delete(0, tk.END)
        self.tahun1.delete(0, tk.END)
        self.umur1.delete(0, tk.END)
        self.harga1.delete(0, tk.END)
        self.deskripsi1.delete("1.0", tk.END)
        self.film1.delete(0, tk.END)

def startPage():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = addFilm(master = root)
    app.mainloop()