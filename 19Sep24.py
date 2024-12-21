""
"""
Class is a data type:

Object represents the actual memory. Object is an instance of a
class.
"""
# class C1:
#     def method1(self,a,b):  #self=1000,a=5,b=7
#         print(self,a,b)
#         print(type(self),type(a))
#
# ob=C1()                     #ob address 1000
# print(ob)
# print(type(ob))
# ob.method1(5,7)   #self=ob,a=5,b=7


# #New Program
# def func1(a,b,c):
#     print(a,b,c)
# class C1:
#     pass
# ob1=C1()
# ob2=C1()
# func1(ob1,ob2,5)

# #New Program
# a=5
# cetpa=7
# self_8=9
# print(a,cetpa,self_8)

"""
How to create instance/object variable inside class
obj.var=value
now object inside class is self
self.var=value

How to access instance variables or instance methods:
obj.var
obj.method   ie obj.method(arguments)

"""

"""
Create a generalized function which takes any no of arguments 
and return the multiplication of all arguments using variable 
length keyword argument function. 
"""

# #BLL
# def mul(*args):     #args=(2, 3, 4, 5, 6)
#     r=1
#     for i in range(len(args)):
#         r=r*args[i]
#     return r
# #PL
# r1=mul(2,3,4,5,6)
# r2=mul(1,2)
# print(r1,r2)

"""
Create your own generalized index function. Print all the matching index 
positions of an element present in a list [2,3,4,5,6,2,3,4,2,3,4,2]. Take the 
element as input from the user.  
"""
# #New Program
# L=[2,3,4,5,6,2,3,4,2,3,4,2]
# ele=2
# for i in range(len(L)):     #i=0,1,2,...n-1
#     if(L[i]==ele):
#         print(i)

# #New Program
# def myAllIndex(name):
#     index_L=[]
#     for i in range(len(idlist)):     #i=0,1,2,3,4
#         if(namelist[i]==name):
#             index_L.append(i)
#     return index_L
#
# idlist=[10,20,30,40,50]
# namelist=["Vikas","Amit","Vikas","Akshat","Prakash"]
# agelist=[39,23,45,18,12]
# name="Vikas"
#
# index_list=myAllIndex(name)
# print(index_list)

"""
OOPS Concept
"""
# def func1(L):       #L address 1000
#     L.append(5)     #L address 1000
#
# L1=[10,20]          #L1 address 1000
# func1(L1)           #L=L1, L address 1000
# print(L1)

# #New Program
# class C1:
#     def func1(self):        #self=1000
#         self.a=5            #self =1000
#         self.b=7
#
# ob=C1()     #Object of C1 Class, how many variables with ob, 0 variable
# ob.func1()      #ob address 1000, self=ob, self 1000
# print(ob.a,ob.b)
# #print(self.a,self.b)     #Error : self is local object

# #New Program
# class C1:
#     def createVariables(self):#self=1000, self=2000
#         self.a=1
#         self.b=2
#         self.c=3
# ob1=C1()        #ob1 address 1000
# ob2=C1()        #ob2 address 2000
# ob1.createVariables()   #self=ob1
# print(ob1.a,ob1.b,ob1.c)
# ob2.createVariables()   #self=2000
# print(ob2.a,ob2.b,ob2.c)
# ob1.a=5
# print(ob2.a,ob1.a)

"""
Constructor: is a method, which is called automatically everytime
we create an object in python. In Python the name of the constructor
is fixed ie __init__() 

"""
# #New Program
# class C1:
#     def __init__(self):     #Constructor
#         print("CETPA")
#
# ob1=C1()
# ob2=C1()
# ob3=C1()

"""
Generally in programming in real world, the variables of all
objects of a class are common like
all customers will have same variables like id,name,age,mob
so we mostly create the variables inside constructor.


"""
# class Customer:
#     def __init__(self):  #self=1000, self=2000
#         self.id=0       #1000.id=0, 2000.id=0
#         self.name=0     #1000.name=0
#         self.age=0      #1000.age=0
#         self.mob=0      #1000.mob=0
# cus1=Customer()      #cus1 1000, self 1000
# print(cus1.id,cus1.name,cus1.age,cus1.mob)
# cus2=Customer()     #cus2 2000 , self 2000
# print(cus2.id,cus2.name,cus2.age,cus2.mob)

"""
How to add 2 numbers using OOPS
"""
# #BLL
# class MyClass:
#     def __init__(self):  #self=1000
#         self.no1=0
#         self.no2=0
#         self.res=0
#     def add(self):      #self=1000,self.no1=5,self.no2=7,self.res=0
#         self.res=self.no1+self.no2  #1000.res=12
#         #return self.res  Don't write this statement
# #PL
# cal=MyClass()        #self=cal=1000,cal.no1=0,cal.no2=0,cal.res=0
# cal.no1=int(input("Enter First No:"))    #cal.no1=5
# cal.no2=int(input("Enter Second No:"))   #cal.no2=7
# cal.add()    #self=cal, self=1000
# print("Result:",cal.res)

# #New Program
# def func(L):
#     L.append(5)
#
# L1=[10,20]
# func(L1)
# print(L)        #Error L is local variable

# #New Program
# class C1:
#     def __init__(self): #self=1000
#         self.a=1
#         self.b=2
#     def modifyData(self):  #self=1000, self.a=1,self.b=2
#         self.a=4            #1000.a=4,self.a=4
#         self.b=5            #1000.b=5
#     def showData(self):     #self=1000
#         print(self.a,self.b)
# ob=C1()     #ob=1000, ob.a=1.ob1.b=2
# ob.modifyData()     #
# ob.showData()

"""
Till now the variables and methods we discussed are
instance/object variables and methods. These are associated
with objects ie if there are 10 objects then each object
have their independent variables.

Now class or static variables and methods. These variables or
method are like normal variables or functions which we have
studied outside class. 
How to create static variables:
Same syntax like outside class. Directly inside class, assign
the value
var_name=value

How to access static variables: using class name
class_name.var_name
Static variables will be common variables

Real properties of python are objects. So instance functions
are generally called methods but static functions are 
generally called functions.

So as per the need, if we want to create separate variables
for different object then we create instance variable.
If we want same variable for all objects then we create static
variables.
"""
# #New Program
# class C1:
#     x,y=1,2     #Static variables
#     def __init__(self):
#         self.a,self.b=3,4   #Instance variable
# print(C1.x,C1.y)
# ob=C1()
# print(ob.a,ob.b)


# #New Program
# class C1:
#     x,y=1,2     #Static variables
#     def __init__(self):
#         self.a,self.b=3,4   #Instance variable
# print(C1.x,C1.y)
# ob1=C1()
# print(ob1.a,ob1.b)
# ob2=C1()
# print(ob2.a,ob2.b)



