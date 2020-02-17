#####################################################
#####      TERMINAL BASED GAME !!!!!!!!!!!!!!!  #####

import random
from sys import argv

#Enter the correct input or else ready to fail 
script, usr = argv 
opt=["rock","paper","scissor"]
sy=random.randrange(0,3)
y=opt[sy]
if(usr==opt[sy]):
    print("Drawwwwwwwww   :|  ")



elif(usr=="rock" and y=="paper"):
    print("System wins !!!!")
elif(y=="rock" and usr=="paper"):
    print("User wins !!!")



elif(y=="rock" and usr=="scissor"):
    print("System wins !!!")
elif(y=="scissor" and usr=="rock"):
    print("User wins !!!!")


    

elif(y=="paper" and usr=="scissor"):
    print("User wins !!!")
elif(usr=="paper" and y=="scissor"):
    print("System wins !!!!")



else:
    print(y)

    print("Bad luck....Try again :(")

print(y)
