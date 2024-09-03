# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:36:30 2024

@author: Kiều Trinh
"""
import math
a = float(input("Nhập vào bán kính hình tròn:"))
C = 2*math.pi*a
print("Chu vi của hình tròn :",C)
S = (C**2)/(4*math.pi)
print("Diện tích hình tròn :",S)
