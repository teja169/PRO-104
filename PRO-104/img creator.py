import cv2 , numpy as np

black = np.zeros([600 , 600])
print(black)

black[ 200:401 , 200:401 ] = 255 
#black[ 300:401 , 200:401 ] = 0

cv2.imshow("black image" , black)
cv2.waitKey(0)

