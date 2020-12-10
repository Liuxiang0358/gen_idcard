#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:08:10 2019

@author: lx
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 20:13:09 2019

@author: lx
"""

'''
生成身份证正面 地址

'''

import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import charac
import os
import random
charac_copy = charac.character()
charac_copy = ''.join(charac_copy)
charac_copy =  charac_copy.replace('\n','')
charac_copy =  charac_copy.replace('\t','')
charac_copy =  charac_copy.replace(' ','')
#font_list = os.listdir('font')'simhei.ttf'
font_list = ['msyh.ttf']
dirth = '/home/lx/data/single_char'
#dirth = 'single_char'
for char in charac_copy: 
    print(char)
    for i in range(5):
        font_char = os.path.join(dirth,'val',char)
        if os.path.isdir(font_char) != True:
            os.makedirs(font_char)
        img = Image.new("RGB",(32,32), (255,255,255))
        draw = ImageDraw.Draw(img)
        font_choice = random.choice(font_list)
        font_size = random.randint(23,25)
        font = ImageFont.truetype('font/'+ font_choice,font_size)
        draw.text((5,0),char,(0,0,0),font=font)
        draw = ImageDraw.Draw(img)
        img.save(font_char+'/'+str(i)+".jpg")

