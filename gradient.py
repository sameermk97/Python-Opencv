import cv2
import matplotlib.pyplot as plt
import numpy as numpy

def show_img(img):
	fig=plt.figure(figsize=(15,15))
	ax=fig.add_subplot(111)
	ax.imshow(img,cmap='gray')
	plt.show()


img=cv2.imread('C:/Users/Kulkarni/Downloads/Computer-Vision-with-Python/DATA/sudoku.jpg',0)


sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
laplacian=cv2.Laplacian(img,cv2.CV_64F)

show_img(sobelx)
show_img(sobely)
show_img(laplacian)