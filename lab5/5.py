#LAB 5
#Fifth exercise: Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re
txt = input("Enter the word: ")
pattern = r"^a.*b$"
a = re.fullmatch(pattern, txt)
if a: 
    print("YES, this word correct. Word is: ", txt)
else: 
    print("NO, this word incorrect. Word is: ", txt)
