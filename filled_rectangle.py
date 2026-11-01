import cv2

img=cv2.imread("pikachu.png")
starting_point=(50,50)
ending_point=(200,200)
color=(255,0,0)
thickness=-1
img=cv2.rectangle(img,starting_point,ending_point,color,thickness)
cv2.imshow("filled rectangle on image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()