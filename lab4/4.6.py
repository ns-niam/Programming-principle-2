# Python: Iterator and Generator (First Exercise)
# Create a generator that generates the squares of numbers up to some number

def square_generator(n):  # We defined a function called square_generator
    for i in range(1, n + 1): 
        print(i ** 2)

num = int(input("Enter a limit: "))
square_generator(num)
