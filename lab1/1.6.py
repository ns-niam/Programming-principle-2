#Python: string. In this file i will write some informations about this topic and practise; 
#First information: "" = '' for example "Hello" is same as 'Hello'

print("Hello World!")

a = "hello"
print(type(a))

b = "Hello World"
print(b[3]) #With this operation we can see third character of the sentence. Result: l

c = "Md Sha Niamatullah"
print(len(c)) #with this operation we can see how many letters and spaces there are in the sentence. Result: 19.

h = "5"
p = "3"
print (h+p) #Result: 53. Why? Because program will be consider the 5 and 3 same as the string. Thats why 5+3 = 53 in the str form.

yer = "Hello World"
print(yer[3:7]) #Result will be: characters from position 3 to position 7 (not included). Result is: l0,

ret = "Hello World"
print(ret[:5]) #The first 4 elements. Result: Hello

ter = "Md Sha Niamatullah"
print(ter.upper()) #All elements in capital letters

ios = "Md Sha Niamatullah"
print(ios.lower()) #All elements in lowercase

lot = "PP1, PP2, Discrete structures"
print(lot.split()) #Result: ['PP1,', 'PP2,', 'Discrete', 'structures'] Using split we can create a list. If any spaces between words it will be new word in list.

#Second information: The strip() method removes any whitespace from the beginning or the end:

str = " Md Sha Niamatullah "
print (str.strip()) #Result: this operation removes spaces in the sentences. Spaces that located at the beginning and at the end. 

top = "Hello"
pot = ", PP2!"
result = top + " " + pot
print(result) #Concatenate. Result is: Hello, PP2!
