import cv2

img=cv2.imread("test_image.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
blur_img=cv2.GaussianBlur(gray_img,(5,5),10)
canny_img=cv2.Canny(blur_img,50,150)

cv2.imshow("Image",canny_img)
cv2.waitKey(0)