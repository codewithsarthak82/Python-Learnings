# Write a program using functions to find greatest of three numbers

a = int(input("Enter The Number 1:  "))
b = int(input("Enter The Number 2:  "))
c = int(input("Enter The Number 3:  "))

def gr(a,b,c):

    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
print("The greatest of the 3 numbers is:",gr(a,b,c))