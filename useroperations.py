import cv2
import os
import face_training
import numpy as np
from PIL import Image
from tkinter import *
import tkinter as tk

import fingerprint


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
    message.set("Please add your biometric datas.")
    userId = newuserid.get()
    userId = int(userId)
    userName = newusername.get()

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
    global newuserid;
    newusername = StringVar()
    newuserid = StringVar()
    message = StringVar()
    Label(create_user, width="300", text="Please enter details below", bg="orange", fg="white").pack()
    Label(create_user, text="New User Name: ").place(x=20, y=40)
    Entry(create_user, textvariable=newusername).place(x=120, y=42)
    Label(create_user, text="User ID: ").place(x=20, y=60)
    Entry(create_user, textvariable=newuserid).place(x=120, y=62)
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
    but3 = tk.Button(menu, text="Change Password", width=15, height=1, bg="orange", command=changepass).place(x=105,y=110)
    menu.mainloop()

def showuserlist():
    print("hi")


def changepass():
    print("hi")


