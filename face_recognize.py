import cv2
import numpy as np
import os
import doorlock
import time
lockstate=0
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

names = []
with open(r'usernames', 'r') as fp:
    for line in fp:
        x = line[:-1]
        names.append(x)

def facerecognizer():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    lockstate = 0
    closestate = 0
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if (confidence < 50):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                lockstate = lockstate + 1
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                closestate = closestate + 1


            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('Face Recognition', img)
        if lockstate == 60:
            doorlock.doorlockopen(id)
            break
        if closestate == 60:
            doorlock.doorlockclose()
            break
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break


    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
