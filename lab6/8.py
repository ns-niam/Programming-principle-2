#File handing.
#Seventh exercise: Write a Python program to copy the contents of a file to another file.

first_file = "C:/Users/user/niam/PP2/Lab 6/file2.txt"
second_file  = "C:/Users/user/niam/PP2/Lab 6/file.txt"

a = open(first_file, "r")
b = open(second_file, "w+")
for i in a: 
    b.write(i)
print(b.read())
print("File copyied successfully! File copyed from a to b")
