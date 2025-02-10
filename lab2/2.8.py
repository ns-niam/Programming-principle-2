#Python: While loops! With the while loop we can execute a set of statements as long as a condition is true
#Python has two primitive loop commands: While loops and For loops.

x = 1
while x < 10:
    #print(x) It is infinitive loop. Because i is always less than 10
    
i = 2
while i < 8:
  print(i)
  i += 1 
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
