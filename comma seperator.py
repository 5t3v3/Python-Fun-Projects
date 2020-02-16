txt=input("Enter the txt file: ")
f=open(str(txt),"r+")
f_data=f.read().split(',')

for i in f_data:
    print(i)
    t=open("syllabus.txt","a")
    t.write(i)
    t.write("\n")
    t.close()