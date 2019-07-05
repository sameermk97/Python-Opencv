import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_img():
	blank_img=np.ones((600,600))
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(blank_img,text='ABCDE',org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
	return blank_img


def show_img(img):
	fig=plt.figure(figsize=(12,10))
	ax=fig.add_subplot(111)
	ax.imshow(img,cmap='gray')
	plt.show()


i=load_img()

kernel=np.ones((5,5),dtype=np.uint8)
result=cv2.erode(i,kernel,iterations=2)

show_img(result)