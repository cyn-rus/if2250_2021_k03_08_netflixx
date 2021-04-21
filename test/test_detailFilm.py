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
    ["F1234","user4040","itsgodzila",10,"uno Perfectooo !"],
    ["F1111","user1111","one",1,"uno one a sebuah"]
]

DBfilm = [
    ["avngrs","The Avengers","avengers.jpg",2012,9.5,13,"Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",1275838,50000,"avengers.jpg"],
    ["endgme","Avengers: Endgame","endgame.jpg",2019,7.4,13,"After the devastating events of Avengers: Infinity War (2018). the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",856461,50000,"endgame.jpg"],
    ["infwar","Avengers: Infinity War","infinitywar.jpg",2018,8,13,"The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",0,50000,"infinitywar.jpg"],
    ["F1234","itsgodzila","itsgodzila.png",2019,7.8,18,"Kisah perjalanan sayuran kang kung di kota besar niwyok",10000000,160000,"itsgodzila.png"],
    ["F1111","One","one.png",1,1,11,"One one one.. one one",111,111,"one.png"]
]


def getIdRowFilm(lisidfilm, param):
    found = False

    for i in range(len(lisidfilm)):
        if (lisidfilm[i] == param[0]):
            found = True
            return i
    if (not found):
        return -1

def isUserHasReview(param):
    listid = [row[0] for row in DBrev]
    listuser = [row[1] for row in DBrev]

    found = False

    for i in range (len(listuser)):
        if (param[1] == listuser[i] and param[0] == listid[i]):
            found = True
            break

    if (found):
        return False
    else:
        return True

def isUserAboveAge(param):
    listid = [row[0] for row in DBfilm]
    listbtsumur = [row[5] for row in DBfilm]

    idx = getIdRowFilm(listid, param)
    if(param[2] < int(listbtsumur[idx])):
        return False
    else:
        return True

def makeString(param):
    idx = param[0]
    first = False
    boxrev = ""

    for i in range(len(DBrev)):
        if (DBrev[i][0] == idx and not first):
            boxrev = "Username : " + DBrev[i][1] + "\n" + "Rating : " + str(DBrev[i][3]) + "/10 \n" + "Review : \n" + DBrev[i][4] + "\n \n"
            first = True
        elif(DBrev[i][0] == idx and first):
            boxrev = boxrev + ("Username : " + DBrev[i][1] + "\n" + "Rating : " + str(DBrev[i][3]) + "/10 \n" + "Review : \n" + DBrev[i][4] + "\n \n")
    return boxrev

def test():
    listidfilm = [row[0] for row in DBfilm]
    listidrev = [row[0] for row in DBrev]
    assert getIdRowFilm([],"") == -1
    assert getIdRowFilm(listidfilm,["avngrs","eloco",13]) == 0
    assert getIdRowFilm(listidfilm,["endgme","eloco",13]) == 1
    assert getIdRowFilm(listidfilm,["infwar","eloco",13]) == 2
    assert getIdRowFilm(listidfilm,["F1234","eloco",13]) == 3
    assert getIdRowFilm(listidfilm,["F1","eloco",13]) == -1
    assert getIdRowFilm([""],["F1","eloco",13]) == -1

    assert isUserHasReview(["F1234","eloco",13]) == False
    assert isUserHasReview(["avngrs","eloco",13]) == True
    assert isUserHasReview(["endgme","dseva",13]) == True

    assert isUserAboveAge(["avngrs","eloco",12]) == False
    assert isUserAboveAge(["avngrs","eloco",18]) == True

    assert makeString(["F9090","user9090",15]) == ""