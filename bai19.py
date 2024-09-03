# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:16:08 2024

@author: Kiều Trinh
"""
a = int(input("Nhập số thứ nhất:"))
b = int(input("Nhập số thứ hai:"))
c = int(input("Nhập số thứ ba:"))
d = int(input("Nhập số thứ tư:"))
sonhonhat = a
if b < sonhonhat:
    sonhonhat = b
if c < sonhonhat:
    sonhonhat = c 
if d < sonhonhat:
    sonhonhat = d
print("Số nhỏ nhất trong 4 số là :", sonhonhat)
    
