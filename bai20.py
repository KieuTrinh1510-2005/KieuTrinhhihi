# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:32:20 2024

@author: Kiều Trinh
"""
a = int(input("Nhập số thứ nhất :"))
b = int(input("Nhập số thứ hai :"))
c = int(input("Nhập số thứ ba :"))
solonnhat = a
if b > solonnhat:
    solonnhat = b
if c > solonnhat:
    solonnhat = c
print("Số lớn nhất là:",solonnhat)

