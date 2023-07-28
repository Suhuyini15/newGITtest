# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:39:16 2023

@author: SUHUYINI
"""

#USER ENTERS NUMBERS

print("Enter the two numbers:")
num1 = int(input())
num2 = int(input())


if (num1 > num2):
    a = num1
    b = num2

elif(num2 > num1):
    a = num2
    b = num1
    
else:
    print(" WRONG INPUT ")
    
 
#FIND HCF

rem = 1    
while rem >= 1:
    rem = a % b
    a = b 
    b = rem
HCF = a


#FIND LCM

LCM = ((num1 * num2)/HCF)


print("  ")
#DISPLAY VALUEDS

print("The LCM of", num1 , "and" , num2 , "is" , LCM) 
print("The HCF of", num1 , "and" , num2 , "is" , HCF) 

    
    
   
    
    
    
        
        


