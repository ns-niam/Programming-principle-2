#LAB5: 
#Tenth exercise: Write a Python program to convert a given camel case string to snake case.

import re
text = "camelCaseExample"
snake_case = re.sub(r'([A-Z])', r'_\1', text).lower()
snake_case = snake_case.lstrip('_')
print(snake_case) 
