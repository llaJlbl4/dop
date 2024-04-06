import cv2

img = cv2.VideoCapture(0)

eye = cv2.CascadeClassifier('eye.xml')
face = cv2.CascadeClassifier('face.xml')
smile = cv2.CascadeClassifier('smile.xml')

while True:
    ret, frame = img.read()
    if ret:
        results_eye = eye.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=100)
        results_face = face.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=15)
        results_smile = smile.detectMultiScale(frame, scaleFactor=3.1, minNeighbors=25)

        for (x, y, z, b) in results_eye:
            cv2.rectangle(frame, (x, y), (x+z, y+b), (0, 255, 0), 2)
        for (x, y, z, b) in results_face:
            cv2.rectangle(frame, (x, y), (x+z, y+b), (255, 255, 0), 2)
        for (x, y, z, b) in results_smile:
            cv2.rectangle(frame, (x, y), (x+z, y+b), (255, 255, 255), 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break