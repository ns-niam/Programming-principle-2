#Python: Sets!
#Now i will write some informations that i understand about this topic: 

#1) Sets are unordered collections of unique elements.
#2) Sets are written with curly brackets.
#3) A set is a collection which is unordered, unchangeable*, and unindexed.
#4) Duplicates are not allowed. If there two same items in the set, and if we print the set, then we can see set without same items. 

myset = {"BMW", "Mercedes", "Rolls Royce", "Sonata", "Changan"}
print(myset)

#EXAMPLES FOR DUPLICATE:
myset = {"BMW", "Mercedes", "Rolls Royce", "Sonata", "Changan", "BMW"}
print(myset) #Нәтиже: Бұл жерде BMW элементі екі рет жазылып тұр. Ал set ережесі бойынша дубликат элементтер қамтылмайды. Сондықтан нәтижеде бір BMW жойылады. 

myset = {True, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(myset) #In this operation 1 and True are the same item. Thats why in the result we can see only True. 

myset = {True, 1, 2, 3, 4, 5, 6, 7, False, 0}
print(myset) #In this operation 0 and False are the same item. Thats why in the result we can see only False. 

#LENGTH OF THE SET: 
myset = {"PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "History of Kazakhstan", "ICT"}
print(len(myset)) #In this operation we can see length of the set. It means that how many elements have in the set.

#TYPE OF THE SET: 
myset = {"PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "History of Kazakhstan", "ICT"}
print(type(myset)) #In this operation we can see type of the set. Result is: <class 'set'>

#PRINTING THE SET WITH FOR LOOP: 
myset = {"PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "History of Kazakh", "ICT"}
for x in myset: 
    print(x) #In this operation we can print the set with for loop.
    
#Some information about the set: 
# 1) We can add and remove elements from the set, but we cannot replace an existing element with another one.

#ADD THE SET ITEMS: 
myset = {"PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "History of Kazakhstan", "ICT"}
myset.add("English language")
print(myset) #In this operation we can add elements to the set.

#ADDING SETS WITH EACHOTHER: 
myset = {"PP1", "PP2", "Calculus 1", "Calculus 2"}
yourset = {"Linear algebra", "History of Kazakhstan", "ICT"}
myset.update(yourset) 
print(myset)

#ADDING SETS WITH LIST: 
mylist = ["PP1", "PP2", "Calculus 1"]
yourset = {"Linear algebra", "History of Kazakh", "ICT"}
yourset.update(mylist)
print(yourset)

#REMOVING ELEMENTS FROM THE SET WITH REMOVE operation:
myset = {"PP1", "PP2", "Calculus 1"}
myset.remove("PP1")
print(myset)

#REMOVING ELEMENTS FROM THE SET WITH DISCARD operation:
myset = {"PP1", "PP2", "Calculus 1"}
myset.discard("PP1")
print(myset)

#REMOVING ELEMENTS FROM THE SET WITH POP operation: You can also use the pop() method to remove an item,
#but this method will remove a random item, so you cannot be sure what item that gets removed.
myset = {"PP1", "PP2", "Calculus 1"}
myset.pop()
print(myset)

myset = {"PP1", "PP2", "Calculus 1"}
x = myset.pop()
print(x) #Removed element
print(myset) #Set after removing

#REMOVING ELEMENTS FROM THE SET WITH CLEAR operation:
myset = {"PP1", "PP2", "Calculus 1"}
myset.clear()
print(myset) #Result: set()

#LOOP SETS: 
myset = {"PP1", "PP2", "Calculus 1"}
for x in myset: 
    print (x) #Sets are unordered, so when you loop through the items, the order will be totally random.
    
#JOIN SETS - БІРІКТІРУ: 
myset = {"PP1", "PP2", "Calculus 1"}
yourset = {"Linear algebra", "English language"}
result = myset.union(yourset)
print(result) #Sets are unordered, so when you join the items, the order will be totally random.
result1 = myset | yourset #We can use | this operator for joining the sets. Result is same with union
print(result1)

myset = {"PP1", "PP2", "Calculus 1"}
yourset = {"Linear algebra", "English language"}
hisset = {"History", "ICT"}
result2 = myset.union(yourset, hisset)
print(result2)
result3 = myset | hisset | yourset
print(result3)

myset = {"PP1", "PP2", "Calculus"}
yourset = {"Linear algebra", "English language"}
myset.update(yourset) #Joining sets using "UPDATE" operator
print(myset)

#JOINING SETS USING "INTERSECTION" operator: 
myset = {"PP1", "PP2", "Calculus"}
yourset = {"Calculus", "English language"}
result4 = myset.intersection(yourset)
print(result4) #If we use "INTERSECTION" operator, we can see elements that have in both sets. Result: {'Calculus'}
result5 = myset & yourset 
print(result5) #We can use & this operator for joining the sets. Result is same with intersection
myset.intersection_update(yourset)
print(myset) #The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

#JOINING SETS USING "difference()" operator: 
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
myset = {"PP1", "PP2", "Calculus"}
yourset = {"Calculus", "English language"}
result6 = myset.difference(yourset)
print(result6) #Result: {'PP1', 'PP2'}
result7 = myset - yourset #We can use the - operator instead of the difference() method, and you will get the same result.
print(result7)

myset = {"PP1", "PP2", "Calculus"}
yourset = {"Calculus", "English language"}
result8 = myset.symmetric_difference(yourset)
print(result8) #The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#Result: {'English language', 'PP1', 'PP2'}
result9 = myset ^ yourset#We can use the - operator instead of the symmetric difference() method, and you
print(result9)
