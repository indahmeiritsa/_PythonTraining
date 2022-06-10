# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 16:24:17 2022

@author: 007660
"""

temp = input("Ketikan temperatur yang ingin dikonversi, eg. 45F, 120C: ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == "C":
    result = int(round((9 * degree) / 5 + 32))
elif i_convertion == "F":
    result = int(round((degree - 32) * 5 / 9))
else:
    print("Masukan input yang benar")

print("Temperaturnya adalah", result, "derajat")