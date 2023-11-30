from tkinter import *

root=Tk()
def add():
    l4.config(text=int(entry1.get()) + int(entry2.get()))
def subtract():
     l4.config(text=int(entry1.get()) - int(entry2.get()))
def multiply():
    l4.config(text=int(entry1.get()) * int(entry2.get()))
def divide():
    l4.config(text=int(entry1.get()) / int(entry2.get()))
root.geometry("790x300")
root.title("Python")
root.configure(borderwidth=5,relief=SUNKEN)
Label(text="\"Arithmetic Operation\"",font="lucida 20 bold underline",padx=10,pady=15,bg="Light blue")\
    .grid(row=1,column=5,ipady=5)
l1=Label(text="First Number",font="lucida 10 bold",pady=15)
l1.grid(row=5,column=3)
l2=Label(text="Second Number",font="lucida 10 bold",pady=15)
l2.grid(row=6,column=3)
l3=Label(text="Result",font="lucida 10 bold",pady=15)
l3.grid(row=9,column=3)
l4=Label(text="Answer",font="lucida 10 bold",pady=15)
l4.grid(row=9,column=4)
entry1=StringVar()
entry2=StringVar()
entry3=StringVar()
Entry(textvariable=entry1).grid(row=5,column=4)
Entry(textvariable=entry2).grid(row=6,column=4)
# Entry(textvariable=entry3).grid(row=9,column=4)
Button(text="ADD",font="lucida 10 bold",borderwidth=3,command=add).grid(row=8,column=3)
Button(text="SUBTRACT",font="lucida 10 bold",borderwidth=3,command=subtract).grid(row=8,column=4)
Button(text="Multiply",font="lucida 10 bold",borderwidth=3,command=multiply).grid(row=8,column=5)
Button(text="Divide",font="lucida 10 bold",borderwidth=3,command=divide).grid(row=8,column=6)
root.mainloop()