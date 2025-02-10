# Python: Dictionaries 
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

mydict = {"Name": "Niam", "Age": 19, "City": "Dhaka", "Country": "Bangladesh"}
print(mydict) #Result: {'Name': 'Niam', 'Age': 19, 'City': 'Dhaka', 'Country': 'Bangladesh'}

print(mydict["Name"]) #Result is: Niam

#Duplicate not allowed: 
mydict = {
    "Name": "Niam",
    "City": "Dhaka",
    "Age": 19,
    "City": "Chittagong"
    }
print(mydict) #Program will keep the last "City" value (Chittagong).

#Length of dictionary: 
mydict = {
    "Name": "Niam",
    "City": "Dhaka",
    "Age": 19,
    "Country": "Bangladesh"
    }
print(len(mydict)) 

#TYPE OF DICTIONARY: 
print(type(mydict)) #Result: <class 'dict'>

#To make a dictionary:
mydict = dict(Name = "Niam", Age = 19, Country = "Bangladesh", City = "Dhaka")
print(mydict)

#REMOVING ITEMS FROM THE DICTIONARY: 
mydict.pop("Age")
print(mydict)

#REMOVING THE LAST ELEMENT:
mydict.popitem()
print(mydict) #This operation will delete the last element of the dictionary

#REMOVING ELEMENTS FROM THE DICTIONARY WITH CLEAR:
mydict.clear()
print(mydict)

#LOOP IN DICTIONARY: 
mydict = {
    "Name": "Niam",
    "City": "Dhaka",
    "Age": 19,
    "Country": "Bangladesh"
    }

for x in mydict: 
    print(x)
    
for x in mydict:
    print(mydict[x]) #Print values: Niam, Dhaka, 19, Bangladesh
    
for x in mydict.values():
    print(x) #'Niam', 'Dhaka', 19, 'Bangladesh'
    
for x in mydict.keys():
    print(x) #'Name', 'City', 'Age', 'Country'

for x, y in mydict.items():
    print(x, y) #Print both keys and values
    
#COPY DICTIONARY: 
x = mydict.copy()
print(x)
