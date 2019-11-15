import random

str=""" This is a simple program to test your luck :P

The logic of this program is that it generates a random number between 1 and 100.

The user is allowed to test his luck by entering a number between 1 and 100.

If both the numbers are same you are so lucky today......


"""
print(str)
x=input("Enter your number : ")
y=(random.randrange(0,101))
print("Random number generated is ",y,"\n")
if (x==y):
    print("You are so lucky today\n")
else:
    print("Better luck next time\n")