#Python: iterator and generator (fourth exercise)
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values

def squares (a,b):
    for i in range (x,y+1):
        yield str(i**2)
        
a = int(input())
b = int(input())
res = ",".join(squares(a,b))
print(res)
