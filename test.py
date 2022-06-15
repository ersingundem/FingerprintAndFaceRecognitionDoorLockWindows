

from tkinter import *
import tkinter as tk
from fingerprint import FingerPrint

"""
names = ["Ersin"]
with open(r'usernames', 'w') as fp:
    for item in names:
        fp.write("%s\n" % item)

useroperations.createuserfacedataset(0)
useroperations.trainfacemodels()
"""

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
            print(myFP.identify())
            print("Fingerprint verified.")
            fingerprint_scan.destroy()
        else:
            print("Fingerprint not verified.")
            fingerprint_scan.destroy()
            fingerprints()


    finally:
        myFP.close()

fingerprints()