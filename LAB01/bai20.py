# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:55:53 2024

@author: Nguyễn Ngọc Như Quỳnh
"""
a=int(input("Nhập a = "))
b=int(input("Nhập b = "))
c=int(input("Nhập c = "))
#Giả định số lớn nhất là a
solonnhat=a
if b>solonnhat:
    solonnhat=b
if c>solonnhat:
    solonnhat=c
print("Số lớn nhất là: ",solonnhat)
