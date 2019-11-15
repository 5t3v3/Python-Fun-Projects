#Love calculator

import random

x=input("Enter your name : ")
s=input("Enter your partner's name : ")

l1=len(x)+random.randrange(1,10)
l2=len(s)+random.randrange(1,10)

print("l1 is",l1)
print("l2 is",l2)
if l1>l2:
    z=l1-l2
    print("Difference of lenths is ",z)
else:
    z=l2-l1
    print("Difference of lenths is ",z)

y=(random.randrange(0,20))

print("Random number generated is ",y,"\n")
if z>y:
    i=(y/z)*100
elif y>z:
    i=(z/y)*100
elif y==z:
    i=100

print("Love percentage is ",i,"%")