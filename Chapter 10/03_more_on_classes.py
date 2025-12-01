"""In those previous examples we were limited tp the name of the users as harry
   or any other name, but we can print their unique names in the object
   creation/instantiation !"""

class Employee:
    language = "Pyhton" #this is a class attribute
    salary = 4000000

harry = Employee()
harry.name = "Harry" #this is an object attribute
print(harry.name ,harry.salary,harry.language)

rohan = Employee()
rohan.name = "Rohan" #this is an object attribute
print(rohan.name,rohan.salary, rohan.language)

sarthak = Employee()
sarthak.name = "Sarthak" #this is an object attribute
print(sarthak.name,sarthak.salary, sarthak.language)

shivank = Employee()
shivank.name = "Shivank" #this is an object attribute
print(shivank.name,shivank.language , shivank.salary)

# This helps us to create a single class as a proper template and give it to an
# object and they can add various attributes refered to it .
"""Moreover a class should have common attributes which can be accessed multiple
   times (important hai boss)"""