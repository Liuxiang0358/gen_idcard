#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 20:41:58 2019

@author: lx
"""
import os
import cv2
import random
import glob
    #print(all_rotate_angles)
rand1 = []
root = glob.glob('/home/lab507c/data_ocr/face/*.jpg')
#root = glob.glob('face/*.jpg')
import numpy as np

def translate(image, x, y):
    # 定义平移矩阵
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def add_noise(im,h,w):
    for i in range(int(0.05 * h * w)): #添加点噪声
        temp_x = np.random.randint(0,im.shape[0])
        temp_y = np.random.randint(0,im.shape[1])
        im[temp_x][temp_y] = random.randint(0,50)
    return im

def add_erode(im):   ###适当腐蚀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))    
    im = cv2.erode(im,kernel) 
    return im

def add_dilate(im):  ###适当膨胀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1, 2))    
    im = cv2.dilate(im,kernel) 
    return im
def rotate(im):
    rows,cols ,chanll= im.shape
    r = random.uniform(-2, 2)
# cols-1 and rows-1 are the coordinate limits.
    M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),r,1)
    im = cv2.warpAffine(im,M,(cols,rows))
    return im

def randlight(im):
    res = np.uint8(np.clip((random.uniform(0.5,1.2) * im + 10), 0, 255))
    return res

def blur(im):
   
    im = cv2.blur(im, (3, 3))
    return im

def do(im,h,w):
        choice =  random.random()
        im = randlight(im)
        im = add_dilate(im)
        if  choice < 0.2:
#            im = add_noise(im,h,w)
             im  = blur(im)
        elif  choice >= 0.3 and choice < 0.4:
            im = translate(im, -5, 0)
        elif  choice >= 0.4 and choice < 0.5:
            im = translate(im, 5, 0)
        elif  choice >= 0.5 and choice < 0.7:
            im = rotate(im)
        elif  choice >= 0.7 and choice < 0.8:
            im  = blur(im)
        else:
            im  = blur(im)
        return im

def read_directory(directory_name):
    # this loop is for read each image in this foder,directory_name is the foder name with images.
    for filename in os.listdir(r"./"+directory_name):
        #print(filename) #just for test
        #img is used to store the image data 
        file_name = directory_name + "/" + filename
        (filename,extension) = os.path.splitext(file_name)
        if extension == '.jpg':
            im = cv2.imread(file_name)
            h,w =  im.shape[0:2]
            img = do(im,h,w)
            cv2.imwrite(file_name, img)
            print(file_name)
        #print(img)
def read_directory1(root):
    # this loop is for read each image in this foder,directory_name is the foder name with images.
    for filename in root:
        im = cv2.imread(filename)
        h,w =  im.shape[0:2]
        img = do(im,h,w)
        cv2.imwrite(filename, img)
        print(filename)
        #print(img)
        
#if __name__ == 'main':
read_directory1(root)

#folders = ['face']
#for folder in folders:
#    read_directory(folder)
#    print(folder)
