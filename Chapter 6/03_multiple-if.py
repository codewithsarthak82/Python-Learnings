age = int(input("Enter Your Age:  "))

# if statement 01 <
if(age%2 == 0):                #{this if is independent}
    print("THE AGE IS EVEN")
# End of statement 01 > 

''' elif and else stataments can never be independent '''
'''last else executes when no conditionals functions work'''

# if statement 02 <
if(age>=18):
    print("VALID")
elif(age<0):
    print("ENTER CORRECT AGE \"ERROR\" FORMAT")
elif(age==0):
    print("INFANT")
else:
    print("NOT VALID")
# End of statement 02 >

print("Thank You have a great day and a lovely year ahead")