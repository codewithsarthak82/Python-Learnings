''' Write a program to find out whether a student has passed or 
failed if it requires a total of 40% and at least 33% in each 
subject to pass. Assume 3 subjects and take marks as an input from 
the user.'''

# here we gonna use the if and elif and else statements ladders 

name = input("Enter Your Name Here:   ")
print(name)

marks01 = int(input("Enter The Marks ; Subject 1:  "))
marks02 = int(input("Enter The Marks ; Subject 2:  "))
marks03 = int(input("Enter The Marks ; Subject 3:  "))

tp = (((marks01+marks02+marks03)/300)*100) #this is total percentage 

avg = ((marks01+marks02+marks03)/3)

if(tp>40 and avg>33): # and operator here is important !
    print(f"\"Congratulations\"you have passed the examination",name)
    
else:
    print("Sorry you haven't passed the examination")
    print("Better Luck Next Time")
