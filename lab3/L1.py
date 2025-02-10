edit my name   #Python: functions 

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result

def my_functionn():
    print("Hello, it is my function")
    
# Def - We always start a function with def.
# My_function - it is name of the function. We can write any words instead of this.
# After name of function, we write () this. It means parameters of function.

def my_surname(surname): #My_surname is the name of the function. In parenthesis written "surname". It is parameter of function;
    print(surname + " " "Niam")
    
my_surname("MD ") #Result: MD NIAM
my_surname("SHA") #Result: SHA NIAm

#Next example: 
def my_function(surname, name): 
    print(surname + " " + name)

my_function("MD", "Niam") #Result: MD

#Next example: Error! 
def my_function(surname, name): 
    print(surname + " " + name)

my_function("MD", "Niam") #Result: MD NIAM
my_function("NIAM", 1234) #Error! We cannot concatenate string and integer.


def my_function(surname, name):
    print(surname + " " + name)
    
my_function("MD sha", "NIam") #Result: md sha niam
my_function(" Abdullah") #Result: Error! Why? Because in this parameter we have only one argument.

def my_function(*kids):
    print("The youngest child is " + kids[2]) #Why we used [2]? Because counting arguments starts from 0. 
my_function("Amina", "Arsen", "Ademi", "Adina") #Result: The youngest child is Ademi. We use a * if we do not know how many arguments we need.

#If i delete * it will be error. Why? Because parameter includes only one argument. 

def my_function(child1, child2, child3): #Keyword Arguments
    print("The youngest child is " + child1) #If we write 1child, 2child instead of child1 it will be error!
my_function(child1 = "Ademi", child2 = "Amina", child3 = "Adina") 

def my_function(**kids): #If we do not know how many elements we need and if we want to use keyword arguments.
    print("The youngest child is " + kids["child3"]) 
my_function(child1 = "Adina", child2 = "Amina", child3 = "Ademi")

#Print the elements with for loops: 
def my_kids(child):
    for x in child: 
        print(x)
    
n = ["Ademi", "Amina", "Adina"] #Result: Ademi, Amina, Adina
my_kids(n)


#Return values:
def my_function(x):
    return 10 * x 
print(my_function(5)) #If we do not use "print" we can not show it on th screen. That is why we need to write print. 
print(my_function(3))

#Recursion example: 
def recursion(x):
  if(x > 0):
    result = x + recursion(x - 1) #
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
recursion(6)


#I asked 10 exercise from Chat GPT and i solved them. Here solution of 10 example: 

#First exercise: Even or Odd
def is_even(number):
    if number % 2 == 0: 
        print("Even number")
    else:
        print("Odd number")
        
n = int(input())
is_even(n)

#Second exercise: Addition of two numbers
def addition(number1, number2):
    result = number1 + number2 
    print(result)

a = int(input())
b = int(input())
addition(a,b)

#Third exercise: Length of word
def length(word):
    print(len(word))
    
p = str(input())
length(p)

#Fourth exercise: exponentiation
def exponentiation(num, power):
    powerofnumber = num ** power 
    print(powerofnumber)
q = int(input())
w = int(input())
exponentiation(q,w)

#Fifth exercise: Reverse 
def reverse_word(word):
    print(word[::-1])
r = str(input())
reverse_word(r)

#Sixth exercise: Add hello after word.
def adding (word):
    print("Hello " + word)
t = str(input())
adding(t)

#Seventh exercise: the perimeter of a rectangle
def perimeter (x,y):
    print(2*(x+y))
u = int(input())
i = int(input())
perimeter(u,i)

#Eighth exercise: converting a negative number to a positive number
def minus_number(number):
    result = number * (-1)
    print(result)
g = int(input())
minus_number(g)

#Nineth exercise: Comparing three numbers
def comparing (number1, number2, number3):
    if number1 > number2 and number1 > number3:
        print(number1, "is the largest.")
    elif number2 > number1 and number2 > number3:
        print(number2, "is the largest.")
    else:
        print(number3, "is the largest.")

li = int(input())
qw = int(input())
er = int(input())
comparing (li, qw, er)

#Tenth exercise: finding percent of number: 
def percent(number, percent):
    divide = percent / 100
    result = number * divide
    print(result)

po = int(input())
pe = int(input())
percent(po, pe)
