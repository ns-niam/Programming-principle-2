#Bulit - in functions:
#second exercise: Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case.

txt = input("Enter the word: ")
upper_count = 0
lower_count = 0

for char in txt: 
    if char.isupper(): 
        upper_count += 1
    elif char.islower():
        lower_count += 1
    
print("Upper case letters: ", upper_count)
print("Lower case letters: ", lower_count)
