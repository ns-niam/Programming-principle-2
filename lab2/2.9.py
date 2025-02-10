#Python: For loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#FOR LOOPS IN LIST: 
mylist = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language", "ICT"]
for x in mylist: #Әр элемент х айнымалысына барып сақталады және біз х-ті шығардық. 
    print(x)

mylist = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language", "ICT"]
for x in mylist: 
    if x == "Calculus 2": #Әр айнымалы х-ке барып сақталады және біз х-ті шығардық. Шығармас бұрын егер х айнымалы Calculus 2-ге тең болған жағдайда бағдарламаны тоқтат деп шарт енгіздік. 
        break
    print(x)
    
mylist = ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language", "ICT"]
for x in mylist: 
    if x == "Calculus 2": #X айнымалы Calculus 2-ге тең болған кезде, жалғастыр. Яғни, бағдарлама бұл жерде Calculus 2-ні тастап кетеді.
        continue
    print(x)

#FOR LOOP IN STRING: 
myword = "Mercedes"
for i in myword:
    print (i)
    
myword = "Mercedes"
for x in myword:
    if x == "e":
        continue
    print(x)
    
#FOR LOOP IN TUPLE: 

    mytuple = ("BMW", "Mercedes", "Rolls Royce")
    for x in mytuple:
        print(x)
        
    mytuple = ("BMW", "Mercedes", "Rolls Royce")
    for x in mytuple:
        if x == "Rolls Royce":
            break
        print(x)
        
#FOR LOOP IN NUMBERS: 
for i in range(100): #It is numbers from 0 to 100 (not included)
    print(i)
    
for i in range (5, 100): #It is numbers from 5 to 100 (not included)
    print(i)
    
for i in range (20, 100, 2): #Numbers from 20 to 100 (not included) with 2 step
    print(i)
    
for i in range (20, 50, -1):
    print(i) #The code will produce no output because the range is invalid.

#for i in range (start, stop, step)

for x in range(6): #Numbers from 0 to 6 (not included)
  print(x)
else:
  print("Finally finished!") #After running the code, the output will be written "Finally finished!"
  
