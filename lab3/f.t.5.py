#Fifth exercise: write a function that accepts string from user and print all permutations of that string.

from itertools import permutations #It is library of python. If we want to find permutations of string, we often use this library
def find_permutations(string):
    all_permutations = permutations(string) #We found all permutations of string.
    print("All permutations of string: ") #To print permutations.
    for result in all_permutations: 
        print(''.join(result)) #With "join" we can print the permutation
        
exercise5 = input("Enter a string: ") #With this operation we can enter a string from console.
find_permutations(exercise5) #Give string to function. The name of function is - find_permutations.
