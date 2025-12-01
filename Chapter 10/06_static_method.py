# Here we will see the use of static method in this code .
"""Simple idea is we can use functions in a class without giving an object attribute by using Static
   method, hence no use of self parameter"""

class employee:
    name = "Sarthak"
    lang = "Pyhton"
    salary = 4000000

    # here we have to use self as we have an object attrbute over here simple
    def getinfo(self): 
        print(f"My name is {self.name}, and my salary is {self.salary} and my language is {self.lang}")
    
    @staticmethod
    # here we have to use static as we do not have any object attribute over here simple 
    def greetings():
        print("Good Morning") 

sarthak = employee()
employee.getinfo(sarthak)
employee.greetings(sarthak)