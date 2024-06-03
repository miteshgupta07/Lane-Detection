import cv2
import numpy as np

def image_to_canny(image):
    gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    blur_img=cv2.GaussianBlur(gray_img,(5,5),0)
    canny_img=cv2.Canny(blur_img,50,150)
    return canny_img

def region_of_interest(image):
    height=image.shape[0]
    triangle=np.array([[(200,height),(1100,height),(550,250)]])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,triangle,255)
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image

img=cv2.imread("test_image.jpg")

canny=image_to_canny(img)
cropped_img=region_of_interest(canny)
cv2.imshow("Image",cropped_img)
cv2.waitKey(0)