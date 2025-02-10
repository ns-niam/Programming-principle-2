#Python: Listss

list = ["PP1", "PP2", "Calculus 1", "Calculus 2"]
print(list) #Result: ['PP1', 'PP2', 'Calculus 1', 'Calculus']

list = ["PP1", "PP2", "Calculus 1", "Calculus 2"]
print(len(list)) #Result: 4

listofnumbers = [1, 2, 3, 4]
print(listofnumbers) #Result: [1, 2, 3, 4]

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "History", "Linear algebra"]
print(list[-1]) #Result: Linear algebra. If we write -2 it will be History. 

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "History", "Linear algebra"]
print(list[2:5]) #Result: ['Calculus 1', 'Calculus 2', 'History'] fifth element nor included. Also it is starts from 0.

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "History", "Linear algebra"]
print(list[:5]) #Result: All elements from 0 to 5(not including). In math can write like this: [0,5)

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "History", "Linear algebra"]
print(list[3:]) #Result: it will start from 3.

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "History", "Linear algebra"]
print(list[-4:-1]) #Result: negative index it means that tarting from at the end of the list. From -4 (including) to -1 (excluding)

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "History", "Linear algebra"]
if "PP1" in list:
    print ("Yes, there is PP1 in the list")
else:
    print ("No, there is no PP1 in the list")
    
#CHANGING THE LIST.    
list = ["PP1", "PP2", "Calculus 1", "Calculus2", "History", "Linear algebra"]
list[0] = "English language"
print(list)

list = ["PP1", "PP2", "Calculus 1", "Calculus2", "History", "Linear algebra"]
list[0:5] = ["English", "ICT", "Kazakh language", "OOP"] #Changing first four element in the list. Тізімдегі алғашқы төрт элементті өзгерту
print(list)

list = ["PP1", "PP2", "Calculus 1", "Calculus2", "History", "Linear algebra"]
list.insert(2, "English language") #With this operation we can insert element to the list. 
print(list) #Result: ['PP1', 'PP2', 'English language', 'Calculus 1', 'Calculus 2', 'History', 'Linear algebra]

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra"]
list.append("English language") #With this operation we can add element to the list.
print(list) #Result: ['PP1', 'PP2', 'Calculus 1', 'Calculus 2', 'Linear algebra', 'English language']

list = ["PP1", "PP2", "Calculus 1"]
secondlist = ["Calculus 2", "Linear algebra", "English language"]
list.extend(secondlist)
print(list) #Result: in this operation we add two list. 

list = ["PP1", "PP2", "Calculus 1"]
list.remove("Calculus 1")
print(list) #Result: in this operation we removed Calculus 1 element from list.

#Removing element using the index.
list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra"]
list.pop(2)
print(list) #Result: in this operation we removed Calculus 1 element from list using index.

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra"]
list.pop()
print(list) #Result: if we use only pop() without index, it wil be removed the last element in the list

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra"]
list.clear()
print(list) #Using clear() we removed all elements from the list.


#Loop lists:
list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "History"]
for x in list:
    print (x) #Result: we printed all elements using for loop
    
list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "History"]
newlist = []
for x in list: 
    if "a" in x: 
        newlist.append(x)
print(newlist) #Result: if there are letter "a" in elements of list, then these elements will be inserted to newlist.

list = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "History"]
list.sort() #With this operation we can sort the elements of list with letter.
print(list) #Result: ['Calculus 1', 'Calculus 2', 'History', 'Linear algebra', 'PP1', 'PP2'] Why? Because "C" is the first in english alphabet than others.

list = [100, 20, 30, 230, 570, 111, 500, 777, 303, 222]
list.sort() #With this operation we can sort the elements of list.
print(list) #Result: [20, 30, 100, 111, 222, 230, 303, 500, 570, 777]

#COPY LISTS: 

list = ["English", "China", "Japan", "Arabic", "Brazil", "Argentina", "Spanish", "Braziles"]
mylist = list.copy()
print (mylist) #Result: we copied the list.

list1 = ["English", "China", "Japan", "Arabic", "Brazil", "Argentina", "Spanish", "Braziles"]
list2 = [1,2,3,4,5,6,7,8] 
list3 = list1 + list2 #We added the list 1 with list 2. 
print(list3)

list = ["English", "China", "Japan", "Arabic", "Brazil"]
list.reverse()
print(list)

list = ["English", "China", "Japan", "Arabic"]
list.pop(3)
print(list)

list = ["English", "China", "Japan", "Arabic", "Brazil", "Brazil"] 
x = list.count("Brazil") 
print(x)

list = ["English", "China", "Japan", "Arabic"]
x = list.index("English")
print(x)
