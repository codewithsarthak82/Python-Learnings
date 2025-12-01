# THE FOLOOWING ARE THE FUNCTIONS OF STRING - 

name = "Sarthakandmumma"

#number 1 : length of the string
A = len(name) 
print(A)

#number 2 : from which letters name ends/starts with ? Boolean Statement 
print(name.endswith("mma"))
print(name.endswith("klm"))

print(name.startswith("Sar"))
print(name.startswith("sar")) #case sensitive hai !
print(name.startswith("lam"))

#number 3 : Capitalize first letter from any word
name2 = "sarthak and Ruchika"
print(name2.capitalize())