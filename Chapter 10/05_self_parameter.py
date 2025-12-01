# Here we will see the use of self parameter in this code .

class employee:
    name = "Sarthak"
    lang = "Pyhton"
    salary = 4000000

    # here we used self parameter to define a function inside a class as 
    # if not done it will cast an error simply - 

    def getinfo(self): 
        print(f"My name is {self.name}, and my salary is {self.salary} and my language is {self.lang}")
    def greetings(self):
        print("Good Morning")    

sarthak = employee()
employee.getinfo(sarthak)
employee.greetings(sarthak)

# this is same way of calling functions in a class and object or OOP's
sarthak.getinfo() 
sarthak.greetings()

# print(sarthak.getinfo,sarthak.greetings)