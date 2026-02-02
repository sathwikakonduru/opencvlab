import cv2
img = cv2.imread("image.jpg")
cv2.imshow("original image",img)
cv2.waitkey(0)
cv2.destroyAllWindows()
