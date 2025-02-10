#Tenth exercise: write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique_elements(list): #We opened a new function. Name of the function is - unique_elements.
    new_list = [] #List of unique elements.
    for element in list: #Checking every element in the list.
        if element not in new_list: #If element is unique, add it
            new_list.append(element) #Adding element to list
    print(new_list)
    
exercise10 = [1,1,2,7,4,5,6,7,8,9,10]
unique_elements(exercise10)
