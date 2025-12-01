"""What is multilevel inheritance - This is a method in which a class(child)
   takes/inherit the properties of different class(parents) but step by step 
   at different levels .

   When a child has multiple parents it is known as - Multilevel 
   Inheritance"""

class Employee:
    name = "Sarthak"
    age = 19
    company = "Apple.co.in"
    def my(self):
        print(f"My name is: {self.name}, My age is: {self.age}, My company is: {self.company}")

class Programmer(Employee): #Employee is parent of Programmer class
    language = "Python"
    Services = "Data Scientist"
    def my_more(self):
        print(f"I am comfortable with: {self.language} in services like: {self.Services}")

class Student(Programmer):  #Programmer is parent of Student class
    College = "IIT Madras"
    def more_more_my(self):
        print(f"I am a student from: {self.College}")

c = Student()
print(c.name,c.age,c.company,c.language,c.Services,c.College)
Student.my(c)
Student.my_more(c)
Student.more_more_my(c)