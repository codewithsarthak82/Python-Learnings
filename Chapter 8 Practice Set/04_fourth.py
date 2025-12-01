# Write a recursive function to calculate the sum of 
# first n natural numbers

def sum(n):
    if(n==0 or n<0): # this is known as base condition.
        return 0
    return sum(n-1) + n

n = int(input("Enter the number:   "))
print(f"The sum of first n natural numbers are: {sum(n)}")
    
    
 