import cv2
#
# img = cv2.imread("cv2_g1_g2/Enot.jpg")
# img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
# cv2.imshow("Enot", img)
#
# cv2.waitKey(31873)
# import cv2
#
# img = cv2.imread("../cv_2/cv2_g1_g2/cv2_g1_g2/sq.jpg")
# img = cv2.resize(img, (img.shape[1]//4, img.shape[0]//4))
# cv2.imshow("Enot", img[127:290, 70:228])
#
# cv2.waitKey(500)

img = cv2.imread("cv2_g1_g2/cv2_g1_g2/face.Jpg")
img = cv2.resize(img, (img.shape[1]//1, img.shape[0]//1))
# img = cv2.GaussianBlur(img, (25, 25), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 100, 100)

cv2.imshow("tb", img)

cv2.waitKey(1000)
