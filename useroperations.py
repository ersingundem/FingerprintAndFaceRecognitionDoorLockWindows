import cv2
import os
import face_training
import numpy as np
from pandastable import Table
from tkinter import ttk

from PIL import Image
from tkinter import *
import tkinter as tk
from cryptography.fernet import Fernet
import fingerprint
import shutil

path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()


def createuserfacedataset(userid):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    face_id = userid

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")

    count = 0

    while (True):

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff
        if k == 27:
            break
        elif count >= 30:
            break

    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()


def trainfacemodels():
    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, ids = face_training.getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


def createnewuser():
    userName = newusername.get()
    names = []
    with open(r'usernames', 'r') as fp:
        for line in fp:
            x = line[:-1]
            names.append(x)

    names.append(userName)
    with open(r'usernames', 'w') as fp:
        for item in names:
            fp.write("%s\n" % item)
    message.set("Please add your biometric datas.")
    userId = names.index(userName)
    print(userName)
    print(userId)
    createuserfacedataset(userId)
    trainfacemodels()

    create_user.destroy()



def createnewuserpage():
    menu.destroy()
    global create_user
    create_user = Tk()
    create_user.title("Create New User")
    create_user.geometry("300x250")
    global message;
    global newusername;
    newusername = StringVar()
    message = StringVar()
    Label(create_user, width="300", text="Please enter details below", bg="orange", fg="white").pack()
    Label(create_user, text="New User Name: ").place(x=20, y=40)
    Entry(create_user, textvariable=newusername).place(x=120, y=42)
    Label(create_user, text="", textvariable=message).place(x=95, y=100)
    Button(create_user, text="Save and Next", width=15, height=1, bg="orange", command=createnewuser).place(x=105, y=130)
    create_user.mainloop()

def menu():
    global menu
    menu = Tk()
    menu.title("Operations Menu")
    menu.geometry("300x250")
    but1 = tk.Button(menu, text="Create New User", width=15, height=1, bg="orange", command=createnewuserpage).place(x=105,y=50)
    but2 = tk.Button(menu, text="Show User List", width=15, height=1, bg="orange", command=showuserlist).place(x=105, y=80)
    but3 = tk.Button(menu, text="Change Password", width=15, height=1, bg="orange", command=changepassform).place(x=105,y=110)
    but4 = tk.Button(menu, text="Factory Reset", width=15, height=1, bg="orange", command=factoryreset).place(x=105,y=140)
    menu.mainloop()

def showuserlist():
    names = []
    with open(r'usernames', 'r') as fp:
        for line in fp:
            x = line[:-1]
            names.append(x)

    win = Tk()
    win.geometry("750x350")
    style = ttk.Style()
    style.theme_use('clam')

    # Add a Treeview widget
    tree = ttk.Treeview(win, column=("ID", "User Name", "Finger"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="User Name")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Finger")

    for name in names:
        tree.insert('', 'end', text="1", values=(names.index(name), name, ' '))

    tree.pack()

    win.mainloop()


def changepass():
    with open('encryptedPWD.txt') as f:
        encpwd = ''.join(f.readlines())
        encpwdbyt = bytes(encpwd, 'utf-8')
    f.close()

    with open('refKey.txt') as f:
        refKey = ''.join(f.readlines())
        refKeybyt = bytes(refKey, 'utf-8')
    f.close()

    keytouse = Fernet(refKeybyt)
    myPass = (keytouse.decrypt(encpwdbyt))
    myPass = str(myPass).split("'")
    myPass = myPass[1]

    opass = oldpass.get()
    npass = newpass.get()

    if opass == '' or npass == '':
        message.set("fill the empty field!!!")
    else:
        if opass == myPass:
            mypwd = npass

            key = Fernet.generate_key()
            f = open("refKey.txt", "wb")
            f.write(key)
            f.close()

            refKey = Fernet(key)
            mypwdbyt = bytes(mypwd, 'utf-8')
            encryptedPWD = refKey.encrypt(mypwdbyt)
            f = open("encryptedPWD.txt", "wb")
            f.write(encryptedPWD)
            f.close()
            message.set("Change Succesful")
            changepass_form.destroy()


        else:
            message.set("Wrong password!!!")


def changepassform():
    menu.destroy()
    global changepass_form
    changepass_form = Tk()
    changepass_form.title("Change Pass Form")
    changepass_form.geometry("300x250")
    global message
    global oldpass
    global newpass
    oldpass = StringVar()
    newpass = StringVar()
    message = StringVar()
    Label(changepass_form, width="300", text="Please enter details below", bg="orange", fg="white").pack()
    Label(changepass_form, text="Old Password: ").place(x=20, y=40)
    Entry(changepass_form, textvariable=oldpass, show="*").place(x=100, y=42)
    Label(changepass_form, text="New Password: ").place(x=20, y=80)
    Entry(changepass_form, textvariable=newpass, show="*").place(x=100, y=82)
    Label(changepass_form, text="", textvariable=message).place(x=95, y=100)
    Button(changepass_form, text="Change Password", width=15, height=1, bg="orange", command=changepass).place(x=105, y=130)
    changepass_form.mainloop()


def factoryreset():
    mypwd = "abcd123"

    key = Fernet.generate_key()
    f = open("refKey.txt", "wb")
    f.write(key)
    f.close()

    refKey = Fernet(key)
    mypwdbyt = bytes(mypwd, 'utf-8')
    encryptedPWD = refKey.encrypt(mypwdbyt)
    f = open("encryptedPWD.txt", "wb")
    f.write(encryptedPWD)
    f.close()
    print("Password Reset Succesful")


    path = 'dataset'
    for file in os.listdir(path):
        pathfile = os.path.join(path, file)
        try:
            if os.path.isfile(pathfile):
                os.remove(pathfile)
            elif os.path.isdir(pathfile):
                shutil.rmtree(pathfile)
        except Exception as error:
            print(error)
    print("Dataset Path is cleaned")

    path = 'trainer'
    for file in os.listdir(path):
        pathfile = os.path.join(path, file)
        try:
            if os.path.isfile(pathfile):
                os.remove(pathfile)
            elif os.path.isdir(pathfile):
                shutil.rmtree(pathfile)
        except Exception as error:
            print(error)
    print("Trainer Path is cleaned")
