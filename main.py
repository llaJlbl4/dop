import cv2
import numpy as np


img = np.zeros((500, 500, 3), dtype='uint8')

# img [100:150, 200:280] = 0, 0, 255
# img [450:500, 450:500] = 0, 255, 0
cv2.rectangle(img, (250, 200), (300, 250), (255, 100, 50), thickness=1)
cv2.rectangle(img, (200, 180), (270, 225), (0, 0, 255), thickness=cv2.FILLED)
cv2.rectangle(img, (260, 230), (400, 190), (0, 255, 0), thickness=2)
cv2.line(img, (250, 200), (400, 190), (255, 0, 0), thickness=1)
cv2.circle(img, (280, 212), 150, (0, 0, 255), thickness=1)
cv2.putText(img, "My text", (100, 200), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)

cv2.imshow("IMG", img)
cv2.waitKey(0)