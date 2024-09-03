# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:12:18 2024

@author: Kiều Trinh
"""
gio = int(input("Nhập số giờ:"))
phut = int(input("Nhập số phút:"))
giay = int(input("Nhập số giây:"))
tonggiay= gio*3600+ phut*60+ giay
print(f"{gio} giờ {phut} phút {giay} giây tương đương với {tonggiay} giây")
