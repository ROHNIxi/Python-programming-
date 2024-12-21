""
"""
GUI Programming Continue.
Pack, Place and Grid geometry won't work together.
Grid is the best geometry to use
"""
# #New Program
# import tkinter as tk
# def leftClick():
#     print("I am Clicked")
# root=tk.Tk()
# root.geometry("300x400")
# btn1=tk.Button(root,text="ABCD",font=1,bg="Red",fg="Yellow",command=leftClick)
# btn1.grid(row=0,column=0)
# root.mainloop()

"""
print function in python is used to print the data
on console window.
Label widget in tkinter is used to display the data
on GUI screen

"""

# #New Program
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x400")
# lbl_id=tk.Label(root,text="Enter Cust ID:",font=1)
# lbl_id.grid(row=0,column=0)
# lbl_name=tk.Label(root,text="Enter Cust Name:",font=1)
# lbl_name.grid(row=1,column=0)
#
# root.mainloop()

"""
Entry widget: To take input from GUI screen in 
single line.

Like input function, we take the data in some
variable, similarly in Entry widget we will input
the data in some variable.
Till now in Python we have discussed, that variables
are created in python by assigning the value. 
Variables created through input functions will
always be of type string.
But in GUI tkinter programming, the variables
are not automatically created by assigning the 
value. Here also like in C Lang or Java, we need
to firstly define the variable type.
"""
# L=list()    #Empty List

#New Program
import tkinter as tk
def data_capture():
    id=var_id.get()
    print(id)
    var_id.set("")
root=tk.Tk()

root.geometry("400x500")
lbl_id=tk.Label(root,text="Enter Cust Id:",font=1)
lbl_id.grid(row=0,column=0)
var_id=tk.StringVar()
entry_id=tk.Entry(root,textvariable=var_id,font=1)
entry_id.grid(row=0,column=1)
btn_submit=tk.Button(root,text="Submit",font=1,command=data_capture)
btn_submit.grid(row=1,column=1)
root.mainloop()









