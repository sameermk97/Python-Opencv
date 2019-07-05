import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
	img=cv2.imread('C:/Users/Kulkarni/Downloads/Computer-Vision-with-Python/DATA/bricks.jpg').astype(np.float32)/255
	img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	return img


def show_img(img):
	fig=plt.figure(figsize=(15,15))
	ax=fig.add_subplot(111)
	ax.imshow(img)
	plt.show()

i=load_img()

font=cv2.FONT_HERSHEY_COMPLEX

cv2.putText(i,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)

kernel=np.ones(shape=(5,5),dtype=np.float32)/25

dst=cv2.filter2D(i,-1,kernel)

show_img(i)
show_img(dst)