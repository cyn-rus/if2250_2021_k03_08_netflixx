import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import admin.adminFilmPage as adminFilmPage
import admin.adminPage as adminPage
import admin.addFilm as addFilm
#import admin.removeFilm as removeFilm
#import admin.updateFilm as updateFilm
import csv
import numpy as np

def header(page_name):
    header = tk.Label(bg="#010027", height=3, width=500)
    header.place(x=0)
    header_text = tk.Label(text=page_name)
    header_text.config(font=("Moiser", 20), bg="#010027", fg="#9f64d8")
    header_text.place(x=631, y=25, anchor="c")

def button_logout(currPage):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Logout", width=6, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "logout"))
    button.place(x=1200, y=8)

def button_halaman_admin(currPage):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Halaman Admin", width=15, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "halaman admin"))
    button.place(x=20, y=9)

def button_halaman_admin_film(currPage):
    fontStyle = tkFont.Font(family="TimeBurner", size=11, weight="bold")
    button = tk.Button(text="Halaman Admin: Film", width=20, anchor="c", font=fontStyle, bg="#010109", fg="#9f64d8", activebackground="#010109", activeforeground="#9f64d8", command=lambda: changePage(currPage, "halaman admin film"))
    button.place(x=20, y=9)

def changePage(currPage, nextPage):
    if nextPage == "halaman admin snack":
        tkMessageBox.showinfo("Netfl\'IXX\'", "Halaman ini sedang dalam perbaikan!")
        print("welp no")
    else:
        currPage.master.destroy()
        if nextPage == "halaman admin":
            adminPage.startPage()
        elif nextPage == "halaman admin film":
            adminFilmPage.startPage()
        elif nextPage == "add film":
            addFilm.startPage()
        elif nextPage == "remove film":
            removeFilm.startPage()
        elif nextPage == "update film":
            updateFilm.startPage()
        else:
            print("welp there goes nothing")

def readFile(fileName):
    data = []
    with open ("../database/"+fileName, "r") as file:
        isiFile = csv.reader(file)
        for row in isiFile:
            data.append(row)

    return (np.array(data)).tolist()

def writeFile(data, fileName):
    with open("../database/"+fileName, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)
        file.close()

def reWriteFile(data, fileName):
    with open("../database/"+fileName, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
        file.close()