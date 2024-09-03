# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:37:56 2024

@author: Kiều Trinh
"""
chu = input("Nhập vào chữ cái :")
if chu.islower():
    chumoi= chu.upper()
else:
    chumoi= chu.lower()
print("Chứ cái sau khi đổi : ",chumoi)
