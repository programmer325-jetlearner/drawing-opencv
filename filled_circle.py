import cv2

img=cv2.imread("pikachu.png")
center=(300,300)
radius=120
color=(0,255,0)
thickness=-1
img=cv2.circle(img,center,radius,color,thickness)
cv2.imshow("filled circle on image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()