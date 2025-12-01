"""Write a class “Calculator” capable of finding square, cube and square 
   root of a number"""
n = int(input("Enter your number:   "))

class calculator:
    a = n*n
    b = n*n*n
    c = (n)*(1/2)
    
    @staticmethod
    def greet():
            print("hello eveyone welcome to our calculator, enjoy")

    def sqaure(self):
            print(f"The sqaure of your number is {self.a}")

    def cube(self):
            print(f"The cube of your number is {self.b}")

    def sqaure_root(self):
            print(f"The sqaureroot of your number is {self.c}")

sarthak = calculator()
calculator.sqaure(sarthak)
calculator.cube(sarthak)
calculator.sqaure_root(sarthak)



    






    
