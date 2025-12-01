""" Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’. """

f = open("c:VS-Code_Python_Immature/VScode-Python/Chapter 9 Practice Set/poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word Twinkle is present in the poem")
else:
    print("The word Twinkle is not present in the poem")