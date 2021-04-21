import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from template import *

class daftarFilm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.daftar_film()

    def daftar_film(self):
        global menu
        global button_first
        global button_left
        global button_right
        global button_last
        global poster_film_one
        global poster_film_two
        global poster_film_three

        def get_daftar(nama_database):
            raw_database = readFile(nama_database)
            daftar = []
            for row in raw_database:
                frame_data = (row[0], row[1], row[2])
                daftar.append(frame_data)

            return daftar

        def create_menu(frame, data_film, start_index, button_font):
            global poster_film_one
            global poster_film_two
            global poster_film_three
            global raw_img_film_one
            global raw_img_film_two
            global raw_img_film_three
            global new_image_one
            global new_image_two
            global new_image_three

            menu = tk.Frame(frame, bg="#010027", relief=tk.RAISED)

            film_one = data_film[start_index]
            clickable_frame_one = tk.Frame(menu, bg="#010027")

            id_film_one = film_one[0]
            nama_film_one = film_one[1]

            raw_img_film_one = Image.open("../img/" + film_one[2])
            new_image_one = raw_img_film_one.resize((270, 400))
            poster_film_one = ImageTk.PhotoImage(new_image_one)

            button_poster_one = tk.Button(clickable_frame_one, image=poster_film_one, relief=tk.FLAT, bg="#010027", activebackground="#6a2ecd", cursor="hand2")
            button_name_one = tk.Button(clickable_frame_one, text=nama_film_one, font=button_font, fg="white", width=25, bg="#010027", activebackground="#6a2ecd", relief=tk.FLAT)

            if len(nama_film_one) > 25:
                button_name_one.configure(anchor=tk.W)

            button_poster_one.pack(pady=10)
            button_name_one.pack()

            # --------------------------------------------------------------------------------
            film_two = data_film[start_index + 1]
            clickable_frame_two = tk.Frame(menu, bg="#010027")

            id_film_two = film_two[0]
            nama_film_two = film_two[1]

            raw_img_film_two = Image.open("../img/" + film_two[2])
            new_image_two = raw_img_film_two.resize((270, 400))
            poster_film_two = ImageTk.PhotoImage(new_image_two)

            button_poster_two = tk.Button(clickable_frame_two, image=poster_film_two, relief=tk.FLAT, bg="#010027", activebackground="#010027", cursor="hand2")
            button_name_two = tk.Button(clickable_frame_two, text=nama_film_two, font=button_font, fg="white", width=25, bg="#010027", activebackground="#010027", cursor="hand2", relief=tk.FLAT)

            if len(nama_film_two) > 25:
                button_name_two.configure(anchor=tk.W)

            button_poster_two.pack(pady=10)
            button_name_two.pack()

            # --------------------------------------------------------------------------------
            film_three = data_film[start_index + 2]
            clickable_frame_three = tk.Frame(menu, bg="#010027")

            id_film_three = film_three[0]
            nama_film_three = film_three[1]

            raw_img_film_three = Image.open("../img/" + film_three[2])
            new_image_three = raw_img_film_three.resize((270, 400))
            poster_film_three = ImageTk.PhotoImage(new_image_three)

            button_poster_three = tk.Button(clickable_frame_three, image=poster_film_three, relief=tk.FLAT, bg="#010027", activebackground="#010027", cursor="hand2")
            button_name_three = tk.Button(clickable_frame_three, text=nama_film_three, font=button_font, fg="white", width=25, bg="#010027", activebackground="#010027", cursor="hand2", relief=tk.FLAT)

            if len(nama_film_three) > 25:
                button_name_three.configure(anchor=tk.W)

            button_poster_three.pack(pady=10)
            button_name_three.pack()

            # --------------------------------------------------------------------------------
            clickable_frame_one.grid(row=0, column=0, padx=20, pady=15)
            clickable_frame_two.grid(row=0, column=1, padx=20, pady=15)
            clickable_frame_three.grid(row=0, column=2, padx=20, pady=15)

            return menu

        header(page_name="            Daftar Film")
        button_film_font = tkFont.Font(family="TimeBurner", size=11, weight="bold")
        button_navigation_font = tkFont.Font(family="Moiser", size=20)

        daftar = get_daftar(nama_database="film.csv")
        first_index = 0
        last_index = len(daftar) - 3

        main_frame = tk.Frame(self.master, bg="#24225e")
        main_frame.pack(pady=120)

        menu = create_menu(frame=main_frame, data_film=daftar, start_index=0, button_font=button_film_font)
        menu.grid(row=0, column=2)

        def change_menu(index, menu):
            menu.grid_forget()

            menu = create_menu(frame=main_frame, data_film=daftar, start_index=index, button_font=button_film_font)
            button_first = tk.Button(main_frame, text='<<', font=button_navigation_font, relief=tk.FLAT,fg="#9f64d8", bg="#010027", activebackground="#6a2ecd", cursor="hand2", command=lambda: change_menu(first_index, menu))
            button_left = tk.Button(main_frame, text='<', font=button_navigation_font, relief=tk.FLAT,fg="#9f64d8", bg="#010027", activebackground="#6a2ecd", cursor="hand2", command=lambda: change_menu(index-1, menu))
            button_right = tk.Button(main_frame, text='>', font=button_navigation_font, relief=tk.FLAT,fg="#9f64d8", bg="#010027", activebackground="#6a2ecd", cursor="hand2", command=lambda: change_menu(index+1, menu))
            button_last = tk.Button(main_frame, text='>>', font=button_navigation_font, relief=tk.FLAT,fg="#9f64d8", bg="#010027", activebackground="#6a2ecd", cursor="hand2", command=lambda: change_menu(last_index, menu))

            if (index == first_index):
                button_first.configure(state=tk.DISABLED, cursor="")
                button_left.configure(state=tk.DISABLED, cursor="")
            if (index == last_index):
                button_right.configure(state=tk.DISABLED, cursor="")
                button_last.configure(state=tk.DISABLED, cursor="")

            button_first.grid(row=0, column=0, sticky=tk.E)
            button_left.grid(row=0, column=1, sticky=tk.E)
            menu.grid(row=0, column=2)
            button_right.grid(row=0, column=3, sticky=tk.W)
            button_last.grid(row=0, column=4, sticky=tk.W)

        button_first = tk.Button(main_frame, text='<<', font=button_navigation_font,fg="#010027", bg="#010027", activebackground="#6a2ecd", state=tk.DISABLED, relief=tk.FLAT)
        button_left = tk.Button(main_frame, text='<', font=button_navigation_font,fg="#010027", bg="#010027", activebackground="#6a2ecd", state=tk.DISABLED, relief=tk.FLAT)
        button_right = tk.Button(main_frame, text='>', font=button_navigation_font,fg="#9f64d8", bg="#010027", activebackground="#6a2ecd", cursor="hand2", relief=tk.FLAT, command=lambda: change_menu(1, menu))
        button_last = tk.Button(main_frame, text='>>', font=button_navigation_font,fg="#9f64d8", bg="#010027", activebackground="#6a2ecd", cursor="hand2", relief=tk.FLAT, command=lambda: change_menu(last_index, menu))

        button_first.grid(row=0, column=0, sticky=tk.E)
        button_left.grid(row=0, column=1, sticky=tk.E)
        button_right.grid(row=0, column=3, sticky=tk.W)
        button_last.grid(row=0, column=4, sticky=tk.W)

def startPageDaftarFilm():
    root = tk.Tk()
    root.title("Netfl\'IXX\'")
    root.geometry("1920x1080")
    root.configure(bg="#24225e")
    app = daftarFilm(master=root)
    app.mainloop()

startPageDaftarFilm()