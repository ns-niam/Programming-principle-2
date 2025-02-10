#First exercise: a recipe you are reading states how many grams you need for the ingredient. 
#Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

def my_task1(grams):
    ounces = 28.3495231 * grams #We opened the variable ounces and we converted grams to ounces using formula; 
    print(ounces)

exercise1 = int(input()) #Grams
my_task1(exercise1) #my_task1 it is name of the function
