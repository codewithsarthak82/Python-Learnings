"""Here we will study how to use nstance attributes in out program and FYI: that
   Instance attributes have a preference over Class Attributes"""

class School:
    salary = 1000000 
    language = "Python" # this is a CLASS attribute .

shivansh = School()
shivansh.name = "Mr.Shivansh Gupta" # this ia an OBJECT attribute .
shivansh.salary = 2000000 # this is an INSTANCE attribute .
shivansh.language = "JavaScript"
print(shivansh.salary,shivansh.language) 


# fist in a code interpretator will look after instance attribute if not found 
# then it will look after class attributes(Simple Algorithms)
    
