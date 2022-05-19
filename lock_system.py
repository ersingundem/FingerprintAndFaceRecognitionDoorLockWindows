from tkinter import *
import tkinter as tk

import face_recognize
from fingerprint import FingerPrint
from face_recognize import *


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

        if myFP.verify():
            print("Hello! Master")
            fingerprint_scan.destroy()
            face_recognize.facerecognizer()
        else:
            print("Sorry! Man")
            fingerprint_scan.destroy()
            fingerprints()

    finally:
        myFP.close()


but3 = tk.Button(window,text="Scan Fingerprint", width=30,font=("Ariel Bold",15),bg='orange',fg='white', command=fingerprints)
but3.place(x=100, y=160)

window.mainloop()