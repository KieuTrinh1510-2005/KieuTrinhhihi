# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:50:49 2024

@author: Kiều Trinh
"""
import math
a= float(input("Nhập a:"))
b= float(input("Nhập b:"))
if a<=0 or b<=0 or a==b:
    print("a,b phải là số lớn hơn 0 và a,b khác nhau.")
else:
    x=(a+b)/(math.pow(a,1/3) + math.pow(b,1/3)) - math.pow(a*b,1/3)
    y=(math.pow(a,1/3) - math.pow(b,1/3))**2
    print("Gía trị biểu thức = ", x/y)
    

