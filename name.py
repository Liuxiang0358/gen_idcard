#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 20:13:09 2019

@author: lx
"""
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
font = ImageFont.truetype('simhei.ttf',50)
#img=Image.open('face.jpg')
#draw = ImageDraw.Draw(img)
#draw.text(( 220, 100),"战斗嘎仙",(0,0,0),font=font)
#draw = ImageDraw.Draw(img)
#img.save("res.png")
#####  姓名
f = open("name.txt","r")   #设置文件对象
line = f.readline()
#lines = []
#while line:             #直到读取完文件
#    line = f.readline()  #读取一行文件，包括换行符
#    lines.append(line)
#f.close() #关闭文件
#print(len(lines))
   ###420 160
#img = cv2.imread('res.png')
#cut = img[105:160,220:420]
#cv2.imwrite('cut.jpg', cut)
while line:             #直到读取完文件
    
    line = f.readline()  #读取一行文件，包括换行符
    line = line[:-1]
    print(line)
    img=Image.open('name.jpg')
    draw = ImageDraw.Draw(img)
    draw.text((8 , 8),line,(0,0,0),font=font)
    draw = ImageDraw.Draw(img)
    img.save("name/"+line+'.png')
    with open("name/"+line+'.txt',"w") as f1:    #设置文件对象
      f1.write(line)
    
f.close() #关闭文件

