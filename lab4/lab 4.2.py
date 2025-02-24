#Python: math (Second exercise)
#Write a Python program to calculate the area of a trapezoid

import math
height = int(input("Enter the height: "))
value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
res = abs((value1 + value2) * height) / 2 
print(res)