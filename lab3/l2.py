#Python: Lambda
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

#Using lambda we can write function smaller than def function.

x = lambda x: x * 6
print(x(5)) #Result: 30. I give number five to the variable.

#Writing this operation with def: 
def myfunction(y):
    print(y*6)
mynumber = int(input())
myfunction(mynumber)

q = lambda a,b: a + b
print(q(5,6))

w = lambda r,t: r**t
print(w(2,3))

#ERROR TYPE OF CODE:
e = lambda i: i+u
print(e(2,3)) #Error: <lambda>() takes 1 positional argument but 2 were given. 

r = lambda number1, number2, number3 : number1 + number2 + number3
print(x(5, 6, 2))

#Let's write code in another form: Two variable

t = u = lambda num1, num2, num3: num1+num2+num3
print(t(5,6,7)) #We give numbers to variable "t"
print(u(5,6,7)) #We give numbers to variable "u"

#Let's write code with def and lambda
def sumofnumbers(num):
    sum = lambda p: num * p
    print(sum(11)) 
lum = sumofnumbers(2)

def funct(num4):
    lambda g: num4 * g
    print(g(2))
newnumber = funct(2)
