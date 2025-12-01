# Write a program to accept marks of 6 students and display them 
# in a sorted manner.

MARKS = []

A = int(input("Enter the marks of student 1:  "))
MARKS.append(A)

B = int(input("Enter the marks of student 2:  "))
MARKS.append(B)

C = int(input("Enter the marks of student 3:  "))
MARKS.append(C)

D = int(input("Enter the marks of student 4:  "))
MARKS.append(D)

E = int(input("Enter the marks of student 5:  "))
MARKS.append(E)

F = int(input("Enter the marks of student 6:  "))
MARKS.append(F)

G = int(input("Enter the marks of student 7:  "))
MARKS.append(G)


MARKS.sort()
print(MARKS) # as lists are muttable hence PRINT IT AGAIN !