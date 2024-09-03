# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:41:37 2024

@author: Kiều Trinh
"""
a = int(input("Nhập giờ:"))
b = int(input("Nhập phút:"))
c = int(input("Nhập giây:"))
if 0<= a <= 23 and 0<= b <= 59 and 0<= c <= 59:
    print("Thời gian hợp lệ.")
else:
    print("Thời gian Không hợp lệ.")
    
