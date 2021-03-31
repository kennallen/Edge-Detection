#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:34:23 2017

@author: kenallen
"""

import numpy as np
from matplotlib import interactive
interactive(True)
from matplotlib.image import imread



                    
#gauss3 = np.array([[1,2,1],   Gaussian distributions for reference
#                  [2,4,2],
#                  [1,2,1]])
#    
#gauss5 = [[1,4,7,4,1],
#         [4,16,26,16,4],
#         [7,26,41,26,7],
#         [4,16,26,16,4],
#         [1,4,7,4,1]]
    



def smooth(Im): # for each pixel takes a weighted average of surrounding pixels using 5x5 gaussian kernel
    
    points_r = Im[:,:,0]#isolate r,g,b pixels
    points_g = Im[:,:,1]
    points_b = Im[:,:,2]
    
    row = np.shape(points_r)[0]
    col = np.shape(points_r)[1]
    
    
    new_r = np.zeros((row,col)) #creats canvas for blurred image
    new_g = np.zeros((row,col))
    new_b = np.zeros((row,col))
    
    
    
    #vectorized blur methodes workign really fase 
    #the next few lines have the 5x5 matrix hardcoded and make each point in the new canvasa 
    #the weighted average of the surrounding pixels giving more weiht to closer ones
    
    
    new_r[2:row-2,2:col-2] = (points_r[0:row-4,0:col-4] + 4*points_r[0:row-4,1:col-3] + 7*points_r[0:row-4,2:col-2] + 4*points_r[0:row-4,3:col-1]+ points_r[0:row-4,4:col]+\
                               4*points_r[1:row-3,0:col-4] + 16*points_r[1:row-3,1:col-3] + 26*points_r[1:row-3,2:col-2] + 16*points_r[1:row-3,3:col-1]+ 4*points_r[1:row-3,4:col]+\
                               7*points_r[2:row-2,0:col-4] + 26*points_r[2:row-2,1:col-3] + 41*points_r[2:row-2,2:col-2] + 26*points_r[2:row-2,3:col-1]+ 7*points_r[2:row-2,4:col]+\
                               4*points_r[3:row-1,0:col-4] + 16*points_r[3:row-1,1:col-3] + 26*points_r[3:row-1,2:col-2] + 16*points_r[3:row-1,3:col-1]+ 4*points_r[3:row-1,4:col]+\
                               points_r[4:row-0,0:col-4] + 4*points_r[4:row-0,1:col-3] + 7*points_r[4:row-0,2:col-2] + 4*points_r[4:row-0,3:col-1]+ points_r[4:row-0,4:col])/273
    
    new_g[2:row-2,2:col-2] = (points_g[0:row-4,0:col-4] + 4*points_g[0:row-4,1:col-3] + 7*points_g[0:row-4,2:col-2] + 4*points_g[0:row-4,3:col-1]+ points_g[0:row-4,4:col]+\
                               4*points_g[1:row-3,0:col-4] + 16*points_g[1:row-3,1:col-3] + 26*points_g[1:row-3,2:col-2] + 16*points_g[1:row-3,3:col-1]+ 4*points_g[1:row-3,4:col]+\
                               7*points_g[2:row-2,0:col-4] + 26*points_g[2:row-2,1:col-3] + 41*points_g[2:row-2,2:col-2] + 26*points_g[2:row-2,3:col-1]+ 7*points_g[2:row-2,4:col]+\
                               4*points_g[3:row-1,0:col-4] + 16*points_g[3:row-1,1:col-3] + 26*points_g[3:row-1,2:col-2] + 16*points_g[3:row-1,3:col-1]+ 4*points_g[3:row-1,4:col]+\
                               points_g[4:row-0,0:col-4] + 4*points_g[4:row-0,1:col-3] + 7*points_g[4:row-0,2:col-2] + 4*points_g[4:row-0,3:col-1]+ points_g[4:row-0,4:col])/273
         
    new_b[2:row-2,2:col-2] = (points_b[0:row-4,0:col-4] + 4*points_b[0:row-4,1:col-3] + 7*points_b[0:row-4,2:col-2] + 4*points_b[0:row-4,3:col-1]+ points_b[0:row-4,4:col]+\
                               4*points_b[1:row-3,0:col-4] + 16*points_b[1:row-3,1:col-3] + 26*points_b[1:row-3,2:col-2] + 16*points_b[1:row-3,3:col-1]+ 4*points_b[1:row-3,4:col]+\
                               7*points_b[2:row-2,0:col-4] + 26*points_b[2:row-2,1:col-3] + 41*points_b[2:row-2,2:col-2] + 26*points_b[2:row-2,3:col-1]+ 7*points_b[2:row-2,4:col]+\
                               4*points_b[3:row-1,0:col-4] + 16*points_b[3:row-1,1:col-3] + 26*points_b[3:row-1,2:col-2] + 16*points_b[3:row-1,3:col-1]+ 4*points_b[3:row-1,4:col]+\
                               points_b[4:row-0,0:col-4] + 4*points_b[4:row-0,1:col-3] + 7*points_b[4:row-0,2:col-2] + 4*points_b[4:row-0,3:col-1]+ points_b[4:row-0,4:col])/273

    filtered_image = np.zeros(np.shape(Im))
    
    
    filtered_image[:,:,0] = new_r #brings the r,g,b pixels back togeter in one array
    filtered_image[:,:,1] = new_g
    filtered_image[:,:,2] = new_b
                  
    return filtered_image    

                  
