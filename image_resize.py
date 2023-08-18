import cv2

source = 'tulip.jpg'
destination = "new_image"
scale_percent=50

src=cv2.imread(source,cv2.IMREAD_UNCHANGED)

#calculate 50 percent of original dimaension
width=int(src.shape[1]*scale_percent/100)
height=int(src.shape[0]*scale_percent/100)
dsize=(width,height)

output=cv2.resize(src,dsize)
cv2.imwrite('new_image1.png',output)