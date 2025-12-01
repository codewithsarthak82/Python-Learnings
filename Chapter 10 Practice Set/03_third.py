""" Create a class with a class attribute a; create an object from it and 
set a directly using object.a = 0. Does this change the class attribute?"""

class example:
    a = 50

sarthak = example()
sarthak.a = 0
print(sarthak.a)

# ANSWER - Yes it does not changes the class attribute but it will be  used 
#          as an instance attribute !
