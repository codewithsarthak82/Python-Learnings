#Write a python function to print first n lines of the following pattern:
''' - for n = 3
    ***
    ** 
    *
'''
n = 3
def star(n):
   return "*" * n

print(star(n))
print(star(n-1))
print(star(n-2))
    



