import cv2
import matplotlib.pyplot as plt



img = cv2.imread('C:/Users/Kulkarni/Downloads/Computer-Vision-with-Python/DATA/crossword.jpg')
#cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#plt.imshow(img)
#plt.show()

def show_pic(img):
	fig = plt.figure(figsize=(15,15))
	ax = fig.add_subplot(111)
	ax.imshow(img,cmap='gray')
	plt.show()



ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)


th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)

blended=cv2.addWeighted(src1=th1,alpha=0.6,src2=th2,beta=0.4,gamma=0)
show_pic(blended)
