#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 02:35:50 2019

@author: lab507c
"""
from faker import Faker
fake = Faker('zh_CN')

with open('gen_name'+'.txt','w',encoding='utf-8') as f:
    for i in range(300000):
        name = fake.name()
        name =list(name)
        name = ' '.join(name)
        f.write(name + '\n')
        print(name)