import cv2
img=cv2.imread('C:/Users/Kulkarni/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:
	cv2.imshow('puppy',img)
	if cv2.waitKey(1) & 0XFF == 27:
		break
cv2.destroyAllWindows()