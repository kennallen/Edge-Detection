#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:54:25 2017

@author: kenallen
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)
#from ImageCompression import compress
from matplotlib.image import imread
import GaussianFilter as gf
from scipy.misc import imsave




Im = imread("bryce.png")  #load image 
save_name = "bryce_edges.png" # option to save image as this
save = False # save image as file or not


Im = gf.smooth(Im) # 5x5 gaussian filter of image
    

soble_vertical = np.array([[1,0,-1],
                          [2,0,-2],
                          [1,0,-1]])

soble_horizontal = np.array([[1,2,1],
                          [0,0,0],
                          [-1,-2,-1]])



def grayscale(a): # return grayscale verion of image
    b = np.zeros(np.shape(a)[0:2])
    b[:,:] = (a[:,:,0]*0.299+a[:,:,1]*0.587 + a[:,:,2])*0.114
    
    return b



def soble(a): #find edges
    
    row = np.shape(Im)[0]
    col = np.shape(Im)[1]

    b = np.zeros((row,col))
    
    #this line find the gradient in the x and y directions with sobel matrices and does sqrt(x^2 + y^2) to them to find the gradient
    
    b[1:row-1,1:col-1] = np.sqrt((a[0:row-2,0:col-2] - a[0:row-2,2:col]+ 2*a[1:row-1,0:col-2] - 2*a[1:row-1,2:col] + a[2:row,0:col-2]  - a[2:row,2:col])**2+\
                         (a[0:row-2,0:col-2] + a[0:row-2,1:col-1] + a[0:row-2,2:col] - a[2:row,0:col-2] - a[2:row,1:col-1] - a[2:row,2:col])**2)
    
    return b



ImG = grayscale(Im)


img_plot = plt.imshow(soble(ImG),cmap = 'gray')

if save == True:
    imsave(save_name,soble(ImG))