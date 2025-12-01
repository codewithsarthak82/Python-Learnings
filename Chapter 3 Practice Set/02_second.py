#Write a program to fill in a letter template given below with name 
# and date ?
# letter = ''' Dear <|Name|>, 
#              You are selected! 
#              <|Date|>'''

a = input("Enter your name:  ")

b = input("Enter date:  ")

print(f"Dear {a}\nYou are selected for IIT Madras Internship\n{b}\n....")

# This is method 2(little advanced but time saving) .
letter = '''Dear,<|name|>\nYou are selected!\n<|Date|>'''
print(letter.replace("<|name|>" ,a).replace("<|Date|>" ,b))