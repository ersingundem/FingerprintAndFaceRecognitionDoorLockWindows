

from tkinter import *
import tkinter as tk
from fingerprint import FingerPrint
import useroperations

names = ["Ersin"]
with open(r'usernames', 'w') as fp:
    for item in names:
        fp.write("%s\n" % item)

useroperations.createuserfacedataset(0)
useroperations.trainfacemodels()


