#Python: iterator and generator (fifth exercise)
#Implement a generator that returns all numbers from (n) down to 0.

def number(n):
    while n >= 0: 
        yield n  #The yield keyword is used to create a generator function
        n = n-1
a = int(input())
for i in number(a):
    print(i, end=" ")
