
#Fourth exercise: Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
txt = ["Almaty", "Regex", "Hello", "PrinT", "KYZYLORDA"]
pattern = r"^[A-Z][a-z]+$"
for i in txt: 
    a = re.findall(pattern, i)
    if a: 
        print("The word that starts with the uppercase letter and ends with lowercase: ", a)
