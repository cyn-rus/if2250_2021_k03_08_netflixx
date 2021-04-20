import tkinter as tk
import tkinter.font as tkFont
import tkinter.scrolledtext as tksc
import tkinter.messagebox as tkmbox
import sys
sys.path.insert(1, "..")
import template

class detailFilmPage(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.detailFilm()

    # mengeluarkan indeks ditemukannya IDFilm
    def getIdRowFilm(self, dataFilm, IDFilm):
        id = 1

        for item in dataFilm:
            if (item == IDFilm):
                return id
            id += 1
    
    def detailFilm(self):
        self.DBfilm1 = template.readFile("film.csv")
        # row 0 = baris non target, selain itu baris target
        # column 0 = 'ID_film'
        listid = [row[0] for row in self.DBfilm1]
        # column 1 = 'judul_film'
        listjdl = [row[1] for row in self.DBfilm1]
        # column 3 = 'rating_film'
        listrating = [row[3] for row in self.DBfilm1]
        # column 4 = 'batasan_umur'
        listbtsumur = [row[4] for row in self.DBfilm1]
        # column 5 = 'deksripsi'
        listdesc = [row[5] for row in self.DBfilm1]
        # column 7 = 'harga_film'
        listharga = [row[7] for row in self.DBfilm1]

        # indeks film yang didetailkan
        idx = self.getIdRowFilm(listid, "F7692")

        # passing array berupa idfilm dan username 
        info = ["F7692", "user9090"]

        # header film
        template.header("Detail Film")
        fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
        bbackFilm = tk.Button(text="Film", width=5, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: template.changePage(self, "film", info))
        bbackFilm.place(x=20, y=8)

        # page position
        # poster film
        self.img = tk.PhotoImage(file = r"../img/judul.png")
        img1 = self.img.subsample(2, 2)
        tk.Label(image = self.img).place(x = 630, y= 70, width= 200, height=390)

        # judul film
        self.jFilm = tk.Label(text = listjdl[idx], bg='green')
        self.jFilm.place(x = 840, y = 70, width=195, height= 30)

        # Text Batas usia film
        self.lAge = tk.Label(text = listbtsumur[idx], bg='green')
        self.lAge.place(x = 840, y = 110, width=92, height=30)

        # Text rating film
        self.lRating = tk.Label(text=listrating[idx], bg='green')
        self.lRating.place(x = 943, y = 110, width=92, height=30)

        # Text deskripsi film
        self.sDesc = tksc.ScrolledText(bg='green')
        self.sDesc.place(x= 840, y=150, width=195, height=250)
        # memasukan nilai deskripsi film ke dalam scrolled text
        self.sDesc.insert(tk.INSERT,listdesc[idx])
        # membuat scrolled text menjadi tidak bisa diedit
        self.sDesc.configure(state='disabled')

        # Text harga film
        self.lHarga = tk.Label(text = "Rp" + listharga[idx], bg='green')
        self.lHarga.place(x=840, y= 410, width=92, height=50)

        # Button beli film
        self.bbyFilm = tk.Button(text="Beli Film", bg='green', activebackground = "grey", command=lambda: template.changePage(self, "beli film", info))
        self.bbyFilm.place(x = 943, y = 410, width=92, height=50)

        # Button menambahkan review
        self.bReview = tk.Button(text="Add Review",bg='blue' , activebackground = "grey", command=lambda: template.changePage(self, "add review", info))
        self.bReview.place(x = 630, y = 470, width= 405, height=50)
        
        # Table list review semua pengguna
        self.tReview = tk.Label(text="tabel list review", bg= "Red")
        self.tReview.place(x= 630, y = 530, width=405, height= 260)

    def startPage():
        root = tk.Tk()
        root.title("Netfl'IXX'")
        root.geometry("1920x1080")
        root.configure(bg="#24225e")
        app = detailFilmPage(master = root)
        app.mainloop()