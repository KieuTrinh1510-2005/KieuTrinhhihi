# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:29:03 2024

@author: Kiều Trinh
"""
x = input("Nhập giờ cần đổi (hh:mm:ss): ")
gio,phut,giay =  map(int, x.split(":"))
tonggiay= gio*3600 + phut*60 + giay
print("Tổng giây : ", tonggiay)
