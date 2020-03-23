from tkinter import *

def printcom():
    print(e1value.get())
    t1.insert(END, e1value.get())

window = Tk()

b1 = Button(window,text="Button", command = printcom)
b1.grid(row=2,column=2)

e1value = StringVar()
e1 = Entry(window,textvariable=e1value)
e1.grid(row=2,column=3)
print(e1value)

t1 = Text(window,height=1,width=1)
t1.grid(row=2,column=4)









window.mainloop()
