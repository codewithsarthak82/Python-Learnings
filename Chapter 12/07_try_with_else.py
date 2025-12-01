"""Using try with else clause is a important -"""
"""The else statemt is executed if code inside try block is successfull
   if try block fails then else is not executed"""
try:
    a = int(input("Enter your number:  "))
    print(a)
except Exception as e:
    print(e)
else:
    print("I am executed and hence inside ELSE clause")