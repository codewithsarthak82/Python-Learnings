# DIFFERENT FUNCTION IN LISTS ARE AS FOLLOWS - 

kids = ["Sarthak","Ruchika","Aaryan", 4 , 56.980 ,"Aayush"]


# 1.extend adds up more data in the particular data set !
numbers01 = [67,7,1,69,0]
numbers02 = [9,89,7,66,4]
numbers01.extend(numbers02)
print(numbers01)

# 2.append matlab at the end mai laga dena !
kids.append("Ruchika")
print(kids)

# 3.sort will arrange numbers in increasing order !
numbers01 = [67,7,1,69,0]
numbers01.sort()
print(numbers01)

# 4.reverse will ulta the order of the elemets or data in the list !
numbers01.reverse()
print(numbers01)

# 5.used to insert in the middle using (index, to be added) !
numbers01.insert(4 , 300)
print(numbers01)

# 6.pop is used to remove/pop any data or element .
kids.pop(3)
print(kids)

# 7.remove will remove  the particular data entered()
numbers01 = [67,7,1,69,0]
numbers01.remove(67)
print(numbers01)

# 8.index will be used to find out the index from a dataset !
numbers03 = [67,98,99,20,70]
print(numbers03.index(99))

# 9.copy method copies the whole list 
list = ["Aarti" , "Pooja" , "Saksham" , "Palak"]
print(list)

#NEWLIST VARIABLE

newlist = list.copy()
print(newlist)









