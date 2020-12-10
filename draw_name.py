#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:59:01 2019

@author: lx
"""

'''
msyhl.ttf   y 0
msyh.ttf    y 0
msyhbd.ttf  0
simhei.ttf  10
STSONG.TTF  10
simsun.ttf  10
STZHONGS.TTF 0
'''
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import charac
import os
from collections import Counter
import random
charac_copy = charac. character()
charac_copy = ''.join(charac_copy)
charac_copy =  charac_copy.replace('\n','')
charac_copy =  charac_copy.replace('\t','')
charac_copy =  charac_copy.replace(' ','')
font_list = os.listdir('font')
face = '/home/lab507c/data_ocr/name/'
#face = 'face/'
#f = open("gen_name2.txt","r")   #设置文件对象
#name = f.readline()
names = []

f = open("gen_name.txt","r")   #设置文件对象
f = open("name_total.txt","r") 
name = f.readline()
while name:             #直到读取完文件
   name = f.readline()  #读取一行文件，包括换行符
   names.append(name)
f.close() #关闭文件
print(len(names))
choice = random.sample(names, 100000)
for name in choice:
#    name = choice[3]
    name = name.replace('\n','')
    p = random.randint(10,20)
    if len(name) == 7:
        name = name.replace(' ','')
        p = random.randint(0,10)
    img=Image.open('templet/id.jpg')
    (h,w) = img.size
    img = img.resize((int(h/(w/32)),32),Image.ANTIALIAS)
    
    draw = ImageDraw.Draw(img)
    font_choice = 'msyh.ttf'
    font_size = random.randint(22,24)
    font = ImageFont.truetype('font/'+font_choice,font_size)
    
    if font_choice in ['msyhl.ttf',' msyh.ttf','msyhbd.ttf','STZHONGS.TTF','STSONG.TTF','msyh.ttf']:       
       draw.text((p,0),name,(0,0,0),font=font)
    else:
       draw.text((p,10),name,(0,0,0),font=font)
        
    draw = ImageDraw.Draw(img)
    name = name.replace(' ','')
    print(name)
#    img = img.resize((280, 32),Image.ANTIALIAS)
    img.save(face+name + ".jpg")
    with open(face+name  +'.txt',"w") as f1:    #设置文件对象
      f1.write(name)