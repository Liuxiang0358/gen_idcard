#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:36:49 2019

@author: lx
"""
'''
生成身份证正面年月日
'''
import time
import random
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
face = '/home/lab507c/data_ocr/face/'
#face = 'face/'
a1=(1935,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(2030,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳
font = ImageFont.truetype('font/simhei.ttf',46)
#随机生成10个日期字符串
font_name =  'simhei.ttf' 
for i in range(2000):   
    try:
        start=time.mktime(a1)    #生成开始时间戳
        end=time.mktime(a2)      #生成结束时间戳
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)    #将时间戳生成时间元组
        date = time.strftime("%Y.%m.%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        data = date.split('.')
        print(data)
        img=Image.open('templet/dirth.jpg')
        draw = ImageDraw.Draw(img)
        draw.text((130+random.randint(0,7), random.randint(3,5)),data[0],(0,0,0),font=font)
        draw.text((297+random.randint(0,7), random.randint(3,5)),data[1],(0,0,0),font=font)
        draw.text((395+random.randint(0,7), random.randint(3,5)),data[2],(0,0,0),font=font)
        draw = ImageDraw.Draw(img)
        img.save(face+date+".jpg")
        with open(face+date+'.txt',"w") as f1:    #设置文件对象
          f1.write('出生'+data[0]+'年'+data[1]+'月'+ data[2]+'日')
    except:
        print('error')
        
'''
生成身份证正面 性别 和 民族
'''
import os
import time
import random
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
font = ImageFont.truetype('font/simhei.ttf' ,35)
f = open("race.txt","r")   #设置文件对象
line = f.readline()
f.close
line = line[:-3]
line =line.split('、')
race = ''.join(line)
race = race.replace('族','')
font_list = os.listdir('font')
for i in range(100):
    for l in line:
        l = list(l[:-1])
        l = ' '.join(l)
        img=Image.open('templet/address.jpg')
        draw = ImageDraw.Draw(img)
        sex = random.choice(['男','女'])
        font_choice = random.choice(font_list)
        font = ImageFont.truetype('font/'+font_choice,30)
        draw.text((random.randint(10,70), random.randint(3,5)), sex+' '+l,(0,0,0),font=font)
#        draw.text((random.randint(100,150), random.randint(3,5)),l,(0,0,0),font=font)
        draw = ImageDraw.Draw(img)
#        img = img.resize((280, 32),Image.ANTIALIAS)
        img.save(face+l+ str(i)+".jpg")
        print(l)
        with open(face+l+ str(i)+'.txt',"w") as f1:    #设置文件对象
#          f1.write('性别'+sex+'民族'+ l[0])
            f1.write(sex +l)


'''
生成身份证正面 ID_number
'''
import time
import random
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import ger_id
import os 
font_list = os.listdir('font')
font = ImageFont.truetype('font/'+random.choice(font_list) ,33)
for i in range(20000):
    try:
        img=Image.open('templet/haoma.jpg')
        draw = ImageDraw.Draw(img)
        number = ger_id.generator()
        print(number)
        if random.random() < 0.2:
            number = ''.join(number)
        else:
            number = ' '.join(number)
        font_choice = random.choice(font_list)
        font = ImageFont.truetype('font/'+'OCR-B 10 BT.ttf',30)
        draw.text((random.randint(5,40),random.randint(0,15)), number,(0,0,0),font=font)
        draw = ImageDraw.Draw(img)
#        img = img.resize((280, 32),Image.ANTIALIAS)
        number = number.replace(' ','')
        img.save(face+number+".jpg")
        print(number)
        
        with open(face+number+'.txt',"w") as f1:    #设置文件对象
          f1.write(number)
    except:
        print('error')





