# Write a program to find out whether a given post is talking about 
# “Harry” or not.

name = str(input("Enter your name:  "))
post = str(input("Enter your post:  "))

if(name in post):
    print("There is your name in the post uploaded")

else:
    print("There is not your name in the post uploaded")