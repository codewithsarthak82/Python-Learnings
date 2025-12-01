# a function is used to give some peice of a logic a sepearte 
# definition in a program 
# we can reduce reliability on a long logic if a task is need to be repeated a number of times

a = int(input("Enter the number of your choice:   "))
b = int(input("Enter the number of your choice:   "))
c = int(input("Enter the number of your choice:   "))

avg = (a+b+c)/3
print(avg)

"""find average of 3 different numbers , but repeatedly 5000 times"""

# FUNCTION DEFINITION
def average(): 
    a = int(input("Enter the number:   "))
    b = int(input("Enter the number:   "))
    c = int(input("Enter the number:   "))
    avg = (a+b+c)/3
    print(avg)

# FUNCTION CALL -
average() 

'''if we noe have to replicat the task we can call a function
   any number of times'''

average()   
average()
average()
average()
average()   

