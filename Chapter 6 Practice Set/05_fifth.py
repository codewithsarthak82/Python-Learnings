# Write a program which finds out whether a given name is present in a list 
# or not

name = str(input("Enter Your Name Here:  "))
list = ["Sarthak","Ruchika","Palak","Aaryan","Ayush"]

#here using the in function -
if(name in list): 
    print("Your name is in the list, you are eligible for the contest")

else:
    print("Your name is not in the list, you are not eligible for the contest")