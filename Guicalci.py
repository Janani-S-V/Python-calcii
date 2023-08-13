import tkinter
from tkinter import *
n=Tk()
n.title("Python calculator")
n.geometry("570x600+100+200")
n.configure(bg="black")
eqn=""
def show(value):
    global eqn
    eqn+=value
    result.config(text=eqn)
def clear():
    global eqn
    eqn=""
    result.config(text=eqn)
def calculate():
    global eqn
    res=""
    if eqn!="":
        try:
            res=eval(eqn)
        except:
            res="error"
    result.config(text=res)

result=Label(n,width=25,height=2,text="",font=("arial",30))
result.pack()
Button(n,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="orange",command=lambda: clear()).place(x=10,y=100)
Button(n,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("/")).place(x=150,y=100)
Button(n,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("%")).place(x=290,y=100)
Button(n,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("*")).place(x=430,y=100)

Button(n,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("7")).place(x=10,y=200)
Button(n,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("8")).place(x=150,y=200)
Button(n,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("9")).place(x=290,y=200)
Button(n,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("-")).place(x=430,y=200)


Button(n,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("4")).place(x=10,y=300)
Button(n,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("5")).place(x=150,y=300)
Button(n,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("6")).place(x=290,y=300)
Button(n,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("+")).place(x=430,y=300)

Button(n,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("1")).place(x=10,y=400)
Button(n,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("2")).place(x=150,y=400)
Button(n,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("3")).place(x=290,y=400)
Button(n,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show("0")).place(x=10,y=500)

Button(n,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="black",command=lambda: show(".")).place(x=290,y=500)
Button(n,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="white",bg="grey",command=lambda: calculate()).place(x=430,y=400)
