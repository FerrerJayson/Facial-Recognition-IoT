import cv2
import numpy as np
import face_recognition

imgPrimary = face_recognition.load_image_file('ImageBasic/Elon Musk.jpg')
imgPrimary = cv2.cvtColor(imgPrimary,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('ImageBasic/Jimmy Fallon.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgPrimary)[0]
encodeElon = face_recognition.face_encodings(imgPrimary)[0]
cv2.rectangle(imgPrimary,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(0,0,255),2)

results =  face_recognition.compare_faces([encodeElon],encodeTest)
faceDistance = face_recognition.face_distance([encodeElon],encodeTest)
cv2.putText(imgTest,f'{results} {round(faceDistance[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2)
print(results,faceDistance)

cv2.imshow('Primary Image',imgPrimary)
cv2.imshow('Image Test',imgTest)
cv2.waitKey(0)
