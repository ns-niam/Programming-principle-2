#Second exercise:  read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
#The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def my_task2(fahrenheit):
    C = (5 / 9) * (fahrenheit - 32)
    print(C)
exercise2 = int(input())
my_task2(exercise2)
