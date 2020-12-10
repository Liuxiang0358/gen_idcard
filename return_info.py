from faker import Faker
import random
import ger_id
import time
import re
fake = Faker('zh_CN')
f = open("race.txt","r")   #设置文件对象
line = f.readline()
f.close()
line = line[:-3]
races =line.split('、')

a1=(1935,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(2030,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳

def cut_text(text,lenth): 
    textArr = re.findall('.{'+str(lenth)+'}', text) 
    textArr.append(text[(len(textArr)*lenth):]) 
    return textArr 

def return_name():
    name = fake.name()
    if len(name)==2:
        name = name[0] + ' ' + name[1]
    return name

def return_address():
    add = fake.address()+"号"
    add = add.replace(" ",'')
    print(add)
    return cut_text(add,11)

def return_sex():
    return random.choice(["男","女"])

def  return_nation():
    return random.choice(races).replace("族",'')

def  return_time():
    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳
    t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)    #将时间戳生成时间元组
    date = time.strftime("%Y.%m.%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
    data = date.split('.')
    for i in range(3):
        if len(data[i]) == 2 and data[i][0]=='0':
            data[i] = data[i].replace("0",'')
    return data

def return_number():
    number = ger_id.generator()
    number = ''.join(number)
    return number 

def return_usedtime():
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
    return data

def return_info():
    total = ger_id.gen_local()
    number = random.choice(total) + '公安局'
    return number 