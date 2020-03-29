import numpy as np
import cv2
import  pickle

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainner.yml")
labels = {"person_name":1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = { v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)

while True:
    # capture frame by frame
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in face:
        roi_gray = gray_frame[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # recognize deep learning

        id_, conf = recognizer.predict(roi_gray)
        if (conf >= 45 and conf <= 85):
            print(id_)
            #print(labels[id_])
            print(x,y,w,h)
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (25,50,255)
            stroke =2
            cv2.putText(frame,name,(x,y-30),font ,1,color,stroke,cv2.LINE_AA)

        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # display the resulting frame

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
