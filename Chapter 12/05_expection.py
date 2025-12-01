"""Exception handling is used in programming for passing the errors in the
   programs while executing different data types"""

try:
    n = int(input("Enter your number:  "))  
    print(n)
except Exception as e: # this piece of code executes when we dont want our program
                       # to crash hence we use this and pass the errors
    print(e)
print("Thank You for executing the code!")

