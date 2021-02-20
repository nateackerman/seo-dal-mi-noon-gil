import face_recognition
#from cv2 import cv2
#from random import randrange
#import numpy as np

#capture = cv2.VideoCapture("수지Suzy_Yes_No_Maybe_1080p.mp4")

known_Suzy = face_recognition.load_image_file("suzy/suzy1.jpg")
unknown_Suzy = face_recognition.load_image_file("suzy/suzy2.jpg")

known_Suzy_encoding = face_recognition.face_encodings(known_Suzy)[0]
unknown_encoding = face_recognition.face_encodings(unknown_Suzy)[0]

results = face_recognition.compare_faces([known_Suzy_encoding], unknown_encoding)

if results[0] == True:
    print("It's a picture of Suzy!")
else:
    print("It's not a picture of Suzy!")
#unknown_image = face_recognition.load_image_file()