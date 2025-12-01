# In this lecture we'll look after merging different dictionaries-
""" Simple and crisp outputs and simple to use and can be used in different 
   occasions and on diffent programming acts """

m = int(input("Enter your maths marks:  "))
c = int(input("Enter your chemistry marks:  "))
p = int(input("Enter your physics marks:  "))

dict1 = {"Maths":m , "Chemistry":c , "Physics": p}
dict2 = {"Average":(m+c+p)/3 , "Total":m+c+p}

merging_dicts = dict1 | dict2
print(merging_dicts)
