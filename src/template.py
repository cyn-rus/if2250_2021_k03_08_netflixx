import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import user.signIn as signIn
import user.mainPage as mainPage
import user.signUp as signUp
import user.forgetPassword as forgetPassword
import csv
import numpy as np

def header(page_name):
    header = tk.Label(text=page_name, bg="grey", height=3, width=500)
    header.place(x=0)
    header_text = tk.Label(text=page_name)
    header_text.config(font=("Moiser", 18), bg="grey")
    header_text.place(x=631, y=25, anchor="c")

def button_film(currPage):
    fontStyle = tkFont.Font(family="TimeBurner", size=10)
    button = tk.Button(text="Film", width=5, anchor="c", font=fontStyle, command=lambda: changePage(currPage, "film"))
    button.place(x=20, y=12)

def button_snack(currPage):
    fontStyle = tkFont.Font(size=10)
    button = tk.Button(text="Snack", width=6, anchor="c", font=fontStyle, command=lambda: changePage(currPage, "snack"))
    button.place(x=1207, y=12)

def button_halaman_utama(currPage):
    fontStyle = tkFont.Font(size=10)
    button = tk.Button(text="Halaman Utama", width=13, anchor="c", font=fontStyle, command=lambda: changePage(currPage, "halaman utama"))
    button.place(x=20, y=12)

def changePage(currPage, nextPage):
    if nextPage == "snack":
        tkMessageBox.showinfo("Netfl\'IXX\'", "Halaman ini sedang dalam perbaikan!")
        print("welp no")
    else:
        currPage.master.destroy()
        if nextPage == "sign in":
            signIn.startPage()
        elif nextPage == "halaman utama":
            mainPage.startPage()
        elif nextPage == "sign up":
            signUp.startPage()
        elif nextPage == "forget password":
            forgetPassword.startPage()
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