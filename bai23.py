# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:37:22 2024

@author: Kiều Trinh
"""

import math
print("ax^2 + bx + c =0")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - (4*a*c)
if delta < 0:
    print("Phương trình vô nghiệm ")
elif delta == 0:
    x =-(b) /(2*a)
    print("x =" ,x)
else: 
    print("Phương trình có hai nghiệm phân biệt")
    x1= (-(b) + math.sqrt(delta))/ (2*a)
    x2= (-(b) - math.sqrt(delta))/ (2*a)
    print("x1=" ,x1)
    print("x2=" ,x2)
