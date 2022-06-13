import os
def register():
    userID = "1"
    userName = "Ersin"
    fingerHash = "0x1b"
    file = open("users.txt","a")
    file.write(userID)
    file.write(" ")
    file.write(userName)
    file.write(" ")
    file.write(fingerHash)
    file.write("\n")
    file.close()


def login():
    username = input("Please enter your username")
    password = input("Please enter your password")  
    for line in open("users.txt","r").readlines():
        users = line.split() # Split on the space, and store the results in a list of two strings
        if userID == users[0] and userName == users[1] and fingerHash == users[2] :




