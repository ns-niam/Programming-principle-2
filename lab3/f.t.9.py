#Nineth exercise: write a function that computes the volume of a sphere given its radius.
def volume(radius): #We opened new function. Name of the function is volume. 
    result = 4/3 * (3.14159 * (radius**3)) #Formula for finding the volume
    print(result) #Print result
    
exercise9 = int(input()) 
volume(exercise9)
