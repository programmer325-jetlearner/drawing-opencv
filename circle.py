import cv2

img=cv2.imread("pikachu.png")
center=(300,200)
radius=100
color=(100,150,100)
thickness=4
img=cv2.circle(img,center,radius,color,thickness)
cv2.imshow("circle on image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()