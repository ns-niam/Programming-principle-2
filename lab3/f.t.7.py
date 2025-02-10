#Seventh exercise: given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums) - 1):  #Checking all elements in the list till the end 
        if nums[i] == 3 and nums[i + 1] == 3:  #If two 3 element located side by side are found:
            return True
    return False


print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False
