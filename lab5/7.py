
# Seventh exercise: Write a Python program to convert a snake_case string to a camelCase string.

import re 
txt = input("Enter the snake case string: ")
result = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), txt) # Convert the letter after an underscore to uppercase.
result = result.capitalize() # Capitalize the first letter.
print(result)
