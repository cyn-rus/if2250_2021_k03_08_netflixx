import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkmbox
import tkinter.scrolledtext as tksc
import sys
sys.path.insert(1, "..")
import template

class reviewPage(tk.Frame):
    # inisiasi class
    def __init__(self, param, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.reviewPage(param)

    # menuliskan nilai rata2 baru dari film yang di review ke film.csv
    def calculateNewRating(self, id):
        DBrev = template.readFile("review.csv")
        DBfilmtemp = template.readFile("film.csv")

        id_name = DBfilmtemp[id][0]

        listid = [row[0] for row in DBrev]
        listrate = [row[3] for row in DBrev]

        jml = 0
        count = 0
        avg = 0
        for i in range(len(listid)):
            if (listid[i] == id_name):
                jml += int(listrate[i])
                count += 1
        if (count > 0):
            avg = jml/count
        else:
            avg = 0

        DBfilmtemp[id][4] = avg
        print(DBfilmtemp[id])
        
        template.reWriteFile(DBfilmtemp, "film.csv")
    
    # menyimpan hasil input review user ke dalam database review.csv
    def writeDBReview(self, param):
        # mengambil nilai dari setiap scale rating dan entry text review
        rate = self.scRate.get()
        teks_review = self.ewReview.get("1.0","end-1c")

        # check apakah entry hanya berisi space " "
        found = False
        for karakter in teks_review:
            if (karakter != ' '):
                found = True
        
        # exception ketika text review masih kosong atau berisi space saja
        if (not found or teks_review == ""):
            tkmbox.showerror("Netfl\'IXX\'", "Oops, sepertinya belum memberikan review")
            return
        
        # mereplace enter line menjadi one line atau satu kalimat
        teks_review = teks_review.replace('\n', ". ")

        # mendapatkan info pengguna 
        DBfilm2 = template.readFile("film.csv")
        listid = [row[0] for row in DBfilm2]
        listjdlFilm = [row[1] for row in DBfilm2]
        id = 1

        for item in listid:
            if (item == param[0]):
                id += 1

        # memasukkan ke dalam array
        self.DBfilm2 = []
        self.DBfilm2.append(param[0])           # dapat dari page film
        self.DBfilm2.append(param[1])           # dapat dari page sign in
        self.DBfilm2.append(listjdlFilm[id])
        self.DBfilm2.append(rate)
        self.DBfilm2.append(teks_review)

        # menuliskan ke dalam file review.csv
        template.writeFile(self.DBfilm2, "review.csv")

        # menuliskan rata - rata nilai rating terbaru
        self.calculateNewRating(id)

        # menampilkan message box review success !
        tkmbox.showinfo("Netfl\'IXX\'", "Review sudah ditambahkan.\nTerima kasih telah memberikan review!")
        
        # back to detail film page
        template.changePage(self, "detail film", param)

    # menampilkan interface page review
    def reviewPage(self, param):
        # header film and button back film
        template.header("add review")
        fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
        fontStyle2 = tkFont.Font(family="TimeBurner", size=11)
        bbackDetailFilm = tk.Button(text="Film", width=5, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: template.changePage(self, "detail film", param))
        bbackDetailFilm.place(x=20, y=8)

        # judul film
        self.hReview = tk.Label(text = "Judul Film", font=fontStyle, bg="#010109", fg="#9f64d8")
        self.hReview.place(x = 400, y = 70, width=405, height=50)

        # text rate this film
        self.lRate =  tk.Label(text = "Rate this film : ", font=fontStyle, bg="#010109", fg="#9f64d8")
        self.lRate.place(x = 400, y= 130, width=405, height=50)

        # scroll for rating film
        self.scRate = tk.Scale(from_ = 0, to = 10, orient = "horizontal")
        self.scRate.place(x = 400, y = 190, width= 405, height= 50)

        # text write your review
        self.lwReview =  tk.Label(text = "Write your review : ", font=fontStyle, bg="#010109", fg="#9f64d8")
        self.lwReview.place(x = 400, y = 250, width=405, height= 50)

        # input entry review from user
        self.ewReview =  tksc.ScrolledText(bg ='grey')
        self.ewReview.place(x = 400, y = 310, width= 405, height= 320)
        self.ewReview.focus()
        self.ewReview.configure(font=fontStyle2, bg="#010109", fg="#9f64d8")

        # submit button
        self.sbButton = tk.Button(text = "Submit", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: self.writeDBReview(param))
        self.sbButton.place(x = 400, y = 640, width=170, height=50)

def startPage(args):
    root = tk.Tk()
    root.title("Netfl'IXX'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = reviewPage(args, master = root)
    app.mainloop()