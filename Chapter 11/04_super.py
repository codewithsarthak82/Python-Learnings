# Here we will see the use of Super() method in Python in Inheritance.

class Employee:
    def __init__(self):
        print("I am a constructor from employee class")
    name = "Sarthak"

class Programmer(Employee) :
    def __init__(self):
        super().__init__()
        print("I am a constructor from Programmer class")
    lang = "Python"

class Student(Programmer):
    def _init_(self):  
        super()._init_() 
        print("I am a constructor from Student class")
    college = "IIT Madras"

o = Student()
print(o.lang,o.college)