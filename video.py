import cv2

cap = cv2.VideoCapture("cv2_g1_g2/istockphoto-1258621982-640_adpp_is.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("video", img)

    cv2.waitKey(121)
