import random
from sys import argv

script, usr = argv
opt=["rock","paper","scissor"]
#usr=input("Enter the option r / p / s ")
sy=random.randrange(0,3)

if(usr==opt[sy]):
    print("You won !!!!!!!!!!!!!!!")
else:
    print("Bad luck....Try again :(")

