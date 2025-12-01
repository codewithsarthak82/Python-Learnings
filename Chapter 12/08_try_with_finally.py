"""Here we will see the use of finally with try clause and its interesting
   as this is helpful while defining functions"""

def fnlly():
    try:
        a = int(input("Enter your numeber: "))
        print(a)
        return 

    except Exception as e:
        print(e)
        return

    finally:
        print("I am always executed in case of functions if I am not used then no value after return statements")

fnlly()

# now what if happens when we will remove the finally block and simply uses print
def fnlly2():
    try:
        b = int(input("Enter your number:  "))
        print(b)
        return

    except Exception as f:
        print(f)
        return

    print("This time I will not be printed")