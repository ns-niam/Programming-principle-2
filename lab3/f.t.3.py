#Third exercise: write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
#How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    for tauyk in range(numheads + 1):
        koyan = numheads - tauyk
        if 2 * tauyk + 4 * koyan == numlegs:
            return tauyk, koyan
        
print(solve(35, 94)) 
