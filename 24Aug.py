""
"""
Swapping is Variable
"""
# #Using 3rd Variable
# a=5
# b=7
# temp=a      #3rd Varaible is temp, temp=5, b=7, a=5
# a=b         #a=7, temp=5
# b=temp
# print(a,b)

# #New Program
# a,b=5,7
# a,b=b,a
# print(a,b)

"""
Shoaib
a =5 b=10 c =a+b a= c-a b=c-b Print (‘a =’ ,a) Print (‘b =’ ,b)
"""

"""
pass is a instruction in python, which does nothing
There are places in python, where we must write some block of
code, like inside a heading, there for the time being we can write
pass
"""
# #New Program
# pass
# pass
# pass
# pass
# pass

# #New Program
# x=6
# if(x==5):
#     print("CETPA")

# #New Program
# x=6
# if(x==5):
#     print("CETPA")
# else:
#     pass

# #New Program
# x=5
# if(x!=5):
#     pass
# else:
#     print("CETPA")


"""
Program/Application/Software/Computer: To take the date from the
user, process the data and generate the outputs.
"""
# print()
# print()

"""
Take two inputs from the user and check their data types. 
sir is there a way to know input
"""
# #New Program
# x=input("Enter A Number:")
# print(type(x))
# x=input("Enter A String:")
# print(type(x))

"""
Nested conditions: We can use conditions or group of conditions
inside any condition ie inside if, elif or else 
"""

# #New Program
# choice=input("Enter day:")
# if(choice=="Stop"):
#     print("Program stopped")
# else:
#     if(choice=="Sunday"):
#         print("Take Rest")
#     elif(choice=="Satruday"):
#         print("After the class, go to movie")


# """
# Example: Find the bigger of 2 numbers without using logical operators
# """
# #New Program
# no1=int(input("Enter First No:"))       #no1=5
# no2=int(input("Enter Second No:"))      #no1=7
# if(no1>no2):
#     print(no1, "is bigger")
# else:
#     print(no2,"is bigger")


"""
Example: Find the biggest of 3 numbers without using logical operators
or using nested conditions
"""
# #New Program
# no1=int(input("Enter First No:"))       #no1=5
# no2=int(input("Enter Second No:"))      #no1=7
# no3=int(input("Enter Third No:"))       #no1=9
# if(no1>no2):        #no2 is not the biggest no
#     if (no1 > no3):
#         print(no1, "is the biggest no")
#     else:
#         print(no3, "is the biggest no")
# else:               #no1 is not the biggest no
#     if (no2 > no3):
#         print(no2, "is the biggest no")
#     else:
#         print(no3, "is the biggest no")

"""
Find the biggest of 3 numbers using logical operators or without
using nested conditions.
"""
# #New Program
# no1=int(input("Enter First No:"))       #no1=7
# no2=int(input("Enter Second No:"))      #no2=5
# no3=int(input("Enter Third No:"))       #no3=9
# if(no1>no2 and no1>no3):
#     print(no1,"is the biggest no")
# elif(no2>no3):                   #no1 is not the biggest no
#     print(no2,"is the biggest no")
# else:
#     print(no3, "is the biggest no")

"""
Example: Find the bigger of 2 numbers and also check whether they are 
equal or not
"""
# #New Program
# no1=int(input("Enter First No:"))       #no1=5
# no2=int(input("Enter Second No:"))      #no1=7
# if(no1>no2):
#     print(no1, "is bigger")
# elif(no2>no1):
#     print(no2,"is bigger")
# else:
#     print("Both the numbers are equal")

# #New Program
# no1=int(input("Enter First No:"))       #no1=5
# no2=int(input("Enter Second No:"))      #no1=7
# if(no1==no2):
#     print("Both the numbers are equal")
# elif(no1>no2):
#     print(no1,"is bigger")
# else:
#     print(no2,"is bigger")

"""
string: 
data type in python: str
string is a collection of homogeneous data type ie characters.
string is made using single, double or triple quotes

till now we have used functions in python:
Syntax to call a function:
function_name(arguments)

class: 
    is a data type.
    is a collection of variables and functions (methods)

A good programmer, who makes the program scalable.
To make the project scalable, we divide the project into multiple
modules and layers.
Layers are further divided into classes. Classes are made up
of functions and variables.

ERP: Enterprise Resource Planning

The functions which are outside class are called functions only,
how to call them: function_name(arguments)

The functions which are inside class are called methods or functions,
how to call method or a function made inside class:
obj_name.method_name()

How to create object of any class in python: 
Standard syntax: 
obj_name=class_name()
or
obj_name=class_name(arguments)
Above syntax will create a default valued object of the class

s=str() #variable or object of string class
Default value of string class is emtpy string

n=int() #variable or object of int class
Default value of int class is 0

In python for predefined general data types, we can directly
pass the value and can create the objects or variables
a=5         #int variable



"""
# #New Program
# s=str()     #
# print(s)
# print(type(s))


# #New Program
# f=float()     #
# print(f)
# print(type(f))

# #New Program
# s="Cetpa"       #Object of string class
# r=s.upper()
# print(r)

# #New Program
# s="Cetpa123"       #Object of string class
# r=s.lower()
# print(r)

"""
Python free IDLE: python.org: Not a single company in the world
uses IDLE. Why: Bahut hee thaki hui IDE hai.


"""

# #New Program
# s="CE**TPA*"
# r=s.replace("*","##")
# print(r)

# #New Program
# s="C*E**TPA*"
# r=s.replace("*","##",2)
# print(r)

# #New Program
# s="cetpa infotech**"
# r=s.title()
# print(r)

"""
split methods splits a string and generate a list based on
criteria given
Default criteria is space
"""
# #New Program
# s="cet*pa info*tech"
# r=s.split("*")
# print(r)

# #New Program
# name="Vikas Kumar Kalra"
# name=name.split()
# print(name)

# #New Program
# name="Vikas*Kumar*Kalra"
# name=name.split("*",1)
# print(name)

# #New Program
# name=input("Enter Your Name:")
# name=name.split()
# print(name)

# #New Program
# name=input("Enter Your Name:").split()
# print(name)

# #New Program: "10 20 30 40 50"
# nos=input("Enter 5 numbers:").split()
# print(nos)

"""
Next week: Wednesday to Saturday:
New Students: Mon, tue
"""








