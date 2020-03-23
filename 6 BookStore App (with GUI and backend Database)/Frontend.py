from tkinter import *
from backend import *

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in view_d():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in search_d(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get()):
        list1.insert(END,row)

def add_command():
    insert_d(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get())
    list1.delete(0, END)
    view_command()

def delete_command():
    delete_d(selected_tuple[0])
    list1.delete(0, END)
    view_command()

def update_command():
    update_d(id=selected_tuple[0], title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get())
    list1.delete(0, END)
    view_command()

window = Tk()
window.wm_title("Book Store (By gobinathan)")

l1=Label(window, text="Title")
l1.grid(row=0, column=0)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1=Listbox(window, height=10, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

s1=Scrollbar(window)
s1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=s1)
s1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,width=12,text="View All",command=view_command)
b1.grid(row=2, column=3)

b2=Button(window,width=12,text="Search Entry",command=search_command)
b2.grid(row=3, column=3)

b3=Button(window,width=12,text="Add Entry",command=add_command)
b3.grid(row=4, column=3)

b4=Button(window,width=12,text="Update",command=update_command)
b4.grid(row=5, column=3)

b5=Button(window,width=12,text="Delete",command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window,width=12,text="Close",command=exit)
b6.grid(row=7, column=3)

window.mainloop()
