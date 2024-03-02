import cv2


img = cv2.imread("img/people.jpg")
img = cv2.resize(img, (0,0), fx=3, fy=3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier("eye.xml")
results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(results)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)

cv2.imshow("IMG", img)
cv2.waitKey(0)