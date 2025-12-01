''' return - function tu ek value leke jaa jo bhi variable 
    mange uske pakda dena '''

value1 = int(input("Enter The Value 1:   "))
value2 = int(input("Enter The Value 2:   "))

name = str(input("Enter Your Name:  "))

def avg(name,ending="Thank You"): # default ending value 
    average = (value1+value2)/2
    print(average)
    print(ending)

avg(name,) # if there will be no ending then a ending="Thank You"
          # will be used as a default ending value

# THIS IS DEFAULT VALUES !


