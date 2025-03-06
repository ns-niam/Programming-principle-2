
#Third exercise: Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
txt = input("Enter the word: ")
pattern = r"^[a-z]+(_[a-z]+)*$"
a = re.fullmatch(pattern, txt)
if a: 
    print("Correct")
else: 
    print("Incorrect")
