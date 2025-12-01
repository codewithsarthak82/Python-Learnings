"""Here we will understand the use of WALRUS OPERATOR in python and their
   different functionality"""
# Using Walrus Opeartor -

if(n:=len([1,2,3,4,5]))>3:
    print(f"List is too long({n} elements, expected<=3)")
