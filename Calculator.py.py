from tkinter import *
masterwindow =Tk()
masterwindow.title("simple calculator")
n1 =IntVar()
n2= IntVar()
r1=IntVar()

masterwindow.geometry("+500+500")
masterwindow.minsize(1000,500)
def add():
    n1 = number1.get()
    n2 = number2.get()
    r1.set(int(n1)+int(n2))


def sub():
    n1 = number1.get()
    n2 = number2.get()
    r1.set(int(n1)-int(n2))



def mul():
    n1 = number1.get()
    n2 = number2.get()
    r1.set(int(n1) * int(n2))


def div():
    n1=number1.get()
    n2=number2.get()
    r1.set(int(n1) / int(n2))


def exit():
    masterwindow.destroy()

l1=Label(masterwindow,text="number 1:",bg="grey",font=("Arial",12,"italic"))
l2=Label(masterwindow,text="number2:",bg="grey",font=("Arial",12,"italic"))
l3=Label(masterwindow,text="result:",bg="grey",font=("Arial",12,"italic"))

b1 = Button(masterwindow, bg="gold",fg="red",   text = 'add',command=add)
b2 = Button(masterwindow, bg="gold",fg="red",   text = 'sub',command=sub)
b3 = Button(masterwindow, bg="gold",fg="red",   text = 'mul',command=mul)
b4 = Button(masterwindow, bg="gold",fg="red",   text = 'div ',command=div)
b5 = Button(masterwindow, bg="gold",fg="red",   text = 'exit ',command=exit)

number1=Entry(masterwindow,textvariable=n1)
number2=Entry(masterwindow,textvariable=n2)
result= Entry(masterwindow,textvariable=r1)

l1.place(x=20,y=40)
number1.place(x=150,y=40)

l2.place(x=20,y=80)
number2.place(x=150,y=80)

l3.place(x=20,y=120)
result.place(x=150,y=120)

b1.place(x=50,y=180)
b2.place(x=150,y=180)
b3.place(x=50,y=240)
b4.place(x=150,y=240)
b5.place(x=250,y=225)

mainloop()