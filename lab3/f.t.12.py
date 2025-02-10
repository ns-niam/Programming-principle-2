#Twelve exercise: define a functino histogram() that takes a list of integers and prints a histogram to the screen.
#For example, histogram([4, 9, 7]) should print the following:

def histogram(numbers):
    for num in numbers: 
        print('*' * num)  #Generating the corresponding ' * ' characters for each number

histogram([4, 9, 7])
