#In this lecture we will look out on creating a class !

"""This is a class with a pre-defined class without an input from the user"""
class Scores:
    name = "Sarthak"
    age = 19
    language = "Python"
    College = "IIT Madras"

sarthak= Scores() # here sarthak is an OBJECT
print(sarthak.name , sarthak.age , sarthak.language , sarthak.College)


"""This is a class with a defined class with an input from the user"""
class Scores:
    name = str(input("Enter your name:  "))
    age = int(input("Enter your age:  "))
    language = str(input("Enter your language:  "))
    College = str(input("Enter your college:  "))

sarthak= Scores() # here sarthak is an OBJECT
print(sarthak.name , sarthak.age , sarthak.language , sarthak.College)


