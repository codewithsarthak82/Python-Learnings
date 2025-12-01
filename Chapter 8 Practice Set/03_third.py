# How do you prevent a python print() function to print a 
# new line at the end

a = str(input("Enter Your Name:   "))
b = str(input("Enter Your Name:   "))
c = str(input("Enter Your Name:   "))
d = str(input("Enter Your Name:   "))

print(a)
print(b)
print(c,end=" ")
print(d,end=" ")

# these end 2 wale print domt show in next line to each other they
# comtinue in a single line !