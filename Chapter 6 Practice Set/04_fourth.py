#Write a program to find whether a given username contains less than 
# 10 characters or not.

name = input("Enter the username here:   ")
a = name.__len__()

if(a<=10):
    print("YES 10 Characters")
    
else:
    print("NO 10 Characters")

