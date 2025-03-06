#Bulit - in functions:
#Last exercise: Write a Python program with builtin function that returns True if all elements of the tuple are true

mytuple1 = (True, False, False, False, True, True, True)
print(all(mytuple1)) #Result = False. Beause in the tuple have "false" logical operators. 

mytuple2 = (True, True, True, True, True, True, True)
print(all(mytuple2)) #Result = True. Beause in the tuple have "true" logical operators.
