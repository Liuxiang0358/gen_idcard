#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 20:13:09 2019

@author: lx
"""

'''
生成身份证正面 地址

'''
import re
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import charac
import random
import os
from collections import Counter

#charac_copy = charac. character()
#charac_copy = ''.join(charac_copy)
#charac_copy =  charac_copy.replace('\n','')
#charac_copy =  charac_copy.replace('\t','')
#charac_copy =  charac_copy.replace(' ','')
font_list = os.listdir('font')
face = '/home/lab507c/data_ocr/address/'
#face = 'face/'
f = open("address.txt","r")   #设置文件对象
line = f.readline()
lines = []
while line:             #直到读取完文件
    line = f.readline()  #读取一行文件，包括换行符
    lines.append(line)
f.close() #关闭文件
print(lines[0])

#total_charac = ''.join(lines)
#charac_copy = set(charac_copy)
#total_charac =set(total_charac)
'''
diff_total   [total.txt 去除一些字典中没有的子符]
diff_charc   [total.txt 没有涉及到的涉及到的生僻字]
'''
#diff_total = total_charac - ( charac_copy & total_charac)
#diff_charc = charac_copy - ( charac_copy & total_charac)
##diff = set(total_charac).symmetric_difference(charac_copy)
#len(diff_total )
#diff_total  = ''.join(diff_total )
#total_charac = ''.join(lines)
#
#for i in range(len(diff_total )):
#    total_charac = total_charac.replace(diff_total[i],'')
#print(len(total_charac))
'''
词频统计
charac_copy = list(choice)
print(random.shuffle(charac_copy))
charac_copy = ''.join(charac_copy)
res = Counter(charac_copy)

'''

'''
'msyhl.ttf',  0
' msyh.ttf',
'msyhbd.ttf',
'STZHONGS.TTF',
'STSONG.TTF',
'msyh.ttf'

'''

def cut_text(text,lenth): 
    textArr = re.findall('.{'+str(lenth)+'}', text) 
    textArr.append(text[(len(textArr)*lenth):]) 
    return textArr 

#total_cut = cut_text(total_charac,11)
#len( total_cut)

'''
给身份证正面写入文字  address  第一行
                      address1 第二行
'''
#clolr_choice = [(110,123,139),(24,116,205),(28,28,28),(0,0,0)]
clolr_choice = [(0,0,0)]
print(len(lines))
choice = random.sample(lines,10000)
for line in choice:
    print(line)
    line = line.replace('\n','')
    line = ''.join(list(line))
    total_cut = cut_text(line,11)
    total_cut = [x for x in  total_cut if x]
#    if random.random() < 0.5:
#        for cut in  total_cut:
#            img=Image.open('templet/address0.jpg')
#            font_choice = random.choice(font_list)
#            font_size = random.randint(33,35)
#            draw = ImageDraw.Draw(img)
#            font = ImageFont.truetype('font/'+font_choice ,font_size)
#            if font_choice in ['msyhl.ttf',' msyh.ttf','msyhbd.ttf','STZHONGS.TTF','STSONG.TTF','msyh.ttf']: 
#                draw.text((115,0),cut,random.choice(clolr_choice),font=font)
#            else:
#                draw.text((115,5),cut,random.choice(clolr_choice),font=font)
#            draw = ImageDraw.Draw(img)
#            cut = cut.replace(' ','')
#            img.save(face+cut+".jpg")
#            with open(face+cut+'.txt',"w") as f1:    #设置文件对象
#              f1.write('住址' + cut)
#    else:
    
    for cut in total_cut:
        p = random.randint(0,20)
        img=Image.open('templet/address.jpg')
        draw = ImageDraw.Draw(img)
        font_choice = random.choice(font_list)
        font_size = random.randint(30,33)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('font/'+ 'msyh.ttf',font_size)
#        if font_choice in ['msyhl.ttf',' msyh.ttf','msyhbd.ttf','STZHONGS.TTF','STSONG.TTF','msyh.ttf']: 
#            draw.text((10+p,0),cut,random.choice(clolr_choice),font=font)
#        else:
        draw.text((10+p,random.randint(0,1)),cut,random.choice(clolr_choice),font=font)
        draw = ImageDraw.Draw(img)
        cut = cut.replace(' ','')
        img = img.resize((280, 32),Image.ANTIALIAS)
        img.save(face+cut+".jpg")
        with open(face+cut+'.txt',"w") as f1:    #设置文件对象
          f1.write(cut)
'''
生成姓名
'''
#font_list  = os.listdir('font')
#diff_charc = list(diff_charc)
#len(diff_charc )
#f = open("name.txt","r")   #设置文件对象
#name = f.readline()
#names = []
#while name:             #直到读取完文件
#   name = f.readline()  #读取一行文件，包括换行符
#   names.append(name)
#f.close() #关闭文件
#print(names[0])
#for i,name in enumerate(names):
##    for j in range(len(diff_charc)):
#    name = list(name)
#    name[1] = diff_charc[i % len(diff_charc)] 
#    name = ''.join(name)
#    
#    img=Image.open('templet/name.jpg')
#    draw = ImageDraw.Draw(img)
##    font_choice = random.choice(font_list)
#    print(name)
#    font = ImageFont.truetype('font/'+'msyh.ttf',40)
#    draw.text((120,10),name,(0,0,0),font=font)
#    draw = ImageDraw.Draw(img)
#    img.save('face/'+name + str(i) + ".jpg")
#    with open("face/"+name + str(i) +'.txt',"w") as f1:    #设置文件对象
#      f1.write('姓名' + name)