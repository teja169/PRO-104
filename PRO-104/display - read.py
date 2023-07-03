import cv2

poster = cv2.imread("poster.jpg")

rocket = poster[ 120:340 , 400:500 ]

poster[0:220 , 500:600] = rocket
text = "ROCKET"
cv2.putText(poster , text , (50,50) , color=(100 , 0 , 0 ) , fontFace=cv2.FONT_ITALIC , fontScale=1 )
cv2.imshow("rocket " , rocket)

cv2.imshow( "poster" , poster)
cv2.waitKey(0)