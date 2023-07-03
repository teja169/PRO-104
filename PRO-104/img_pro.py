import cv2 

img = cv2.imread("butterfly.jpg")
cv2.imshow("butterfly image" , img )

#print(img)

gimg = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
print(gimg)
cv2.imshow("gray butterfly" , gimg)


cv2.waitKey(0)
