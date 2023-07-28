# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:05:24 2023

@author: SUHUYINI
"""

print("Please enter a number:")
num=int(input())

#FIRST NUMBER
#     reverse number
remainder= (str(num)[::-1])
    
#   find first number
f_num = int(remainder)%10
print("The first number is",f_num)


#LAST NUMBER
l_num = num%10
print("The last number is",l_num)

#ADD
add = f_num + l_num

print("The sum of the first and last number is",add)