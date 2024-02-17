import cv2
import numpy as np

img = cv2.imread("Enot.jpg")
img = cv2.resize(img, (1000, 500))

cv2.rectangle(img, (100, 0), (770, 420), (255, 100, 50), thickness=1)
cv2.circle(img, (350, 235), 25, (0, 255, 0), thickness=cv2.FILLED)
cv2.circle(img, (510, 255), 25, (0, 255, 0), thickness=cv2.FILLED)
cv2.circle(img, (410, 360), 50, (0, 0, 255), thickness=cv2.FILLED)
cv2.line(img, (350, 235), (410, 360), (255, 0, 0), thickness=1)
cv2.line(img, (510, 255), (410, 360), (255, 0, 0), thickness=1)
cv2.putText(img, "Ejik", (450, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Enot", img)
cv2.waitKey(0)