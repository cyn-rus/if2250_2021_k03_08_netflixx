# Netfl'IXX'
Aplikasi untuk menonton film bernama Netfl'IXX' yang memanfaatkan konsep prosedural dan bahasa pemrograman Python untuk implementasinya. Aplikasi ini dibuat untuk memenuhi tugas besar IF2250 - Rekayasa Perangkat Lunak

# Cara Menjalankan Program
## Prerequisite
- Minimal [Python 3](https://www.python.org/downloads/)
- [Tkinter](https://www.tutorialspoint.com/how-to-install-tkinter-in-python)
- [Yagmail](https://pypi.org/project/yagmail/)
- [Numpy](https://numpy.org/install/)
- [TkCalendar](https://pypi.org/project/tkcalendar/)

## Menjalankan Program
1. Clone project ini
2. Masuk ke dalam _directory_ src
`cd src`
3. Jalankan `python main.py`

# Daftar Modul
## Pembagian Modul
| Nama modul      |    NIM   | Nama                          |
| --------------- |:--------:| :-----------------------------|
| Film            | 13519148 | Muhammad Atthaumar Rifqy      |
| Review          | 13519159 | Benidictus Galih Mahar Putra  |
| Update Database | 13519137 | Siti Iedrania Azzariyat Akbar |
| User            | 13519118 | Cynthia Rusadi                |

## Tampilan Layar
### Halaman Utama
![alt text](doc/halaman_utama.jpg "Halaman Utama")

### Film

### Review

### Update Database
![alt text](doc/halaman_admin.png "Halaman Admin")
![alt text](doc/halaman_admin_film.png "Halaman Admin Film")
![alt text](doc/add_film.png "Add Film")
![alt text](doc/remove_film.png "Remove Film")
![alt text](doc/update_film.png "Update Film")
![alt text](doc/update_film_2.png "Update Film (2)")

### User
![alt text](doc/sign_in.jpg "Sign In")
![alt text](doc/sign_up.jpg "Sign Up")
![alt text](doc/forget_password.jpg "Forget Password")
![alt text](doc/forget_password_2.jpg "Forget Password (2)")
![alt text](doc/forget_password_3.jpg "Forget Password (3)")

# Basis Data
## Film
| id_film | judul       | poster_film | tahun_rilis | rating_film | batasan_umur | deskripsi | jumlah_tonton | harga_film | film |
| ------- |:----------- |:----------- |:-----------:|:-----------:|:------------:|:--------- |:-------------:|:----------:|:--- |
| avngrs  | The Avengers| avengers.png| 2021        | 9           | 13           | Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.| 1275838 | 50000 | avengers.jpg |
| endgme | Avengers: Endgame | endgame.png | 2019 | 7 | 13 | After the devastating events of Avengers: Infinity War (2018). the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe. | 856461 | 50000 | endgame.jpg|
| infwar | Avengers: Infinity War | infinitywar.png | 2018 | 9 | 13 | The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe. | 0 | 5000 | inifinitywar.jpg|
| F1234 | It's Godzila | itsgodzila.png | 2019 | 7.7 | 18 | Kisah perjalanan sayuran kang kung di kota besar niwyok. | 10000000 | 160000 | itsgodzila.png |

## Review
| ID_film | username | judul_film | rating_film | teks_review |
| ------- |:--------:|:----------:|:-----------:|:------------|
|F1234 | eloco | itsgoszila | 8 | Bagus cukup menarik bahagia |
|avngrs | dseva | The Avengers | 9 | interesting |
|endgme | eloco | Avengers: Endgame | 7 | the quality is good |
|F1234 | mirc | itsgodzila | 5 | nani? why no godzila here |
|endgme |noma |Avengers: Endgame | 6 |the graphic is more worse|
|F1234 |palmo | It's Godzila | 10 | perfect! I love this movie|
|endgme |kiko |Avengers: Endgame | 8 | it's good but not really good|
|infwar |user9028 |Avengers: Infinity War | 9 | my name is|

## User
|email|username|name|password|dob|role|
|-----|:------:|:--:|:------:|:-:|:--:|
|cyrus.orange41@gmail.com | eloco | cyn | Testes123# | 01/01/2001 | user |
|cyn.rusadi@gmail.com | dseva | cynrus | iniapaAn6^ | 05/07/2006 | admin |
|13519118@std.stei.itb.ac.id | mirc | gatau | iengAja0) | 17/08/1945 | user |
|meong@gmail.com,meonghihi | noma | Meong123@ | 01/04/2000 | user |
|anjing@informatika.itb.ac.id | palmo | anjing guk guk | GukGuk12345% | 06/04/1997 | user |
|tes@gmail.com,kiko | ini tes doang | Heiheihei7& | 07/04/2006 | user | 
|tupai@gmail.com,user9028 | saya tupai | Tupaitupai1! | 05/06/1998 | user |
|admin@gmail.com | xxxxxx | Admin | adminAdmin4$ | 10/10/2010 | admin |

## xxxxxx
|tanggal|type|
|-------|:--:|
|01/01/2020|add avngrs|
|02/01/2020|add endgme|
|20/04/2021|add infwar|
|20/04/2021|add test|
|20/04/2021|update test|
|20/04/2021|remove test|
|20/04/2021|add test1|
|20/04/2021|add test2|
|20/04/2021|remove test2|
|20/04/2021|update test1|
|20/04/2021|remove test1|
