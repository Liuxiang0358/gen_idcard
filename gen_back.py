#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:42:44 2019

@author: lx
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 20:13:09 2019

@author: lx
"""
"""
生成公安居和ID

"""
####
import random
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import ger_id
#charac_copy = charac.charac()
#font = ImageFont.truetype('STSONG.TTF',40)
#font_load = os.listdir('font')
#font = ImageFont.truetype('simhei.ttf',50)
#font_load =      
back = '/home/lab507c/data_ocr1/'
#font_name =  'simhei.ttf' 
#total = ger_id.gen_local()
#
#for i in range(1):
#    for number in total:
#    #        number = '丰宁满族自治县'
#        number = number + '公安局' 
#        print(number)
#        img=Image.open('templet/jiguan.jpg')
#        draw = ImageDraw.Draw(img)
#        font_size = random.randint(40,41)
#        print(font_name)
#        font = ImageFont.truetype('font/'+font_name ,font_size)
#        draw.text((180+random.randint(0,5),random.randint(3,5)),number,(0,0,0),font=font)
#        draw = ImageDraw.Draw(img)
#        img = img.resize((280, 32),Image.ANTIALIAS)
#        img.save( back+ number+str(i)+".jpg")
#        with open( back+ number+str(i)+'.txt',"w") as f1:    #设置文件对象
#          f1.write("签发机关" + number)

'''
生成有效日期
'''
import time
import random
import os
a1=(1976,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(2030,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳
font = ImageFont.truetype('font/simhei.ttf' ,30)
#随机生成10个日期字符串
font_name =  'simhei.ttf' 
font_list = os.listdir('font')
for i in range(10000):   
    
#    try:
        print(i)
        start=time.mktime(a1)    #生成开始时间戳
        end=time.mktime(a2)      #生成结束时间戳
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date_start = time.strftime("%Y.%m.%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        start=time.mktime(a1)    #生成开始时间戳
        end=time.mktime(a2)      #生成结束时间戳
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t) 
        
        date_end = time.strftime("%Y.%m.%d",date_touple)
        if random.random() < 0.25:
            date_end = '长期'
        data = date_start + '-' +date_end
        data = ' '.join(data)
        print( data)
        img=Image.open('templet/number.jpg')
        draw = ImageDraw.Draw(img)
        font_choice = random.choice(font_list)
        font = ImageFont.truetype('font/'+font_choice,32)
        draw.text((random.randint(0,50),random.randint(0,10)),data,(0,0,0),font=font)
        draw = ImageDraw.Draw(img)
        data = data.replace(' ','')
        img = img.resize((280, 32),Image.ANTIALIAS)
        img.save(back+data+".jpg")
        with open(back+data+'.txt',"w") as f1:    #设置文件对象
          f1.write(data)
#    except:
#        print('error')

