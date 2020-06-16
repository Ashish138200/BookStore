from tkinter import *
import backend

#print(backend.view())
def get_selected_row(event): #Event parameter holds the type of event
    '''When the get_selected_row  function is called, Python will execute the indented block under try . If there is an
    IndexError, none of the lines under try  will be executed; the line under except  will be executed, which is pass.
    The pass  statement means "do nothing". Therefore the function will do nothing when there's an empty listbox.'''
    try:
        global selected_tuple
        index=list1.curselection()[0] #get the index of the selected row; [0]:The index from the tuple
        selected_tuple=list1.get(index) # from the listbox get the tuple with index x
        e1.delete(0,END) #entry must be empty
        e1.insert(END,selected_tuple[1]) #title
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2]) #author name
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3]) #year
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4]) #ISBN
    except IndexError:
        pass

def view_command():
    list1.delete(0,END) #to ensure that the listbox is empty when you click view All button again and again
    for row in backend.view():
        list1.insert(END,row) # insert(rowposition(1,2,....END),row)

def search_command():
    list1.delete(0,END)
    # something.get() will convert it into a string
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    #something.get() will convert it into a string
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])
#selected_tuple[0] : index
def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window=Tk()
photo = PhotoImage(file = "bookstore.png")
window.iconphoto(False, photo)

window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row) # This method return the values of the selected object in the listbox

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
