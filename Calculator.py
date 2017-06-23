#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
def parenthese(data):
    #去掉括号
    data_parenthese=re.search(r'\([^()]+\)',data).group()
    while True:
        if '/' in data_parenthese or '*' in data_parenthese:
            data_parenthese=multiply_or_divide(data_parenthese)
        else:
            break
    while True:
        if '-' in data_parenthese and not '(-' in data_parenthese or '+' in data_parenthese:
            data_parenthese=add_or_subtract(data_parenthese)
        else:
            break
    data_parenthese=data_parenthese.strip('()')
    data=data.replace(re.search(r'\([^()]+\)',data).group(),data_parenthese)
    if '*-' in data or '/-' in data:
        pick_up=re.search(r'[\d.]+[*/]-',data).group()
        data=data.replace(pick_up,'-'+pick_up.strip('-'))
    data=data.replace('+-','-')
    data=data.replace('--','+')
    return data

def add_or_subtract(data):
    #去掉加减号
    pick_up = re.search(r'-?[\d.]+[-+][\d.]+', data).group()
    result = calculate(pick_up)
    data = data.replace(pick_up, str(result))
    return data

def multiply_or_divide(data):
    #去掉乘除号
    pick_up=re.search(r'[\d.]+[/*][\d.]+',data).group()
    result=calculate(pick_up)
    data=data.replace(pick_up,str(result))
    return data

def calculate(data):
    #加减乘除的运算
    if '/' in data:
        return float(data.split('/')[0])/float(data.split('/')[1])
    if '*' in data:
        return float(data.split('*')[0])*float(data.split('*')[1])
    if '+' in data:
        return float(data.split('+')[0])+float(data.split('+')[1])
    if '-' in data:
        return float(data.split('-')[0])-float(data.split('-')[1])

data=input('请输入:')
data=data.replace(' ','')
while True:
    if '(' in data:
        data=parenthese(data)
    else:
        break
while True:
    if '/' in data or '*' in data:
        data=multiply_or_divide(data)
    else:
        break
while True:
    if '-' in data and not data.startswith('-') or '+' in data:
        data=add_or_subtract(data)
    else:
        break
print('结果:',data)


