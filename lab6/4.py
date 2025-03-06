#Built - in functions: 
#Fourth exercise: Write a Python program that invoke square root function after specific milliseconds

import time  
import math 

n = int(input("Enter a number: "))  
t = int(input("Enter delay in milliseconds: ")) 

time.sleep(t / 1000)  
result = math.sqrt(n)
print(f"Square root of {n} after {t} milliseconds is {result}")
