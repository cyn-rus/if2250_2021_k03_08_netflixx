import pytest

DBrev = [
    ["F1234","eloco","itsgodzila",8,"Bagus cukup menarik bahagia"],
    ["avngrs","dseva","The Avengers",9,"interesting"],
    ["endgme","eloco","Avengers: Endgame",7,"the quality is good"],
    ["F1234","mirc","itsgodzila",5,"nani? why no godzila here"],
    ["endgme","noma","Avengers: Endgame",6,"the graphic is more worse"],
    ["F1234","palmo","itsgodzila",10,"perfect! I love this movie"],
    ["endgme","kiko","Avengers: Endgame",8,"it's good but not really good"],
    ["infwar","user9028","Avengers: Infinity War",9,"my name is"],
    ["F1234","user9090","itsgodzila",6,"adfasdfasdfasdf"],
    ["avngrs","user4040","The Avengers",10,"yesss haloooo"],
    ["F1234","user4040","itsgodzila",10,"uno Perfectooo !"]
]

DBfilm = [
    ["avngrs","The Avengers","avengers.jpg",2012,9.5,13,"Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",1275838,50000,"avengers.jpg"],
    ["endgme","Avengers: Endgame","endgame.jpg",2019,7.4,13,"After the devastating events of Avengers: Infinity War (2018). the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",856461,50000,"endgame.jpg"],
    ["infwar","Avengers: Infinity War","infinitywar.jpg",2018,8,13,"The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",0,50000,"infinitywar.jpg"],
    ["F1234","itsgodzila","itsgodzila.png",2019,7.8,18,"Kisah perjalanan sayuran kang kung di kota besar niwyok",10000000,160000,"itsgodzila.png"]
]

def calculateNewRating(id):
    listid = [row[0] for row in DBrev]
    listrate = [row[3] for row in DBrev]

    jml = 0
    count = 0
    avg = 0
    for i in range(len(listid)):
        if (listid[i] == id):
            jml += listrate[i]
            count += 1
    if (count > 0):
        avg = jml/count
    else:
        avg = 0
    
    return avg

# sementara karena rate dan teks_review diambil dari eksternal maka
# rate dan teks_review diambil dari parameter
# rate = scRate.get()
# teks_review = ewReview.get("1.0","end-1c")
def writeDBReview(param, rate, teks_review):
    # check apakah entry hanya berisi space " "
    found = False
    for karakter in teks_review:
        if (karakter != ' '):
            found = True
        
    # exception ketika text review masih kosong atau berisi space saja
    if (not found or teks_review == ""):
        return False
        
    # mereplace enter line menjadi one line atau satu kalimat
    teks_review = teks_review.replace('\n', ". ")

    # mendapatkan info pengguna 
    listid = [row[0] for row in DBfilm]
    listjdlFilm = [row[1] for row in DBfilm]

    found = False
    id = 0

    for i in range(len(listid)):
        if (listid[i] == param[0]):
            id = i
            found = True
            break

    if (not found):
        id = -1

    # memasukkan ke dalam array
    DBtemp = []
    DBtemp.append(param[0])           # dapat dari page film
    DBtemp.append(param[1])           # dapat dari page sign in
    DBtemp.append(listjdlFilm[id])
    DBtemp.append(rate)
    DBtemp.append(teks_review)

    return DBtemp

def test():
    assert calculateNewRating("") == 0
    assert calculateNewRating("F1001") == 0
    assert calculateNewRating("F1234") == 7.8
    assert calculateNewRating("avngrs") == 9.5
    assert calculateNewRating("endgme") == 7
    assert calculateNewRating("infwar") == 9

    assert writeDBReview([], 10, "") == False
    assert writeDBReview([], 6, "            ") == False
    assert writeDBReview(["avngrs","yharou",13], 8, "Hai what is your name?") == ["avngrs","yharou","The Avengers",8,"Hai what is your name?"]
