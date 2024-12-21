""
"""
Exception Handling:

Java Keywords:
try
catch
finally
throw
throws


Python Keywords:
try
except
finally
raise


"""
#New Program
#BLL
import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def pow(a,b):
    return a**b

# #PL
# while (1):
#     try:
#         no1 = int(input("Enter First No:"))
#         no2 = int(input("Enter Second No:"))
#         choice = input("Enter Any operation +,-,*,/,pow,log:")
#         if (choice == "+"):
#             res = add(no1, no2)
#             print("Result:", res)
#         elif (choice == "-"):
#             res = sub(no1, no2)
#             print("Result:", res)
#         elif (choice == "*"):
#             res = mul(no1, no2)
#             print("Result:", res)
#         elif (choice == "/"):
#             res = div(no1, no2)
#             print("Result:", res)
#         elif (choice == "pow"):
#             res = pow(no1, no2)
#             print("Result:", res)
#         elif (choice == "log"):
#             res = math.log(no1, no2)
#             print("Result:", res)
#         else:
#             raise NotImplementedError("Incorrect Choice")
#     except Exception as err:
#         print("Error!",err)
#         print(type(err))


# #New Program
# x=235
# print(len(x))           #x.__len__()
#
# s="CETPA"
# print(len(s))       #s.__len__()


"""
to store the data permanently: files writes, database write

File Handling: To store the data permanently.

We have already discussed about input and print function, in both
cases data travels in string format. 

"Welcome to CETPA" data will be travelled in streams format


"""
# a,b=5,7
# r=(a>b)         #   a.__gt__(b)
# print(r)

# #New Program
# class Customer:
#     pass
# obj=Customer()
# print(type(obj))

# #New Program
# x=5
# print(type(x))
# int

# #New Program
# L=[10,20]
# L.append(30)
# print(L)
# print(type(L))

# #New Program
# def add(a,b):
#     return a+b
# r=add(5,7)

class Customer:
    pass
obj1=Customer()     #obj1 of Customer Class
def func1():
    return Customer()
obj2=func1()


"""
For file handling: Firstly we need to create an object of 
TextIOWrapper Class
TextIOWrapper Class is made inside io module.
TExtIOWrapper in general terms is called file class
"""

# # #New Program
# f=open("D://temp/file1.txt","r")
# print(type(f))      #f is an object of TextIOWrapper Class

# #New Program
# f=open("D://temp/file1.txt","r")        #s="CETPA"
# data=f.read()                           #data=s.lower()
# print(data)                             #print(data)

# #New Program
# f=open("D://Temp/file1.txt","r")
# data=f.read(5)
# print(data)
# data=f.read(10)
# print(data)
# f.close()

"""
Modes of file operations:
Text Modes: String Modes: Character Modes: Here data must be in string
format only
r    :  Read Mode: In Read Mode, if file exists then data will be
                read from starting of file and if file doesn't
                exist then error. 
w   :   Write Mode:  In write Mode, if file exists then firstly 
                data will be truncated and then data will be
                written at starting of the file and if file doesn't
                exist then new file will be created.
a   :   Append Mode: In append Mode, if file exists then data will be
                written at the end of the file and if file doesn't
                exist then new file will be created.
r+  :   Read and Write Mode
w+  :   Write and Read Mode
a+  :   Append and Read mode

Binary Modes: Data must be in binary format
rb    :  Read Mode Binary: if file exists then data will be
                read from starting of file and if file doesn't
                exist then error. 
wb   :   Write Mode Binary:  if file exists then data will be
                written at starting of the file and if file doesn't
                exist then new file will be created.
ab   :   Append Mode Binary: if file exists then data will be
                written at the end of the file and if file doesn't
                exist then new file will be created.
rb+  :   Read and Write Mode Binary
wb+  :   Write and Read Mode Binary
ab+  :   Append and Read mode Binary
"""
# #New Program
# s=b"CETPA"
# print(type(s))

# #New Program
# s="CE\nT\P\tA"
# print(s)

# #New Program
# s="CE\\nT\P\\tA"
# print(s)

# #New Program
# s=r"CE\nT\P\tA"     #Raw String
# print(s)

# #New Program
# f=open(r"D:\Temp\file1.txt","r")
# print(f.read())

# #New Program
# f=open(r"D:\Temp\file1.txt","w")
# print(f.read())       #Error
# f.close()

# #New Program
# f=open(r"D:\Temp\FamilyTheme.mp3","w")

#New Program


# #New Program
# f=open(r"D:\Temp\file2.txt","w")
# data="Hello World"
# f.write(data)
# f.close()

# #New Program
# f=open(r"D:\Temp\file2.txt","rb")
# data=f.read()
# print(data)
# f.close()

"""
os library
"""
# #New Program
# import os
# os.startfile("D:/temp/01 Kal Ho Naa Ho - Sonu Nigam.mp3")

# #New Program
# import os
# os.startfile("D:/temp/Cetpa Video.mp4")


