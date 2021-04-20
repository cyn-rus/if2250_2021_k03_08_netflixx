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
        self.reviewPage()

    def calculateNewRating(id):
        DBfilm = template.readFile("film.csv")
        listid = [row[0] for row in DBfilm]
        listrate = [row[3] for row in DBfilm]

        jml = 0
        count = 0
        for i in range(len(listid)):
            if (listid[i] == id):
                jml += listrate[i]
                count += 1

        return jml/count
    
    # menyimpan hasil input review user ke dalam database review.csv
    def writeDBReview(self):
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
            tkmbox.showerror("Error Empty Review", "Your review text is still empty !")
            return
        
        # mereplace enter line menjadi one line atau satu kalimat
        teks_review = teks_review.replace('\n', ". ")

        # mendapatkan info pengguna 
        DBfilm2 = template.readFile("review.csv")
        listid = [row[0] for row in DBfilm2]
        listjdlFilm = [row[2] for row in DBfilm2]
        id = 1

        for item in listid:
            if (item == self.param[0]):
                id += 1

        # memasukkan ke dalam array
        self.DBfilm2 = []
        self.DBfilm2.append(self.param[0])           # dapat dari page film
        self.DBfilm2.append(self.param[1])           # dapat dari page sign in
        self.DBfilm2.append(listjdlFilm[id])
        self.DBfilm2.append(rate)
        self.DBfilm2.append(teks_review)

        # menuliskan ke dalam file review.csv
        template.writeFile(self.DBfilm2, "review.csv")

        # menampilkan message box review success !
        tkmbox.showinfo("Succesfully Added", "Your Review has been added ! \nThank you for reviewing !")
        
        # back to detail film page
        template.changePage(self, "detail film", self.calculateNewRating(self.param[0]))

    # menampilkan interface page review
    def reviewPage(self):
        # header film and button back film
        template.header("Add Review")
        fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
        bbackDetailFilm = tk.Button(text="Film", width=5, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: template.changePage(self, "detail film", self.calculateNewRating(self.param[0])))
        bbackDetailFilm.place(x=20, y=8)

        # judul film
        self.hReview = tk.Label(text = "Judul Film", bg = 'grey')
        self.hReview.place(x = 630, y = 70, width=405, height=50)

        # text rate this film
        self.lRate =  tk.Label(text = "Rate this film : ", bg = 'grey')
        self.lRate.place(x = 630, y= 130, width=405, height=50)

        # scroll for rating film
        self.scRate = tk.Scale(from_ = 0, to = 10, orient = "horizontal", activebackground = "grey")
        self.scRate.place(x = 630, y = 190, width= 405, height= 50)

        # text write your review
        self.lwReview =  tk.Label(text = "Write your review : ", bg = 'grey')
        self.lwReview.place(x = 630, y = 250, width=405, height= 50)

        # input entry review from user
        self.ewReview =  tksc.ScrolledText(bg ='grey')
        self.ewReview.place(x = 630, y = 310, width= 405, height= 320)
        self.ewReview.focus()

        # submit button
        self.sbButton = tk.Button(text = "Submit", bg = 'grey', command=lambda: self.writeDBReview())
        self.sbButton.place(x = 630, y = 640, width=170, height=50)

    def startPage():
        root = tk.Tk()
        root.title("Netfl'IXX'")
        root.geometry("1920x1080")
        root.configure(bg="#24225e")
        app = reviewPage(master = root)
        app.mainloop()