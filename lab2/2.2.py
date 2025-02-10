#Python: Operatorss

# Addition: +
# Multiplication: *
# Subtraction: -
# Divide: /
# Moduls: %
# Exponentiation: **
# Floor division: //

a = 5
b = 5 
c = a+b #Result: 10
q = a-b #Result: 0
w = a*b #Result: 25 
e = a**b #Result: 5*5*5*5*5 = 3125
r = a/b #Result: 1.0
t = a%b #Result: 0
y = a//b #Result: 1
print (c)
print (q)
print (w)
print (e)
print (r)
print (t)
print (y)

# Equal: ==
# Not equal: !=
# Greater than: >
# Greater than or equal: >=
# Less than: <
# Less than or equal: >=

u = int(input())
i = int(input())

if u > i: 
    print("u is greater than i")
elif i > u: 
    print("i is greater than u")
elif u == i: 
    print("u equals i")
else: 
    print("ERROR")
    
#Python Logical Operators:

# AND: Returns True if both statements are true
# OR:  Returns True if one of the statements is true
# NOT: Reverse the result, returns False if the result is true

o = int(input())
p = int(input())
s = int(input())

if o > p and s > p: 
    print("YES")
else: 
    print("NO")
