""" this is the method to write any string in a file """

# This is very simple - 
 # 1. open a file .
  # 2. operate write function(str jo write karna hai)
   # 3. close the file and fucntion .

st = "Hey I am a good boy and I like leg days"

file = open("newfile.txt","w")
file.write(st)
file.close()

''' hence when thisf file runs this leaves a newfile.txt named file '''
#   in our folder named Cs VScode-Python Part 2 
