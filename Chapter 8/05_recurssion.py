# recursion - repetiiton of functions in a mandatory go .

"""recurssion hold on those values jinki values ka logic recursive hai jaise
   factorials,series,binomials.. etc"""
# we always have a base contd. in a function and recurssions.

def fact(n):
    """This is called as teh base condition """
    if(n==1 or n==0): 
        return 1
    return n*fact(n-1)
# how this acts as recursive as here it will again call fact(n-1) then(n-2)
# this will end as when it will have 1 and returns the value 1 and recurssion 
# breaks in a simple way to be said.

n = int(input("Enter the value:  "))
print("The factorial of this number is:  ", fact(n))




    