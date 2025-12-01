'''Write a python program using function to convert Celsius to 
   Fahrenheit'''
#  c/5 = (f-32)/9 this is teh formula hence for conversion

c = int(input("Enter the temprature in celcius:   "))

def temp():
    a = ( ((c*9)/5) + (32) )
    return a

print(f"The temprature in fahrenheit is: {temp()}°F")
    