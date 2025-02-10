#Fourth exercise:  you are given list of numbers separated by spaces. 
#Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def is_prime(n): 
    if n < 2: #Numbers, which less than 2 they are not prime. 
        return False 
    for i in range(2, int(n**0.5) + 1): #Why we use int(n**0.5)? Because if we use this form, it will be effective. We can test primt numbers with numbers from 1 to 9
        if n % i == 0: #If our number divided i, then number is not prime.   
            return False 
    return True 
 
def filter_prime(numbers): #We opened second function for sorting numbers. Filter prime - is name of the function. 
    return [num for num in numbers if is_prime(num)] #If numbers are prime, then we save them to "num" variable, and make list of prime numbers, then print. 
 
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
