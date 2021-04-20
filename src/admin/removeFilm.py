import tkinter as tk
import tkinter.messagebox as tkMessageBox
import tkinter.font as tkFont
from csv import reader
from datetime import datetime
import sys
sys.path.insert(1, "..")
import template

class removeFilm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.remove_film_page()

    def remove_film_page(self):
        template.header("remove film")
        template.button_halaman_admin_film(self)

        textFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")
        entryFont = tkFont.Font(size=13)
        buttonFont = tkFont.Font(family="TimeBurner", size=14, weight="bold")

        self.id = tk.Label(text="ID Film", font=textFont, bg="#24225e", fg="#9f64d8")
        self.id.place(x=610, y=70)
        self.id1 = tk.Entry(font=entryFont)
        self.id1.place(x=535, y=95, width=210, height=27)

        self.submit = tk.Button(text="Hapus Film", font=buttonFont, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.isRemoveFilmValid())
        self.submit.place(x=570, y=170, width=140, height=40)

    def isRemoveFilmValid(self):
        data = template.readFile("film.csv")
        idFilm = [row[0] for row in data]

        id = self.id1.get()

        for row in data:
            if id == row[0]:
                teks = ("Hapus film ini?\nID Film: "+row[0]+"\nJudul Film: "+row[1]
                + "\nTahun Rilis Film: "+row[3]+"\nRating Film: "+row[4]+"\nJumlah Ditonton: "+row[7])
                response = tkMessageBox.askyesno("Netfl\'IXX\'", teks)
                if response:
                    newFile = []
                    with open ("../database/film.csv", "r") as file:
                        isiFile = reader(file)
                        for row in isiFile:
                            if row[0] != id:
                                newFile.append(row)
                    # newFile = np.array(newFile)).tolist()
                    template.reWriteFile(newFile, "film.csv")
                    tkMessageBox.showinfo("Netfl\'IXX\'", "Film berhasil dihapus")

                    tanggal = datetime.today().strftime("%d/%m/%Y")
                    template.writeFile([tanggal, "remove"+" "+id], "xxxxxx.csv")

                    self.id1.delete(0, tk.END)
                return

        tkMessageBox.showwarning("Netfl\'IXX\'", "ID film tidak ditemukan")

def startPage():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = removeFilm(master = root)
    app.mainloop()