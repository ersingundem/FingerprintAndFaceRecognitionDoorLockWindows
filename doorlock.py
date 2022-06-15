import time
import serial
import pyttsx3

engine = pyttsx3.init()

arduino = serial.Serial(port='COM7', baudrate=9600)

def sendopensignaltoarduino():
    arduino.write(str.encode('1'))

def sendclosesignaltoarduino():
    arduino.write(str.encode('1'))

def doorlockopen(id):

    engine.say("Face Verified, Door will be open in 5 seconds.")
    engine.runAndWait()
    time.sleep(2)
    sendopensignaltoarduino()
    engine.say("Door is open. Welcome"+id)
    engine.runAndWait()

def doorlockclose():
    engine.say("An unauthorized access attempt was detected. The door is locked. Please leave your current location.")
    engine.runAndWait()
