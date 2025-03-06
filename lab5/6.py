#LAB 5
#Sixth exercise: WWrite a Python program to replace all occurrences of space, comma, or dot with a colon.

import re 
txt = input("Enter the string: ")
a = re.sub(r"[ , .]", ":", txt)
print(a)
