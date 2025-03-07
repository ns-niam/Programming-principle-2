#File handing.
#Fourth exercise: Write a Python program to count the number of lines in a text file.

a = open("C:/Users/user/niam/PP2/Lab 6/file.txt", "r")
lines = a.readlines()
print(len(lines))
