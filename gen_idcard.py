import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import return_info as ri
import uuid
import time
import re
import random
import os

def cut_text(text,lenth): 
    textArr = re.findall('.{'+str(lenth)+'}', text) 
    textArr.append(text[(len(textArr)*lenth):])
    return textArr 

def findall_chinese(s):
    '''
    查找字符串中的所有汉字，返回列表
    :param s: 待查找字符串
    :return: list
    '''
    res = re.compile('[\u4e00-\u9fff]+').findall(s)
    length = 0
    for r in res:
        length += len(r)
    return length

name = ri.return_name()
sex = ri.return_sex()
nation = ri.return_nation()
date = ri.return_time()
addresses = ri.return_address()
id_number = ri.return_number()
effective_date = ri.return_usedtime()
issuing_authority = ri.return_info()

location ={}   ### 保存地址 

imageFile = "templet/face.jpg"
im=Image.open(imageFile)

'''
print name
'''
x = 220
y = 100
w = 50
h = 63
k = len(name)
width = k * w
if ' ' in name:
    width = k * w *0.75
font = ImageFont.truetype('font/STSONG.TTF' ,50)
draw = ImageDraw.Draw(im)
tmp = [(x,y),(x+width,y),(x+width,y+h),(x,y+h),(x,y)]
location["name"] = tmp[:-1]
draw.line(tmp,width=4,fill='red')
draw.text(( x, y),name,(0,0,0),font=font)   ###420 160

'''
print sex
'''
x = 220
y = 185
w = 40
h = 50
k = len(sex)
width = k * w
font = ImageFont.truetype('font/STSONG.TTF' ,40)
draw = ImageDraw.Draw(im)
tmp = [(x,y),(x+width,y),(x+width,y+h),(x,y+h),(x,y)]
location["sex"] = tmp[:-1]
draw.line(tmp,width=4,fill='red')
draw.text(( x, y),sex,(0,0,0),font=font)   ###420 160

'''
print nation
'''
x = 450
y = 180
w = 40
h = 50
k = len(nation)
width = k * w
font = ImageFont.truetype('font/STSONG.TTF',40)
draw = ImageDraw.Draw(im)
tmp = [(x,y),(x+width,y),(x+width,y+h),(x,y+h),(x,y)]
location["sex"] = tmp[:-1]
draw.line(tmp,width=4,fill='red')
draw.text(( x, y),nation,(0,0,0),font=font)   ###420 160

'''
print date
'''
xy_list = [(220,260),(385,260),(485,260)]
w = 22
h = 40
font = ImageFont.truetype('font/STSONG.TTF' ,40)
draw = ImageDraw.Draw(im)
for i,(x,y) in enumerate(xy_list): 
    k = len(date[i])
    width = k * w
    location["nation"] = tmp[:-1]
    draw.text(( x, y),date[i],(0,0,0),font=font)   ###420 160
    x = x
    y = y+7
    tmp = [(x,y),(x+width,y),(x+width,y+h),(x,y+h),(x,y)]
    draw.line(tmp,width=4,fill='red')

'''
print address
'''
font = ImageFont.truetype('font/STSONG.TTF' ,40)
x = 220
y = 355
w = 40
h = 50
for i,address in enumerate(addresses):
    if address != '':
        k = len(address)
        chinese_len = findall_chinese(address)
        width = chinese_len * w + (len(address) - chinese_len) * w * 0.5
        draw = ImageDraw.Draw(im)
        
        x = 220 
        y = 355 + i * 60
        draw.text(( x, y),address,(0,0,0),font=font)
        tmp = [(x,y),(x+width,y),(x+width,y+h),(x,y+h),(x,y)]
        location["address"] = tmp[:-1]
        draw.line(tmp,width=4,fill='red')
       ###420 160

'''
print id_number
'''
x = 420
y = 570
w = 30
h = 43
k = len(id_number)
width = k * w
font = ImageFont.truetype('font/OCR-B 10 BT.ttf' ,50)
draw = ImageDraw.Draw(im)
tmp = [(x,y),(x+width,y),(x+width,y+h),(x,y+h),(x,y)]
location["id_number"] = tmp[:-1]
draw.line(tmp,width=4,fill='red')
draw.text((x, y),id_number,(0,0,0),font=font)   ###420 160

im.save("res1.jpg")



imageFile = "templet/back.jpg"
im=Image.open(imageFile)
'''
print issuing_authority
'''
x = 440
y = 480
w = 50
h = 60
k = len(issuing_authority)
width = findall_chinese(issuing_authority) * w + (len(issuing_authority) -findall_chinese(issuing_authority)) * w * 0.6
font = ImageFont.truetype('font/simhei.ttf' ,40)
draw = ImageDraw.Draw(im)
tmp = [(x,y),(x+width,y),(x+width,y+h),(x,y+h),(x,y)]
location["issuing_authority"] = tmp[:-1]
draw.line(tmp,width=4,fill='red')
draw.text(( x, y),issuing_authority,(0,0,0),font=font)   ###420 160

'''
print effective_date
'''
x = 440
y = 580
w = 40
h = 60
k = len(effective_date)
width = findall_chinese(effective_date) * w + (len(effective_date) - findall_chinese(effective_date)) * w * 0.6
font = ImageFont.truetype('font/simhei.ttf' ,40)
draw = ImageDraw.Draw(im)
tmp = [(x,y),(x+width,y),(x+width,y+h),(x,y+h),(x,y)]
location["name"] = tmp[:-1]
draw.line(tmp,width=4,fill='red')
draw.text(( x, y),effective_date,(0,0,0),font=font)   ###420 160
im.save("res2.jpg")
