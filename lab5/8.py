#LAB 5
#Eighth exercise: Write a Python program to split a string at uppercase letters.

import re 
txt = input("Enter the word: ")
a = re.split(r'(?=[A-Z])', txt)
print(a)
