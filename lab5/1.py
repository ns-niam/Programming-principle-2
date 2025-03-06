# LAB 5
# First exercise: Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
txt = ["abc", "ab", "abb", "bb", "bca", "b", "ba", "abbbbbbb", "a", "aaa"]
pattern = r"^ab*"
for i in txt: 
    a = re.fullmatch(pattern, i)
    if a: 
        print(f'"{i}" Correct')
    else:
        print(f'"{i}" Incorrect')
        
        
# WHAT WE DID?

    # 1. We imported the 're' module to use regular expressions.
    # 2. We defined a list of strings that we want to check.
    # 3. We defined a regular expression pattern: "ab*" means "a followed by zero or more b's".
    # 4. We used a loop to iterate over the list of strings.
    # 5. For each string, we used the 'fullmatch' function from the 're' module to check if it matches the pattern.
