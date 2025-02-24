# Python: Iterator and Generator (First Exercise)
# Create a generator that generates the squares of numbers up to some number

def square_generator(n):  # We defined a function called square_generator
    for i in range(1, n + 1): 
        print(i ** 2)

num = int(input("Enter a limit: "))
square_generator(num)

# Python: Iterator and Generator (Second Exercise)
# Write a program using a generator to print the even numbers between 0 and n in comma-separated form where n is input from the console

def even_number(n):  # We defined a function called even_number
    for i in range(0, n + 1):  # for loop for iterations
        if i % 2 == 0:
            yield str(i)  # yield functions like return and print. We need str for using join operator

n = int(input("Enter a number: "))
result = ",".join(even_number(n))
print("Even numbers:", result)
