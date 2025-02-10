#Python: Conditions

# 1) Equals: a == b
# 2) Not equals: a != b
# 3) Less than: a < b
# 4) Greater than: a > b
# 5) Less than or equal: a <= b
# 6) Greater than or equal: a >= b

#I asked 15 exercise from Chat GPT for this topic. Now i will solve 15 exercise for if | else. I ask only exercise, not solution :)

#First:  Write a program to check if a number is even or odd.
q = int(input())
if q%2 == 0: 
    print("Number is even")
else:
    print("Number is odd")
    
#Second: Determine if a number is positive, negative, or zero.
w = int(input())
if w > 0: 
    print("Number is positive")
elif w < 0: 
    print("Number is negative")
else: 
    print("Number is zero")
    
#Third: Compare two integers and find the larger one.
e = int(input())
r = int(input())
if e > r: 
    print("e is greater than r")
elif r > e: 
    print("r is greater than e")
else: 
    print("e and r are equal")
    
#Fourth: Check if a number is divisible by 5.
t = int(input())
if t%5 == 0: 
    print("Number is divisible by 5")
else: 
    print("Number is not divisible by 5")
    
#Fifth: Check Leap Year
u = int(input())
if u%4 == 0 and (u%100 != 0 or u%400 == 0): 
    print("Leap Year")
else: 
    print("Not a Leap Year")
    
#Sixth: Minimum of Two Numbers
y = int(input())
i = int(input())
if y > i: 
    print(i)
else: 
    print(y)
    
#Seventh: Pass or Fail
o = int(input())
if o > 50:
    print("Pass")
else:
    print("Fail")
    
#Eighth: Grade Calculator
grade = float(input())
if grade > 90: 
    print("Grade: A")
elif grade > 80 and grade < 90: 
    print("Grade: B")
elif grade > 70 and grade < 79:
    print("Grade: C")
elif grade > 60 and grade < 69:
    print("Grade: D")
else: 
    print("Grade: F")
    
#Ninth: Even Numbers Between Two Numbers
first = int(input())
second = int(input())
if first % 2 == 0 and second % 2 == 0:
    print ("All numbers even")
else: 
    print ("Not all numbers even")
    
#Tenth: Age Group
age = int(input())
if age < 13: 
    print("Child")
elif age > 13 and age < 19: 
    print("Teen")
else: 
    print("Adult")
    
#Eleventh: Absolute Difference
b = int(input())
v = int(input())
difference = b - v
if difference > 10: 
    print("Big Difference")
else: 
    print("Small Difference")

#Twelve: Largest of Three Numbers
firstt = int(input())
secondd = int(input())
thirdd = int(input())
if firstt > secondd and firstt > thirdd:
    print(firstt)
elif secondd > firstt and second thirdd: 
    print(secondd) 
elif thirdd > secondd and thirdd > firstt: 
    print(thirdd)
else: 
    print("All numbers are equal")
    
#Thirteenth: Find Quadrant
k, s = map(int, input("Enter coordinates (k s): ").split())
if k > 0 and s > 0:
    print("Quadrant 1")
elif k < 0 and s > 0:
    print("Quadrant 2")
elif k < 0 and s < 0:
    print("Quadrant 3")
elif k > 0 and s < 0:
    print("Quadrant 4")
else:
    print("On the Axis")

#Fourteenth: Is Vowel or Consonant
vowel = int(input())
if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
    print("Vowel")
else: 
    print("Consonant")

#Fifteenth: Palindrome
word = int(input())
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
