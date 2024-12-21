""
"""
Language Translator


"""
# #New Program
# from googletrans import Translator
# t=Translator()
# r=t.translate("Good Morning","ru")
# print(r)
# res=r.text
# print(res)


# #New Program
# import tkinter as tk
# import googletrans
# def display(data):
#     lbl_out=tk.Label(root,text=data,font=1)
#     lbl_out.grid(row=3,column=0)
#
# def conv_to_Hindi():
#     msg=var_in.get()        #msg="Good Morning"
#     r=t.translate(msg,"hi")
#     data=r.text
#     display(data)
# root=tk.Tk()
# root["bg"]="Green"
# root.geometry("400x500")
# t=googletrans.Translator()
# lbl_1=tk.Label(root,text="Enter Message in Any Langauge")
# lbl_1.config(fg="Blue",font=20)
# lbl_1["bg"]="Orange"
# lbl_1.grid(row=0,column=0,padx=10,pady=50)
# var_in=tk.StringVar()
# entr_1=tk.Entry(root,textvariable=var_in,font=1)
# entr_1.grid(row=1,column=0)
#
# btn_hi=tk.Button(root,text="Hindi",font=1,bg="Yellow",fg="Blue",command=conv_to_Hindi)
# btn_hi.grid(row=2,column=0)
#
# root.mainloop()

# #New Program
# import tkinter as tk
# def leftClickHandler(e):
#     print("Left Click")
#     print(e.x,e.y)
#     wdgt=e.widget
#     wdgt["bg"]="Orange"
#
# def rightClickHandler(e):
#     print("Right Click")
#     wdgt=e.widget
#     wdgt["bg"]="Yellow"
#     print(wdgt["text"])
# root=tk.Tk()
# root.geometry("500x600")
# btn=tk.Button(root,text="ABCD",font=1,width=15,height=4)
# btn.pack()
# btn.bind("<Button-1>",leftClickHandler)
# btn.bind("<Button-3>",rightClickHandler)
#
# root.mainloop()


# #New Program
# import tkinter as tk
# def oneHandler(e):
#     wdgt=e.widget
#     # wdgt["text"]="Orange"
#     # wdgt["bg"]="Red"
#     if(wdgt["text"]=="Blue"):
#         root["bg"]="Blue"
#     elif (wdgt["text"] == "Green"):
#         root["bg"] = "Green"
#     else:
#         root["bg"] = "Red"
#
# root=tk.Tk()
# root.geometry("600x500")
# btn_blue=tk.Button(root,text="Blue",font=1,width=15,height=3)
# btn_blue.bind("<Button-1>",oneHandler)
# btn_blue.grid(row=0,column=0)
# btn_green=tk.Button(root,text="Green",font=1,width=15,height=3)
# btn_green.grid(row=0,column=1)
# btn_green.bind("<ButtonPress-1>",oneHandler)
# btn_red=tk.Button(root,text="Red",font=1,width=15,height=3)
# btn_red.grid(row=0,column=2)
# btn_red.bind("<ButtonPress-1>",oneHandler)
#
#
# root.mainloop()


# #New Program
# import tkinter as tk
# def handler(e):
#     wdgt=e.widget
#     print(wdgt["text"])
# root=tk.Tk()
# count=0
# for i in range(4):
#     for j in range(4):
#         count+=1
#         btn=tk.Button(root,text=str(count),font=1,height=2,width=5)
#         btn.grid(row=i,column=j)
#         btn.bind("<Button-1>",handler)
#
#
# root.mainloop()
#




