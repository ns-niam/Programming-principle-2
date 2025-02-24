#Python: math (fourth exercise)
#Write a Python program to calculate the area of a parallelogram.

import math

a = int(input())
h = int(input())
s = a*h
print(s)

#Area of a parallelogram with sinus: 

length = int(input())
high = int(input())
sin_angle = int(input())
convert = math.radians(sin_angle)
area = length * high * math.sin(convert)
print(area)
