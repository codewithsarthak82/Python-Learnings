# arguments are used in functions - simply they print the desired
# call when neded 
''' can be taken as input from function or can be pre defined '''

name1  = str(input("Enter Your Name 1:  "))
name2  = str(input("Enter Your Name 2:  "))
name3  = str(input("Enter Your Name 3:  "))
name4  = str(input("Enter Your Name 4:  "))

def gd(name,ending): #name and endings are arguments
    print(f"Good Day, {name}\n{ending}") # using f string

gd(name1 ,"Thank You !")
gd(name2 ,"Thank You !")
gd(name3 ,"Thank You !")
gd(name4 ,"Thank You !")