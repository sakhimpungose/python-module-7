#Face detection

import cv2

#Create a CascadeClassifier object
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Capturing video via the default camera
video = cv2.VideoCapture(0)

while True:
    
    check, frame = video.read()
    
    if check:
        # Reading the image as a gray scale image
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.05, minNeighbors=5)
        
        for x, y, w, h in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)        
        
        cv2.imshow('Capturing...', cv2.flip(frame, 1))
    
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()
