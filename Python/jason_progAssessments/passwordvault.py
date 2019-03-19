#passwordvault.py
#This python script allows users to save and extract password and username data they have saved
#Jason Poonia, 18 March 2019

#MODEULS
import os
import re
#LISTS
userlist = ["JASON", "HANRO", "ARYAN", "HASSAN158", "VIVEK"]
passwordlist = ["PASSWORD"]
adminlist = ["ADMIN"]
websitelist = []
web_usernamelist = []
web_passwordlist = []

print("WELCOME TO NEXUS PASSWORD PROTECTION VAULT")
print("HERE YOU WILL BE ABLE TO SECURELY SAVE AND PROTECT YOUR PASSWORDS WITHOUT HAVING THE NEED TO MEMORIZING ALL OF THEM")

def menuoptions():
    print("______________________\n")
    print("PASSWORD VAULT")
    print("______________________\n")
    print("1 | ADD WEBSITE CREDENTIALS")
    print("2 | VIEW WEBSITE CREDENTIALS")
    print("3 | SUMMARY OF CREDENTIALS")
    print("4 | EXIT")

def menu():
        x = input("ENTER 1 | 2 | 3 | 4\n")
        return x

def writetofile(web_username, web_password, website):
    websitelist.append(website)
    web_usernamelist.append(web_username)
    web_passwordlist.append(web_password)

def extractlist():
    for i in range(0, len(websitelist)):
        print("`````````````````````````````")
        print("WEBSITE: {}".format(websitelist[i]))
        print("USERNAME: {}".format(web_usernamelist[i]))
        print("PASSWORD: {}".format(web_passwordlist[i]))

def login():
    while True:
        user = str(input("USERNAME: \n")).upper()
        if not re.match("[a-zA-Z0-9_]", user):
            print("ENGLISH ALPHABET ONLY| NO SPACES/WHITESPACES | MAX 20 CHARACTERS")
        else:
            password =  str(input("PASSWORD: \n")).upper()
            if not re.match("[a-zA-Z0-9_]", password):
                print("ENGLISH ALPHABET ONLY | NO SPACES/WHITESPACES | MAX 20 CHARACTERS")
            elif user in userlist and password in passwordlist:
                print("AUTHENTICATION SUCCESFULL")
                break
            elif user in adminlist and password in passwordlist:
                print("ADMIN PRIVILGES GRANTED")
                global admin
                admin = "1"
                break
            else:
                print("AUTHENTICATION FAILED")

login()
menuoptions()

while True:
    task = menu()
    if task == "1":
        while True:
            website = str(input("WEBSITE: \n")).upper()
            web_username = str(input("USERNAME: \n")).upper()
            if not re.match("^[A-Za-z0-9]{1,32}$", web_username):
                print("ENGLISH ALPHABET ONLY| NO SPACES/WHITESPACES | MAX 32 CHARACTERS")
            else:
                web_password =  str(input("PASSWORD: \n")).upper()
                if not re.match("^[A-Za-z0-9]{1,32}$", web_password):
                    print("ENGLISH ALPHABET ONLY | NO SPACES/WHITESPACES | MAX 32 CHARACTERS")
                else:
                    writetofile(web_username, web_password, website)
                    break
    elif task == "2":
        extractlist()
    elif task == "3":
        if len(websitelist) == 0:
            print("NO SAVED CREDENTIALS")
        else:
            print("WEBSITES:",websitelist)
            print("USERNAMES:",web_usernamelist)
            print("PASSWORDS:",web_passwordlist)
    elif task == "4":
        login()
        menuoptions()
        menu()
    else:
        print("INPUT VALUE NOT ALLOWED | ENTER WHOLE NUMBER ONLY")
