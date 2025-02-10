
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

# New class. We inherit from the Person class
class Student(Person):
    def __init__(self, name, age, student_id):
        # Using super() to call the __init__ method of the parent class
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        # Call the introduce method of the Person class
        super().introduce()
        # Add additional student-specific information
        print(f"My student ID is: {self.student_id}")

# Creating an object of the Student class
student1 = Student("Niam", 19, "S12345")
student1.introduce()
