# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:03:51 2024

@author: Nguyễn Ngọc Như Quỳnh
"""
gio=int(input("Nhập giờ = "))
phut=int(input("Nhập phút = "))
giay=int(input("Nhập giây = "))
if 0<=gio<=23 and 0<=phut<=59 and 0<=giay<=59:
    print("Giờ hợp lệ")
else:
    print("Không hợp lệ")
