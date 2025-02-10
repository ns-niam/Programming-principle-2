#Python (Data types): In this file i will write the informations about this topic and practise!

#Text type = str; 
#Numeric type: int, float, double, complex; 
#Sequence Types: list, tuple, range;
#Mapping Type:	dict;
#Set Types:	set, frozenset;
#Boolean Type: bool;

y = 100
print(type(y)) #With this operation we can define the type of the variable; Result: <class 'int'>

x = "My name is Niam"
print(type(x)) #With this operation we can define the type of the variable; Result: <class 'str'>

z = "100"
print (type(z)) #Result of the operation is <class 'str'>. Why? Because i am writing the variable with "".

b = 20.5 
print(type(b)) #With this operation we can define the type of the variable. Result: <class 'float'>

u = ["PP1", "PP2", "Discrete structure"]
print(type(u)) #With this operation we can define the type of the variable. Result: <class 'list'>

v = {"PP1", "PP2", "Discrete structure"}
print (type(u)) #Result: <class 'set'>

t = True
print (type(t)) #Result: <class 'bool'>

a = int(input())
l = int(input())
c = a+l
print(c) #Result: 7. I give variable in <class 'int'> form at the console;


q = 5
d = "3"
p = a+d
print(p) #Result: Error! We can not add int with str; 

j = 1j
print(type(j)) #Result: complex. If we write number and letter together, the type will be complex. BUT IT WORKS ONLY FOR "j". Example: 1j, 2j, 3j..add()
