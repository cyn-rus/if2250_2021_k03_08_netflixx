import pytest
import re

data=[
    ["a@gmail.com", "aaa", "ini a", "aAaA", "01/01/2001", "user"],
    ["b@gmail.com", "bbb", "bukan b", "lalala", "02/02/2002", "admin"],
    ["c@gmail.com", "ccc", "saya c", "hemhemhem", "03/03/2003", "user"]
    ]

def isSignInValid(loginData, pw):
    listEmail = [row[0] for row in data]
    listPass = [row[3] for row in data]
    listUsername = [row[1] for row in data]

    if loginData == "" or pw == "":
        return False

    if loginData in listEmail or loginData in listUsername:
        try:
            idx = listEmail.index(loginData)
        except:
            idx = listUsername.index(loginData)
        
        if listPass[idx] == pw:
            return data[idx][5]
        else:
            return False
    else:
        return False

def checkPassword(pw, conf_pw):
    pwRule = [
            lambda s: any(x.isupper() for x in s),
            lambda s: any(x.isdigit() for x in s),
            lambda s: any(x.isalnum() for x in s),
            lambda s: not bool(re.match('^[a-zA-Z0-9]*$', s)),
            lambda s: len(s) >= 8,
                    ]

    if not all(rule(pw) for rule in pwRule):
        return False
    
    if pw != conf_pw:
        return False

    return True

def isSignUpValid(email, username, pw, conf_pw, name, dob):
    listEmail = [row[0] for row in data]
    listUsername = [row[1] for row in data]

    if email == "" or username == "" or pw == "" or conf_pw == "" or name == "":
        return False

    emailRegex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if not re.search(emailRegex, email):
        return False
    
    if email in listEmail:
        return False

    if " " in username:
        return False

    if username in listUsername:
        return False

    if not checkPassword(pw, conf_pw):
        return False

    formatDOB = dob.split("/")
    if (len(formatDOB[0]) == 1):
        formatDOB[0] = "0" + formatDOB[0]
    if (len(formatDOB[1]) == 1):
        formatDOB[1] = "0" + formatDOB[1]
    if (int(formatDOB[2]) <= 21):
        formatDOB[2] = "20" + formatDOB[2]
    else:
        formatDOB[2] = "19" + formatDOB[2]

    alteredDOB = formatDOB[1] + "/" + formatDOB[0] + "/" + formatDOB[2]

    return [email, username, name, pw, alteredDOB, "user"]

def sendEmail(email):
    listEmail = [row[0] for row in data]
    listNama = [row[2] for row in data]
    
    if email == "":
        return False
    
    try:
        idx = listEmail.index(email)
        return 123456
    except:
        return False

def reSendEmail(idx):
    listEmail = [row[0] for row in data]

    return sendEmail(listEmail[idx])

def validateCode(inputCode, code):
    if inputCode == "":
        return False
    
    if inputCode == str(code):
        return True
    else:
        return False

def changePassword(pw, confPw, idx):
    if pw == "" or confPw == "":
        return False

    if not checkPassword(pw, confPw):
        return False

    listEmail = [data[0] for row in data]

    data[idx][3] = pw
    return data[idx]

def test():
    assert isSignInValid("", "") == False
    assert isSignInValid("ddd", "aAaA") == False
    assert isSignInValid("d@gmail.com", "lalala") == False
    assert isSignInValid("b@gmail.com", "hemhemhem") == False
    assert isSignInValid("c@gmail.com", "apaya") == False
    assert isSignInValid("a@gmail.com", "aAaA") == "user"
    assert isSignInValid("bbb", "lalala") == "admin"

    assert checkPassword("HaHaHa", "HaHaHa") == False
    assert checkPassword("Abcdefghi1!", "abcedfghi1!") == False
    assert checkPassword("AbcDefGhi2@", "AbcDefGhi2@") == True

    assert isSignUpValid("", "", "", "", "", "") == False
    assert isSignUpValid("aaaaa", "lala", "LaLaLaLa3#", "LaLaLa3#", "waaa", "1/1/01") == False
    assert isSignUpValid("a@gmail.com", "lala", "LaLaLaLa3#", "LaLaLa3#", "waaa", "1/1/01") == False
    assert isSignUpValid("d@gmail.com", " ", "LaLaLaLa3#", "LaLaLa3#", "waaa", "1/1/01") == False
    assert isSignUpValid("d@gmail.com", "aaa", "LaLaLaLa3#", "LaLaLaLa3#", "waaa", "1/1/01") == False
    assert isSignUpValid("d@gmail.com", "ddd", "LaLaLaLa3#", "LaLaLaLa3#", "waaa", "1/1/01") == ["d@gmail.com", "ddd", "waaa", "LaLaLaLa3#", "01/01/2001", "user"]

    assert sendEmail("") == False
    assert sendEmail("huh@gmail.com") == False
    assert sendEmail("a@gmail.com") == 123456

    assert reSendEmail(0) == 123456

    assert validateCode("", 123456) == False
    assert validateCode("234567", 123456) == False
    assert validateCode("123456", 123456) == True

    assert changePassword("", "", 0) == False
    assert changePassword("MeongKucing5%", "MeongKucing5%", 0) == ["a@gmail.com", "aaa", "ini a", "MeongKucing5%", "01/01/2001"]