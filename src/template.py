import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import user.signIn as signIn
import user.mainPage as mainPage
import user.signUp as signUp
import user.forgetPassword as forgetPassword
import admin.adminFilmPage as adminFilmPage
import admin.adminPage as adminPage
import admin.addFilm as addFilm
import admin.removeFilm as removeFilm
import admin.updateFilm as updateFilm
import detailFilm
import reviewFilm
import csv
import numpy as np

def header(page_name):
    header = tk.Label(bg="#010027", height=3, width=500)
    header.place(x=0)
    header_text = tk.Label(text=page_name)
    header_text.config(font=("Moiser", 20), bg="#010027", fg="#9f64d8")
    header_text.place(x=631, y=25, anchor="c")

def button_film(currPage):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Film", width=5, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "detail film"))
    button.place(x=20, y=8)

def button_snack(currPage):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Snack", width=6, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "snack"))
    button.place(x=1200, y=8)

def button_halaman_utama(currPage):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Halaman Utama", width=15, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "halaman utama"))
    button.place(x=20, y=9)

def button_logout(currPage):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Logout", width=8, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "logout"))
    button.place(x=1180, y=8)

def button_halaman_admin(currPage, user):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Halaman Admin", width=15, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "halaman admin", user))
    button.place(x=20, y=9)

def button_halaman_admin_film(currPage, user):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Halaman Admin: Film", width=20, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "halaman admin film", user))
    button.place(x=20, y=9)

def changePage(currPage, nextPage, *args):
    if nextPage == "snack" or nextPage == "halaman admin snack":
        tkMessageBox.showinfo("Netfl\'IXX\'", "Halaman ini sedang dalam perbaikan!")
        print("welp no")
    else:
        if nextPage == "logout":
            tkMessageBox.showinfo("Netfl\'IXX\'", "Anda berhasil keluar dari aplikasi")
        currPage.master.destroy()
        if nextPage == "sign in":
            signIn.startPage()
        elif nextPage == "halaman utama":
            mainPage.startPage()
        elif nextPage == "sign up":
            signUp.startPage()
        elif nextPage == "forget password":
            forgetPassword.startPage()
        elif nextPage == "halaman admin":
            adminPage.startPage(args[0])
        elif nextPage == "halaman admin film":
            adminFilmPage.startPage(args[0])
        elif nextPage == "add film":
            addFilm.startPage(args[0])
        elif nextPage == "remove film":
            removeFilm.startPage(args[0])
        elif nextPage == "update film":
            updateFilm.startPage(args[0])
        elif nextPage == "add review":
            reviewFilm.startPage(args[0])
        elif nextPage == "detail film":
            detailFilm.startPage(args[0])
        else:
            print("welp there goes nothing")

def readFile(fileName):
    data = []
    with open ("./database/"+fileName, "r") as file:
        isiFile = csv.reader(file)
        for row in isiFile:
            data.append(row)

    return (np.array(data)).tolist()

def writeFile(data, fileName):
    with open("./database/"+fileName, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)
        file.close()

def reWriteFile(data, fileName):
    with open("./database/"+fileName, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
        file.close()
