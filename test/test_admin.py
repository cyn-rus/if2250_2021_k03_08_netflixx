import pytest
import re

data = [
    ["id1","judul1","1.jpg","2001","1","13","deskripsi1","10","50000","1.jpg"], 
    ["id2","judul2","2.jpg","2002","2","14","deskripsi2","20","100000","2.jpg"], 
    ["id3","judul3","3.jpg","2003","3","15","deskripsi3","30","150000","3.jpg"]
    ]

def isAddFilmValid(user, id, judul, poster, tahun, umur, harga, deskripsi, film):
    idFilm = [row[0] for row in data]

    if id == "" or judul == "" or poster == "" or tahun == "" or umur == "" or harga == "" or deskripsi == "" or film == "":
        return False
    
    if " " in id:
        return False
    if id in idFilm:
        return False
    
    numberRegex = '^(0|[1-9][0-9]*)$'
    if not re.search(numberRegex, tahun):
        return False
    if not re.search(numberRegex, umur):
        return False
    if not re.search(numberRegex, harga):
        return False
    
    #data.append([id, judul, poster, tahun, "0", umur, deskripsi, "0", harga, film])

    return ["add"+" "+id, user+".csv", [id, judul, poster, tahun, "0", umur, deskripsi, "0", harga, film]]

def isRemoveFilmValid(user, id):
    idFilm = [row[0] for row in data]

    for row in data:
        if id == row[0]:
            """ newFile = []
            for row in data:
                if row[0] != id:
                    newFile.append(row)
            data = newFile """
            return ["remove"+" "+id, user+".csv", row]

    return False

def isIDFilmValid(user, id):
    idFilm = [row[0] for row in data]

    if id not in idFilm:
        return False
    
    return id

def isUpdateFilmValid(user, id, judul, poster, tahun, umur, harga, deskripsi, film):
    idFilm = [row[0] for row in data]

    if id == "" or judul == "" or poster == "" or tahun == "" or umur == "" or harga == "" or deskripsi == "" or film == "":
        return False

    if id not in idFilm:
        return False
    
    if " " in id:
        return False
    
    numberRegex = '^(0|[1-9][0-9]*)$'
    if not re.search(numberRegex, tahun):
        return False
    if not re.search(numberRegex, umur):
        return False
    if not re.search(numberRegex, harga):
        return False
    
    for row in data:
        if id == row[0]:
            updated = [id, judul, poster, tahun, row[4], umur, deskripsi, row[7], harga, film]
            """ newFile = []
            for row in data:
                if row[0] != id:
                    newFile.append(row)
                else:
                    newFile.append(updated)
            data = newFile """
            return ["update"+" "+id, user+".csv", row, updated]
    

def test():
    assert isAddFilmValid("xxxxxx", "id4", "judul4", "4.jpg", "2004", "16", "200000", "deskripsi4", "") == False
    assert isAddFilmValid("xxxxxx", "id 4", "judul4", "4.jpg", "2004", "16", "200000", "deskripsi4", "4.jpg") == False
    assert isAddFilmValid("xxxxxx", "id2", "judul4", "4.jpg", "2004", "16", "200000", "deskripsi4", "4.jpg") == False
    assert isAddFilmValid("xxxxxx", "id4", "judul4", "4.jpg", "empat", "16", "200000", "deskripsi4", "4.jpg") == False
    assert isAddFilmValid("xxxxxx", "id4", "judul4", "4.jpg", "2004", "empat", "200000", "deskripsi4", "4.jpg") == False
    assert isAddFilmValid("xxxxxx", "id4", "judul4", "4.jpg", "2004", "16", "empat", "deskripsi4", "4.jpg") == False
    hasiladd = ["add id4", "xxxxxx.csv", ["id4", "judul4", "4.jpg", "2004", "0", "16", "deskripsi4", "0", "200000", "4.jpg"]]
    assert isAddFilmValid("xxxxxx", "id4", "judul4", "4.jpg", "2004", "16", "200000", "deskripsi4", "4.jpg") == hasiladd
    #assert isIDFilmValid("xxxxxx", "id4") == "id4"
    
    assert isRemoveFilmValid("xxxxxx", "id5") == False
    hasilremove = ["remove id1", "xxxxxx.csv", ["id1","judul1","1.jpg","2001","1","13","deskripsi1","10","50000","1.jpg"]]
    assert isRemoveFilmValid("xxxxxx", "id1") == hasilremove
    #assert isIDFilmValid("xxxxxx", "id1") == False

    assert isIDFilmValid("xxxxxx", "id6") == False
    assert isIDFilmValid("xxxxxx", "id3") == "id3"

    assert isUpdateFilmValid("xxxxxx", "id6", "judul5", "5.jpg", "2005", "17", "250000", "deskripsi5", "5.jpg") == False
    assert isUpdateFilmValid("xxxxxx", "id3", "judul5", "5.jpg", "2005", "17", "250000", "deskripsi5", "") == False
    assert isUpdateFilmValid("xxxxxx", "id3", "judul5", "5.jpg", "lima", "17", "250000", "deskripsi5", "5.jpg") == False
    assert isUpdateFilmValid("xxxxxx", "id3", "judul5", "5.jpg", "2005", "lima", "250000", "deskripsi5", "5.jpg") == False
    assert isUpdateFilmValid("xxxxxx", "id3", "judul5", "5.jpg", "2005", "17", "lima", "deskripsi5", "5.jpg") == False
    row3 = ["id3","judul3","3.jpg","2003","3","15","deskripsi3","30","150000","3.jpg"]
    now3 = ["id3","judul5","5.jpg","2005","3","17","deskripsi5","30","250000","5.jpg"]
    hasilupdate = ["update id3", "xxxxxx.csv", row3, now3]
    assert isUpdateFilmValid("xxxxxx", "id3", "judul5", "5.jpg", "2005", "17", "250000", "deskripsi5", "5.jpg") == hasilupdate
