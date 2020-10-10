import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face  = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 60), 2)
    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cap.release()

