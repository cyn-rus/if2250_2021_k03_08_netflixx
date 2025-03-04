import tkinter as tk
from tkinter.constants import FALSE
import tkinter.font as tkFont
import tkinter.scrolledtext as tksc
import tkinter.messagebox as tkmbox
import template

class detailFilmPage(tk.Frame):
    def __init__(self, param, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.detailFilm(param)

    # mengeluarkan indeks ditemukannya IDFilm
    def getIdRowFilm(self, dataFilm, IDFilm):
        found = False

        for i in range(len(dataFilm)):
            if (dataFilm[i] == IDFilm):
                found = True
                return i
        if (not found):
            return -1
    
    # mengecek apakah user pernah mereview detail film yang dipilih
    def isUserHasReview(self, param):
        DBrev = template.readFile("review.csv")
        listid = [row[0] for row in DBrev]
        listuser = [row[1] for row in DBrev]

        found = False

        for i in range (len(listuser)):
            if (param[1] == listuser[i] and param[0] == listid[i]):
                found = True
                break

        if (found):
            tkmbox.showerror("Netfl\'IXX\'", "Kamu belum tonton film ini atau sudah pernah memberi review")
            return
        else:
            template.changePage(self, "add review", param)

    # mengecek apakah user memiliki usia di atas kriteria usia film
    def isUserAboveAge(self, param):
        if(param[2] < int(self.listbtsumur[self.idx])):
            tkmbox.showerror("Netfl\'IXX\'", "Umur tidak mencukupi!")
            return
        else:
            template.changePage(self, "beli film", param)
        
    # menggabungkan semua list username, rating, dan review dari review.csv menjadi sebuah string
    def makeString(self, idfilm):
        DBrev1 = template.readFile("review.csv")
        first = False
        boxrev = ""
        for i in range(len(DBrev1)):
            if DBrev1[i][0] == idfilm:
                boxrev += ("Username : " + DBrev1[i][1] + "\n" + "Rating : " + DBrev1[i][3] + "/10\nReview :\n" + DBrev1[i][4] + "\n\n")
        return boxrev
    
    def detailFilm(self, param):
        self.DBfilm1 = template.readFile("film.csv")
        # row 0 = baris non target, selain itu baris target
        # column 0 = 'ID_film'
        self.listid = [row[0] for row in self.DBfilm1]
        # column 1 = 'judul_film'
        self.listjdl = [row[1] for row in self.DBfilm1]
        # column 2 = 'poster_film'
        self.listposter = [row[2] for row in self.DBfilm1]
        # column 3 = 'rating_film'
        self.listrating = [row[4] for row in self.DBfilm1]
        # column 4 = 'batasan_umur'
        self.listbtsumur = [row[5] for row in self.DBfilm1]
        # column 5 = 'deksripsi'
        self.listdesc = [row[6] for row in self.DBfilm1]
        # column 7 = 'harga_film'
        self.listharga = [row[8] for row in self.DBfilm1]

        # indeks film yang didetailkan
        self.idx = self.getIdRowFilm(self.listid, param[0])

        # header film
        template.header("detail film")
        fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
        fontStyle2 = tkFont.Font(family="TimeBurner", size=11)
        bbackFilm = tk.Button(text="Film", width=5, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: template.changePage(self, "film", param))
        bbackFilm.place(x=20, y=8)

        # page position
        # poster film
        self.img = tk.PhotoImage(file = r"../img/" + self.listposter[self.idx])
        self.img1 = self.img.subsample(5, 5)
        tk.Label(image = self.img).place(x = 550, y= 70, width= 200, height=390)

        # judul film
        self.jFilm = tk.Label(text = self.listjdl[self.idx], font=fontStyle, bg='#010109', fg="#9f64d8")
        self.jFilm.place(x = 760, y = 70, width=195, height= 30)

        # Text Batas usia film
        self.lAge = tk.Label(text = "Age " + self.listbtsumur[self.idx] + "+", font=fontStyle, bg='#010109', fg="#9f64d8")
        self.lAge.place(x = 760, y = 110, width=92, height=30)

        # Text rating film
        self.lRating = tk.Label(text=self.listrating[self.idx] + "/10", font=fontStyle, bg='#010109', fg="#9f64d8")
        self.lRating.place(x = 863, y = 110, width=92, height=30)

        # Text deskripsi film
        self.sDesc = tksc.ScrolledText(bg='#010109')
        self.sDesc.place(x= 760, y=150, width=195, height=250)
        # memasukan nilai deskripsi film ke dalam scrolled text
        self.sDesc.insert(tk.INSERT,"Description : \n" + self.listdesc[self.idx])
        # membuat scrolled text menjadi tidak bisa diedit
        self.sDesc.configure(state='disabled', font=fontStyle2, fg="#9f64d8")

        # Text harga film
        self.lHarga = tk.Label(text = "Rp" + self.listharga[self.idx], font=fontStyle, bg='#010109', fg="#9f64d8")
        self.lHarga.place(x=760, y= 410, width=92, height=50)

        # Button beli film
        self.bbyFilm = tk.Button(text="Beli Film", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.isUserAboveAge(param))
        self.bbyFilm.place(x = 863, y = 410, width=92, height=50)

        # Button menambahkan review
        self.bReview = tk.Button(text="Add Review", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.isUserHasReview(param))
        self.bReview.place(x = 550, y = 470, width= 405, height=50)
        
        # Table list review semua pengguna
        self.tReview = tksc.ScrolledText(bg='#010109')
        self.tReview.place(x= 550, y = 530, width=405, height= 260)
        # memasukan nilai review film ke dalam scrolled text
        self.tReview.insert(tk.INSERT, self.makeString(param[0]))
        # membuat scrolled text menjadi tidak bisa diedit
        self.tReview.configure(state='disabled', font=fontStyle2, fg="#9f64d8")

def startPage(args):
    root = tk.Tk()
    root.title("Netfl'IXX'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = detailFilmPage(args, master = root)
    app.mainloop()