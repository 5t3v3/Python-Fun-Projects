################################
#######  ODD or Even  ##########
import random
total=0
total2=0
print("First batting user !!!!!")
try:
    for i in range(0,10):
        usr=int(input("Enter a number between 1 and 6: "))
        sys=random.randrange(1,7)
        print("Sys input is ",sys)
        if(usr!=sys):
            total=total+usr 
        else:
            break

    print("Total scored by user is : ",total)

    print("\n Second batting computer !!!!!!!")

    for i in range(10):
        usr2=int(input("Enter a number between 1 and 6: "))
        sys2=random.randrange(1,7)
        print("Sys input is ",sys2)
        if(usr2!=sys2):
            total2=total2+sys2
            if(total2>total):
                print("System wins !!!!!!!!!")
                break
        else:
            break

    print("Total Scored by sys",total2)

    if(total>total2):
        print("You won !!!!!!!!!!")
except:
    print("Enter correct input!!!!!!!!! ")
    break
