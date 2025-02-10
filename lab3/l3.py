# Python: Classes and Objects

# What are classes and objects?
# A class is a template or blueprint for creating objects of a certain type.

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age  

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

person1 = Person("Niam", 20)
person1.introduce()  # Result: My name is Niam, and I am 20 years old.

class KBTU: 
    def __init__(self, lessons, lecturer):
        self.lessons = lessons  # There are lessons in KBTU
        self.lecturer = lecturer  # There are teachers of lessons 
        
    def university(self):
        print(f"Lessons: {self.lessons}, Lecturer: {self.lecturer}")
        
information = KBTU(["PP1", "PP2", "OOP"], "Tamiris Abildayeva")
information.university()

# Explanation of the code:
# First, I created a new class to store information about KBTU. The name of the class is KBTU.
# Second, through the constructor (__init__ method), the necessary information is accepted when an object is created and stored in object attributes.

class Name: 
    def __init__(self, name, surname):
        self.firstname = name
        self.lastname = surname
    
    def myfunction(self):
        print(self.firstname + " " + self.lastname)
        
x = Name("Niam", " MD sha")
y = Name("Tamiris", "Abildayeva")
z = Name("Islam", "Menlidai")
x.myfunction()
y.myfunction()
z.myfunction()
