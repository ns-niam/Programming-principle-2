#Python: math (Third exercise)
#Write a Python program to calculate the area of regular polygon

import math
n = int(input("Enter the number: "))
s = int(input("Enter the number: "))
area = (n*s**2) / (4 * math.tan(math.pi / n)) 
print(area)
