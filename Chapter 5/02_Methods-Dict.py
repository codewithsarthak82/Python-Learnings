#THE FOLLOWING ARE THE DIFFERENT METHODS IN DICTIONARIES - 

marks = {
        "Sarthak": 90,  
        "Ruchika": 99,
        "Harry": 87,
        }

# 1.Items - batata hai about (keys,values) in a dictionary .
X = marks.items()
print(X)

# 2.Keys - Tells about keys from a dictionary .
Y = marks.keys()
print(Y)

# 3.Values - Tells about values from a dictionary .
Z = marks.values()
print(Z)

# 4.Updates - New / additional data ko change/add krne ke liye .
L = marks.update({"Sarthak":89})
M = marks.update({"Ruchika":100 , "Palak":90})
print(marks)

# 5.Get - Give the value assign to any key in dictionary .
print(marks.get("Sarthak"))
print(marks["Sarthak"])

""" {both have same kaam lekin difference ayega kab} """

# now difference when a key is not present in the dictionary #
'''print(marks.get("SarthakDhiman")) #gonna give none  .
 print(marks["SarthaKDhiman"])     #gonna give error .'''


# 6.Clear - This cleans out all keys and values in a dictionary .
'''marks.clear()
 print(marks)''' 

# 7.Copy - This copies all the keys and values from a dictionary .
newmarks = marks.copy()
print("The newmarks are:  ",newmarks)

# 8. FromKeys - This creates a new dictionary with keys from new 
#               sequence created and values set to new values .

keys = ['SarthakDhiman' ,'RuchikaDhiman' , 'HarryKhan']
newmarks = marks.fromkeys(keys,80)
print(newmarks)

# 9. Pop - This pop's out and dlt all the values and keys from a dict .
marks = {
        "Sarthak": 90,  
        "Ruchika": 99,
        "Harry": 87,
        }

marks.pop('Sarthak')
print(marks)

# 10. 