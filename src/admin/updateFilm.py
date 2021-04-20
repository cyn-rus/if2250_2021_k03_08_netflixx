import tkinter as tk
import tkinter.messagebox as tkMessageBox
import tkinter.font as tkFont
from csv import reader
from datetime import datetime
import re
import sys
sys.path.insert(1, "..")
import template

class updateFilm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.update_film_page()

    def update_film_page(self):
        template.header("update film")
        template.button_halaman_admin_film(self)

        textFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")

        self.id = tk.Label(text="ID Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.id.place(x=140, y=70)
        self.id1 = tk.Entry(font=entryFont)
        self.id1.place(x=140, y=95, width=210, height=27)

        self.submit = tk.Button(text="Pilih Film", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.isIDFilmValid())
        self.submit.place(x=800, y=75, width=140, height=40)
    
    def isIDFilmValid(self):
        data = template.readFile("film.csv")
        idFilm = [row[0] for row in data]
        id = self.id1.get()

        if id not in idFilm:
            tkMessageBox.showwarning("Netfl\'IXX\'", "ID film tidak ditemukan")
            return
        
        textFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")
        textFont2 = tkFont.Font(family="TimeBurner", size=13, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")

        judulFilm = [row[1] for row in data]
        posterFilm = [row[2] for row in data]
        tahunFilm = [row[3] for row in data]
        umurFilm = [row[5] for row in data]
        deskripsiFilm = [row[6] for row in data]
        hargaFilm = [row[8] for row in data]
        filmFilm = [row[9] for row in data]
        i = idFilm.index(id)
        
        self.submit.destroy()
        self.back = tk.Button(text="Cari Film Lain", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: template.changePage(self, "update film"))
        self.back.place(x=800, y=75, width=140, height=40)
        
        # label
        self.id1.destroy()
        self.id1 = tk.Label(text=id, font=textFont2, bg="#24225e", fg="#9f64d8")
        self.id1.place(x=140, y=95)

        self.judul = tk.Label(text="Judul Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.judul.place(x=140, y=140)
        self.judul1 = tk.Label(text=judulFilm[i], font=textFont2, bg="#24225e", fg="#9f64d8")
        self.judul1.place(x=140, y=165)

        self.poster = tk.Label(text="Nama File Poster Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.poster.place(x=140, y=210)
        self.poster1 = tk.Label(text=posterFilm[i], font=textFont2, bg="#24225e", fg="#9f64d8")
        self.poster1.place(x=140, y=235)

        self.tahun = tk.Label(text="Tahun Rilis Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.tahun.place(x=140, y=280)
        self.tahun1 = tk.Label(text=tahunFilm[i], font=textFont2, bg="#24225e", fg="#9f64d8")
        self.tahun1.place(x=140, y=305)

        self.umur = tk.Label(text="Batas Umur Penonton", font=textFont, bg="#24225e", fg="#9f64d8")
        self.umur.place(x=140, y=350)
        self.umur1 = tk.Label(text=umurFilm[i], font=textFont2, bg="#24225e", fg="#9f64d8")
        self.umur1.place(x=140, y=375)

        self.harga = tk.Label(text="Harga Tiket Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.harga.place(x=140, y=420)
        self.harga1 = tk.Label(text=hargaFilm[i], font=textFont2, bg="#24225e", fg="#9f64d8")
        self.harga1.place(x=140, y=445)

        self.deskripsi = tk.Label(text="Deskripsi Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.deskripsi.place(x=140, y=490)
        self.deskripsi1 = tk.Label(text=deskripsiFilm[i][0:50]+"...", font=textFont2, bg="#24225e", fg="#9f64d8", wraplength=500, justify=tk.LEFT)
        self.deskripsi1.place(x=140, y=515)

        self.film = tk.Label(text="Teks Isi Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.film.place(x=140, y=560)
        self.film1 = tk.Label(text=filmFilm[i], font=textFont2, bg="#24225e", fg="#9f64d8")
        self.film1.place(x=140, y=585)

        # entry
        self.njudul = tk.Label(text="Judul Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.njudul.place(x=670, y=140)
        self.njudul1 = tk.Entry(font=entryFont)
        self.njudul1.place(x=670, y=165, width=210, height=27)

        self.nposter = tk.Label(text="Nama File Poster Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.nposter.place(x=670, y=210)
        self.nposter1 = tk.Entry(font=entryFont)
        self.nposter1.place(x=670, y=235, width=210, height=27)

        self.ntahun = tk.Label(text="Tahun Rilis Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.ntahun.place(x=670, y=280)
        self.ntahun1 = tk.Entry(font=entryFont)
        self.ntahun1.place(x=670, y=305, width=210, height=27)

        self.numur = tk.Label(text="Batas Umur Penonton", font=textFont, bg="#24225e", fg="#9f64d8")
        self.numur.place(x=670, y=350)
        self.numur1 = tk.Entry(font=entryFont)
        self.numur1.place(x=670, y=375, width=210, height=27)

        self.nharga = tk.Label(text="Harga Tiket Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.nharga.place(x=670, y=420)
        self.nharga1 = tk.Entry(font=entryFont)
        self.nharga1.place(x=670, y=445, width=210, height=27)

        self.ndeskripsi = tk.Label(text="Deskripsi Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.ndeskripsi.place(x=670, y=490)
        self.ndeskripsi1 = tk.Entry(font=entryFont)
        self.ndeskripsi1.place(x=670, y=515, width=540, height=27)

        self.nfilm = tk.Label(text="Nama File Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.nfilm.place(x=670, y=560)
        self.nfilm1 = tk.Entry(font=entryFont)
        self.nfilm1.place(x=670, y=585, width=540, height=27)

        self.submit = tk.Button(text="Update Film", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.isUpdateFilmValid())
        self.submit.place(x=590, y=650, width=140, height=40)
    
    def isUpdateFilmValid(self):
        data = template.readFile("film.csv")
        idFilm = [row[0] for row in data]

        id = self.id1["text"]
        judul = self.njudul1.get()
        poster = self.nposter1.get()
        tahun = self.ntahun1.get()
        umur = self.numur1.get()
        harga = self.nharga1.get()
        deskripsi = self.ndeskripsi1.get()
        film = self.nfilm1.get()

        if id == "" or judul == "" or poster == "" or tahun == "" or umur == "" or harga == "" or deskripsi == "" or film == "":
            tkMessageBox.showwarning("Netfl\'IXX\'", "Semua data film harus diisi")
            return
        
        if id not in idFilm:
            tkMessageBox.showwarning("Netfl\'IXX\'", "ID film tidak ditemukan")
            return
        
        if " " in id:
            tkMessageBox.showerror("Netfl\'IXX\'", "ID film tidak boleh mengandung spasi")
            return
        
        numberRegex = '^(0|[1-9][0-9]*)$'
        if not re.search(numberRegex, tahun):
            tkMessageBox.showerror("Netfl\'IXX\'", "Tahun rilis film harus berupa angka")
            return
        if not re.search(numberRegex, umur):
            tkMessageBox.showerror("Netfl\'IXX\'", "Batas umur penonton harus berupa angka")
            return
        if not re.search(numberRegex, harga):
            tkMessageBox.showerror("Netfl\'IXX\'", "Harga film harus berupa angka")
            return
        
        for row in data:
            if id == row[0]:
                teks = ("Perbaharui film ini?\nID Film: "+row[0]+"\nJudul Film: "+row[1]
                + "\nTahun Rilis Film: "+row[3]+"\nRating Film: "+row[4]+"\nJumlah Ditonton: "+row[7])
                response = tkMessageBox.askyesno("Netfl\'IXX\'", teks)
                if response:
                    newFile = []
                    with open ("../database/film.csv", "r") as file:
                        isiFile = reader(file)
                        for row in isiFile:
                            if row[0] != id:
                                newFile.append(row)
                            else:
                                updated = [id, judul, poster, tahun, row[4], umur, deskripsi, row[7], harga, film]
                                newFile.append(updated)
                    # newFile = np.array(newFile)).tolist()
                    template.reWriteFile(newFile, "film.csv")
                    tkMessageBox.showinfo("Netfl\'IXX\'", "Film berhasil diperbaharui")

                    tanggal = datetime.today().strftime("%d/%m/%Y")
                    template.writeFile([tanggal, "update"+" "+id], "xxxxxx.csv")

                    template.changePage(self, "update film")

def startPage():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = updateFilm(master = root)
    app.mainloop()