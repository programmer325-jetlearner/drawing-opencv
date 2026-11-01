import cv2

img=cv2.imread("pikachu.png")
starting_point=(100,100)
ending_point=(270,270)
color=(255,0,0)
thickness=7
img=cv2.rectangle(img,starting_point,ending_point,color,thickness)
cv2.imshow("rectangle on image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()