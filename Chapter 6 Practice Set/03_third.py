''' A spam comment is defined as a text containing following keywords:
   “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
   Write a program to detect these spams '''

#here we taking an input from a user 
I = str(input("Enter your received message here:   "))

#we have entered the data considered as spam messages
spam = ("Make a lot of money","buy now","subscribe this","click this")


#This is crazy syntax as this cretaed a loop in the conditionals
if any(keyword in I for keyword in spam):
    print("SPAM MESSAGE DO NOT REPLY BE ALERT AND AWARE")

else:
    print("NOT A SPAM MESSAGE")

print("Have a lovely day ahead")