# Here we will see the use of init methods(DUNDERS) in this code .

class employee:
    name = "Sarthak"
    lang = "Pyhton"
    salary = 4000000

    """Either we can use init like this withou any object attributes"""
    # def _init_(self): 
    #     print("I am creating an Object")

    """Or we can use init like this using any object attributes"""
    def __init__(self,name,salary,lang): # these are self called attributes 
        self.name = name
        self.salary = salary
        self.lang = lang
        print("I am creating an object automatically")

sarthak = employee("Sarthak",4500000,"Pyhton")
print(sarthak.name,sarthak.salary,sarthak.lang)