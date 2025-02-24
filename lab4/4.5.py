# W3SCHOOL: PYTHON ITERATORS
# In this file, Niam will solve problems from W3SCHOOL and analyze theoretical information.

# THEORETICAL INFORMATION:
# Iterators are one of Python's core tools that allow iterating through a dataset (lists, tuples, strings, etc.)
# by moving from one element to another.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)  # The iter function here assigns each element to a variable.

print(next(myit))  # Next function outputs each element one by one.
print(next(myit))
print(next(myit))

myword = "Programming"
myitword = iter(myword)
print(next(myitword))  # Using next to output each element one by one. Here, the elements are letters.
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))

myset = ["BMW", "Mercedes", "Honda"]
myitset = iter(myset)
print(next(myitset))
print(next(myitset))
print(next(myitset))

mytuple1 = ("BMW", "Mercedes", "Honda")
for x in mytuple1:
    print(x)
    
    
class MyNumbers:  # Created a class named MyNumbers.
  def __iter__(self):  # Self refers to a specific instance of the class.
    self.a = 1  # Inside the method, self.a = 1 assigns the initial value of 1 to the variable 'a'.
    return self

  def __next__(self):  # Next is used to move to the next iterator.
    x = self.a  # Each time next() is called, the value of self.a is assigned to variable x.
    self.a += 1  # Then, self.a += 1 increases the value by one.
    return x

myclass = MyNumbers()  # Created an instance of MyNumbers class named myclass.
myiter = iter(myclass)  # Using iter to iterate through numbers.

print(next(myiter))  # Using next to retrieve each number. Here, we use next five times, so numbers from 1 to 5 will be displayed.
print(next(myiter))  # In reality, this process can continue indefinitely.
print(next(myiter))
print(next(myiter))
print(next(myiter))

# USING STOP ITERATION:
class MyNum:
    def __init__(self):
        self.a = 1

    def __iter__(self):  # Defining the __iter__ method
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

mycode = MyNum()
for num in mycode:  # Direct iteration using a for loop
    print(num)
