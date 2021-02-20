import face_recognition
import cv2 as cv
import random

filesArray = [
    "suzy1.jpg",
    "suzy2.jpg",
    "suzy3.jpg",
    "suzy3.webp",
    "suzy4.jpg",
    "suzy6.jpg",
    "suzy7.jpg",
    "suzy8.jpg",
    "suzy9.jpg",
    "suzy10.jfif",
    "suzy11.jpg",
    "suzy12.jpg",
    "suzy13.jpg",
    "suzy14.png",
    "suzy15.jpg",
    "suzy16.jpg",
    "suzy17,jpg",
    "suzy18.jpg",
    "suzy19.jpg",
    "suzy20.jpg",
    "suzy21.jfif",
    "suzy22.jpg",
    "suzy23.jpg",
    "suzy24.jpg",
    "suzy25.jpg",
    "suzy26.jpg",
    "suzy27.jpg",
    "suzy28,jpg",
    "suzy29.jpg",
    "suzy30.jpg",
    "suzy31.jpg",
    "suzy32.jpg",
    "suzy33.jpg",
    "suzy33.jfif",
    "suzy34.jpg",
    "suzy35.jpg",
    "suzy36.jpg",
    "suzy37.jpg",
    "suzy38.jpg"
]

img = face_recognition.load_image_file('suzy/'+ random.choice(filesArray))
face_locations = face_recognition.face_locations(img)
print(face_locations)

color = cv.cvtColor(img, cv.COLOR_RGB2BGRA)

for faces in face_locations:
    top, right, bottom, left = faces
    cv.rectangle(color, (left, top), (right, bottom), (0, 255, 0), 3)

if len(face_locations) == 0:
    print("No one")
else:
    print("Suzy found!")

#cv.rectangle(img, (400, 100), (1100, 1200), (0, 255, 0), 3)
cv.imshow('Suzy', color)
cv.waitKey(0)