# here we will see the use of class methods in py.

"""now while executing thsi code we will obtain the value of name as Shubham
   whereas we want Sarthak as the value"""
class Employee:
    name = 'sarthak'
    def show(self):
        print(f"the name is: {self.name}") # here Shubham is taken

b = Employee()
b.name = 'Shubham'
Employee.show(b)

###########################################################################

"""Now we will use the class method to pass the class value in the property"""
class Employee:
    name = 'sarthak'
    @classmethod
    def show(cls):
        print(f"the name is: {cls.name}") #now Sarthak will be taken

b = Employee()
b.name = 'Shubham'
b.show()
