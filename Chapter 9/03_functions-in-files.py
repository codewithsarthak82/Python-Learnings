# """These are some functions in which we can use some different operation on file"""

# # this is print lines print all lines from any file 
file = open("c:VScode-Python/Chapter 9/file.txt")
lines = file.readlines()
print(lines)
file.close()

# # this is print line print iteartion of lines(ie. one by one reading lines)
file = open("c:VScode-Python/Chapter 9/file.txt")

line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)

line3 = file.readline()
print(line3)

line4 = file.readline()
print(line4)

line5 = file.readline()
print(line5)

line6 = file.readline()
print(line6)

line7 = file.readline()
print(line7)

line8 = file.readline()
print(line8)

line9 = file.readline()
print(line9)

line10 = file.readline()
print(line10)

line11 = file.readline()
print(line11 == "") # this tells us that there is no line 11 in this file
                    # this is a boolean return{true/false}

""" printing lines using while loop """
line = file.readline()
while(lines != ""):
    print(line)
    line = file.readline()


file.close()


