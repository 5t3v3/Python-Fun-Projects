# Frquency of characters in a string
# Just 4 fun
def char_range(char1 ,char2):
    for char in range (ord(char1),ord(char2)+1):
        yield (char)
dictt={}
for second in char_range("a","z"):
    dictt[chr(second)]=0
inn=input("Enter the string : ")
lenn=len(inn)
print("Length of the string is ",lenn)

for first in range(lenn):
    for second in char_range("a","z"):
        if inn[first]==chr(second):# chr is the character function like str
            dictt[chr(second)]=dictt[chr(second)]+1
                 

print (dictt)       
