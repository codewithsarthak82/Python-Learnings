# Loops in python - when repeated data needs to be taken from machine then
# we cannot do it manually we can simply use loops .
'''Some of them are - for and while loops'''

print(1)
print(2)
print(3)

'''now to perform this same task we can take help of loops in coding'''
# using for loop - 
for i in range(1,4): 
#this perform tasks from (n1,n2-1)hence if n=4 then prints 1,2,3 as output


    print(i)
for l in range(0,20000,50):
    print(l)
'''we can also use step sizing here as strings as indexing'''


for l in range(4):
    print(l) 
    #this is very similar to printing from(0,4)


# FOR LOOPS FOR TUPLES -
l = (1,2,3,4,45,67,89,90)
for i in l:
    print(i)


# FOR LOOPS FOR LISTS -
l = ["Sarthak","Ruchika","Manan","Palak"]
for i in l:
    print(i)


# FOR LOOP FOR STRINGS -
name = "Sarthak"
for  i in name:
    print(i)   


# these loops follows "ITERATION" in their functions >


