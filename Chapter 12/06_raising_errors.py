"""For specific type of arithmetic operations of from the inout from user
   we can throw different type of errors"""

a1 = int(input("Enter your first number:"))
a2 = int(input("Enter your second number:"))

if(a2 == 0):
    raise ZeroDivisionError("Zero is not accepted as denominator, Sorry for the inconvinience")
else:
    print(f"The result for our division is: {a1/a2}")