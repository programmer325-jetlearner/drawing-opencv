import cv2

img=cv2.imread("pikachu.png")
position=(100,100)
font=cv2.FONT_HERSHEY_COMPLEX
fontScale=1
color=(255,0,0)
thickness=3
img=cv2.putText(img,"hello",position,font,fontScale,color,thickness,cv2.LINE_AA)
cv2.imshow("text on image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()