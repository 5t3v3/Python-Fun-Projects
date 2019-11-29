# Frquency of characters in a string
# Just 4 fun
def char_range(char1 ,char2):
    for char in range (ord(char1),ord(char2)+1):
        yield (char)



inn=input("Enter the string : ")
lenn=len(inn)
print("Length of the string is ",lenn)
# NO idea about this part
for i in range(lenn):
    print(i)
    for j in char_range('a','z'):
       # print(chr(j))
       # print(inn[i])
        if inn[i]==chr(j):
            print("Status =1")
'''
print("Frequency of A is ",A)
print("Frequency of B is ",B)
print("Frequency of C is ",C)
print("Frequency of D is ",D)
print("Frequency of E is ",E)
print("Frequency of F is ",F)
print("Frequency of G is ",G)
print("Frequency of H is ",H)
print("Frequency of I is ",I)
print("Frequency of J is ",J)
print("Frequency of K is ",K)
print("Frequency of L is ",L)
print("Frequency of M is ",M)
print("Frequency of N is ",N)
print("Frequency of O is ",O)
print("Frequency of P is ",P)
print("Frequency of Q is ",Q)
print("Frequency of R is ",R)
print("Frequency of S is ",S)
print("Frequency of T is ",T)
print("Frequency of U is ",U)
print("Frequency of V is ",V)
print("Frequency of W is ",W)
print("Frequency of X is ",X)
print("Frequency of Y is ",Y)
print("Frequency of Z is ",Z)


'''