import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_img():
	img=cv2.imread('C:/Users/Kulkarni/Downloads/Computer-Vision-with-Python/DATA/sammy_noise.jpg')
	img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	return img


def show_img(img):
	fig=plt.figure(figsize=(15,15))
	ax=fig.add_subplot(111)
	ax.imshow(img)
	plt.show()


i=load_img()

clear_img=cv2.medianBlur(i,5)

show_img(i)

show_img(clear_img)