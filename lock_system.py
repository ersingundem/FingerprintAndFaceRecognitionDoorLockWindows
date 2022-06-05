from tkinter import *
import tkinter as tk
import time

import face_recognize
from fingerprint import FingerPrint
import pyttsx3

engine = pyttsx3.init()

window=tk.Tk()
window.title("Door Lock System")
window.geometry("500x500")
window.config(background='white')
window.maxsize(500,500)



def fingerprints():
    myFP = FingerPrint()
    try:
        myFP.open()
        global fingerprint_scan
        fingerprint_scan = tk.Tk()
        fingerprint_scan.title("Fingerprint")
        fingerprint_scan.geometry("400x400")
        fingerprint_scan.maxsize(400, 400)
        Label(fingerprint_scan, width="400", text="Please touch the fingerprint sensor", bg="orange", fg="white").pack()
        fingerprint_scan.update()
        engine.say("Please touch the fingerprint sensor")
        engine.runAndWait()

        if myFP.verify():
            print("Fingerprint verified.")
            fingerprint_scan.destroy()
            engine.say("Fingerprint verified. Face Recognition system is starting")
            engine.runAndWait()
            engine.say("Look at the Camera Please")
            engine.runAndWait()
            face_recognize.facerecognizer()


        else:
            print("Fingerprint not verified.")
            engine.say("Fingerprint not verified.")
            engine.runAndWait()
            fingerprint_scan.destroy()
            fingerprints()


    finally:
        myFP.close()

def login():
    uname=username.get()
    pwd=password.get()
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      if uname=="abcd@gmail.com" and pwd=="abc123":
       message.set("Login success")
      else:
       message.set("Wrong username or password!!!")

def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("300x250")
    global message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    Label(login_screen, text="Username * ").place(x=20,y=40)
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    Label(login_screen, text="Password * ").place(x=20,y=80)
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()

but3 = tk.Button(window,text="Open the Lock", width=30,font=("Ariel Bold",15),bg='orange',fg='white', command=fingerprints)
but3.place(x=100, y=200)
but4 = tk.Button(window, text="Control Panel", width=30, font=("Ariel Bold",15), bg='orange', fg='white', command=Loginform)
but4.place(x=100, y=100)

window.mainloop()