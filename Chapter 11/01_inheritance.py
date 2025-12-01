"""What is inheritance - this is a method in programs in which we can use
   parent class to create a child class and this can be done at different
   levels - Single Inheritance , Multiple Inheritance and Multilevel Inheritance"""

# Example where Employee class is inherited in Programmer class.

class Employee:
    name = "Sarthak"
    age = 19
    company = "Dell Technology Systems"

    def show(self):
        print(f"My name is: {self.name}, My age is: {self.age} and My company is: {self.company}")

# so this is a class which will have all properties from class employee.
class Programmer(Employee):
    salary = 4000000
    college = "Indian Institute Of Technology Madras"

    def show_more(self):
        print(f"My salary is: {self.salary} and My college is: {self.college}")

a = Employee()
b = Programmer()
print(a.name,a.age,a.company)
Employee.show(a)

# hence here we can sayy that name,age and company is not in the programmer
# class but still shows all the properties from employee class
print(b.name,b.age,b.company,b.salary,b.college)

# even defined functions are also been called using inheritance principle
# as we can call function from employee class using programmer class
Programmer.show(b)
Programmer.show_more(b)

"""Employee() class is parent of programmer() class in simple words"""
