import cv2

img=cv2.imread("pikachu.png")
starting_point=(100,100)
ending_point=(500,100)
color=(0,0,255)
thickness=5
img=cv2.line(img,starting_point,ending_point,color,thickness)
cv2.imshow("line on image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()