#Sixth exercise: write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def keri_soz(string): #We opened new function. Name of the function is - keri_soz.
    word = string.split() #We opened new variable and maked string as a list using split operation.
    word.reverse() #With this operation we can write words as a reversing format. 
    print(' '.join(word)) #We joined the strings using ''.join() method.

exercise6 = input("Enter a string: ")
keri_soz(exercise6)
