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

def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),10)
    return line_image        


img=cv2.imread("test_image.jpg")

canny=image_to_canny(img)
cropped_img=region_of_interest(canny)
lines=cv2.HoughLinesP(cropped_img,2,np.pi/180,threshold=100,lines=np.array([]),minLineLength=40,maxLineGap=5)
line_image=display_lines(img,lines)
combo_image=cv2.addWeighted(img,0.8,line_image,1,1)
cv2.imshow("Image",combo_image)
cv2.waitKey(0)