from tkinter import*

def btnclick(num):
    global operator
    operator =operator +str(num)
    txt_input.set(operator)

def btnclear():
    global operator
    operator=""
    txt_input.set("")


def btnequal():
    global operator
    sums=str(eval(operator))
    txt_input.set(sums)
    operator=""

calc=Tk()
calc.tite=("Calculator")
txt_input=StringVar()
operator=""



txtbox=Entry(calc,font=("arial",20,'bold'),textvariable=txt_input,bg="light blue",bd=30,insertwidth=4,justify='right').grid(columnspan=4)

#=====================================================================================================================================================================================================================
#First row 

btn1=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="1",command=lambda:btnclick(1)).grid(row=1,column=0)

btn2=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="2",command=lambda:btnclick(2)).grid(row=1,column=1)

btn3=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="3",command=lambda:btnclick(3)).grid(row=1,column=2)

addition=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="+",command=lambda:btnclick('+')).grid(row=1,column=3)

#=====================================================================================================================================================================================================================
#Second row



btn4=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="4",command=lambda:btnclick(4)).grid(row=2,column=0)

btn5=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="5",command=lambda:btnclick(5)).grid(row=2,column=1)

btn6=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="6",command=lambda:btnclick(6)).grid(row=2,column=2)

subs=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="-",command=lambda:btnclick('-')).grid(row=2,column=3)

#=====================================================================================================================================================================================================================
#3rd row

btn7=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="7",command=lambda:btnclick(7)).grid(row=3,column=0)

btn8=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="8",command=lambda:btnclick(8)).grid(row=3,column=1)

btn9=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="9",command=lambda:btnclick(9)).grid(row=3,column=2)

multip=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="x",command=lambda:btnclick('x')).grid(row=3,column=3)

#=====================================================================================================================================================================================================================
#4th row

btn0=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="0",command=lambda:btnclick(0)).grid(row=4,column=0)

equal=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="=",command=btnequal).grid(row=4,column=1)

clear=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="c",command=btnclear()).grid(row=4,column=2)

divide=Button(calc,font=("arial",20,'bold'),padx=15,bd=8,fg="black",text="/",command=lambda:btnclick('/')).grid(row=4,column=3)

#=====================================================================================================================================================================================================================
#End of row


calc.mainloop()

