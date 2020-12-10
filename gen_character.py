#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:17:48 2019

@author: lx
"""
import PIL.Image as Image
import PIL.ImageColor as ImageColor
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import cv2
import charac


######
#imgobj = cv2.imread('real.jpg') #读取图像
#cv2.imshow("image",imgobj)

####   STSONG 宋体
####   simhei 黑体
#设置字体（LiberationSans-Regular.ttf这是我ubuntu16.04自带的字体)
charac_copy = charac.charac()
font = ImageFont.truetype('font/seguili.ttf',50)
font = ImageFont.truetype('simhei.ttf',50)
#打开图片
imageFile = "templet/face.jpg"
im1=Image.open(imageFile)
#img = cv2.imread('res.png')
#cv2.imshow('img_bilateralFilter',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
# 在图片上添加文字 1
draw = ImageDraw.Draw(im1)

# (0,0):坐标 "XUNALOVE"：添加的字体 (0,0,255):字体颜色 font:字体大小

name = ''
sex = ''
rice = ''
address  = ''
ID_number = ''
draw.text(( 220, 100),"战斗嘎仙",(0,0,0),font=font)   ###420 160
draw = ImageDraw.Draw(im1)
font = ImageFont.truetype('simhei.ttf',40)
draw.text(( 220, 185),"男",(0,0,0),font=font)
draw = ImageDraw.Draw(im1)
draw.text(( 450, 185),"汉",(0,0,0),font=font)
draw = ImageDraw.Draw(im1)
draw.text(( 220, 270),"2019",(0,0,0),font=font)
draw = ImageDraw.Draw(im1)
draw.text(( 385, 270),"06",(0,0,0),font=font)
draw = ImageDraw.Draw(im1)
draw.text(( 485, 270),"08",(0,0,0),font=font)
draw = ImageDraw.Draw(im1)
draw.text(( 220, 355),"四川省成都市皮杜曲电子\n科技大学",(0,0,0),font=font)
draw = ImageDraw.Draw(im1)
draw.text(( 420, 570),"14232619940515271X",(0,0,0),font=font)
draw = ImageDraw.Draw(im1)

# 保存
im1.save("res2.png")

#while true:
    
img2 = cv2.imread(imageFile )
#####  jiguan
cut2 = img2[500:550,250:1000]
cv2.imwrite('id.jpg', cut2)
    #####  住址
cut = img2[560:615,335:1050]
cv2.imwrite('cut.jpg', cut)
########  name
cut2 = img2[95:150,190:400]
cv2.imwrite('id.jpg', cut2)