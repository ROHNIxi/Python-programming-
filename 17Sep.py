""
"""
Please create your account on github:
Purpose: 
1. You can showcase your projects to HR.
2. You can contribute your project to the world, give and take.
In a team work, you can share the resource and can enhance the 
project
3. While working in the industry or during interview, for freshers
having basic knowledge of github is mandatory. 
4. Industry uses paid version of github. Github is a VCS tool.
VCS stands for Version Control System.

Please github pe kuch videos dekh lo and apne aap bhee padhna sikho.
Course khatam ho jayega to mai apke saath apke office ya ghar nahi
aaunga aage apki help karne ke liye. So please be ready for the
industry independently. 

"""

"""
Lambda Functions:
"""
# #New Program
# func=lambda a:a/2       #func is the function pointer
# print(func(5))

# #New Program
# def func(a):
#     return a/2
#
# print(func(5))

# #New Program
# evenodd=lambda a:a%2==0
# res=evenodd(55)
# print(res)

# #New Program
# def func(a):
#     if(a%2==0):
#         return True
#     else:
#         return False    #return a%2==0
# print(func)

# #New Program
# evenodd=lambda a:a%2==0
#
# number=int(input("Enter Any Number:"))
# res=evenodd(number)
# print(res)

"""
OOPS: Object Oriented Programming:
For OOPS base is Class

Class: Is a collection of variables and functions. In OOPS or in
class, generally the functions are called methods.

Python supports modular approach of programming: A good programmer
is a programmer, who divide the code in to small blocks or modules.
A good programme should follow a hierarichal architecture.
A big project should be made up of multiple python files (modules).
Each modules should made up of Classes. Each class should be made
up of functions and variables.
Divide your projects into multiple layers, modules, classes, 
methods and functions as per the need.
We can develop any big project without OOPS also but complexity of
the project will be increased a lot. Using OOPS, we can decrease
the complexity of the project, the project is made scalable using 
OOPS, we can easily modify and enhance the project later using OOPS.

Syntax to create a class:
class Class_Name:
    variables and methods ie block of code

To access a normal variable or function which is created outside
class we can access them directly.
If a variable or function is created inside class then we can 
access them through object or class.

How to create object of any class:
obj_name=class_name(arguments)
obj_name=class_name()

Like list hold multiple elements and each element can be a variable
similarly object can hold multiple variables ie multiple values.

When we print the objects of user defined class, then address of
the objects are printed.
"""
# #New Program
# class C1:
#     pass
# obj=C1()        #obj is object of C1 Class
# print(type(obj))
# print(obj)

# #New Program
# L1=[1,2,3]
# L2=[5,6,7]
# L1.append(10)       #if append is function not a method append(L1,10)
# print(L2)
# print(L1)

# #New Program
# s="Cetpa"
# r="hello"
# s.upper()

# #New Program
# class MyClass:
#     def func1(a,b):
#         print(a,b)
# obj1=MyClass()  #obj1 is object of MyClass
# obj1.func1(5)

"""
If we are calling a method which is created inside a class, then
while calling from actual parameters, first object is passed
to formal parameters and then rest of the arguments are passed.
"""

# #New Program
# d1={1:10,2:20,3:30}     #d1 is of dict type
# d2={11:100,12:200,13:300}
# res=d1.values()     #If values is a function values(d1)
# print(res)


# #New Program
# x=5
# print(x)


# #New Program
# class MyClass:
#     def func1(a,b):
#         print(a,b)
# obj1=MyClass()  #obj1 is object of MyClass
# u=5
# obj1.func1(u)   #a=obj1,b=u
# print(obj1)

"""
When we call a method which is inside a class then from formal
parameters object is passed to the first argument of actual
parameters. Python recommends that the object name in formal
parameters should be self.

"""
# #New Program
# L1=[1,2,3]
# L1.append(5)

#New Program
"""
Class is a collection of attributes or properties. Class 
properties are variables and methods.
"""
# #New Program
# L1=["ab","cd"]
# L1.upper()      #AttributeError: 'list' object has no attribute 'upper'
# print(L1)

# #New Program
# class Customer:
#     def func1(self,a,b):
#         pass
#
# cus=Customer()
# cus.func1(5,7)

"""
Class represents real time entity.
One of the benefits of using OOPS is that we can easily represent
real time entities using classes.

Syntax to call a method of a class:
obj_name.method_name(arguments)

There is one more syntax to call a class method in Python:
class_name.method_name(object_name,arguments)
"""
# #New Program
# L1=[10,20,30]
# L1.append(40)
# print(L1)
# L1=[10,20,30]
# list.append(L1,40)
# print(L1)

"""
We have two types of variables in a class:
Instance/object variable
Static/class variable


We have two types of functions in a class:
Instance/object methods (functions)
Static/class functions

How to create instance/object variable:
By assigning the value.
obj_name.variable_name=value

How to access a method of a class:
obj_name.method_name(arguments)

How to access an instance variable:
obj_name.variable_name
"""

# #New Program
# class C1:
#     pass

# #New Program
# class C1:
#     pass
# obj1=C1()
# obj1.a=5    #a is a variable of obj1 object
# print(obj1.a)
# obj1.b=7
# obj1.c=9
# print(obj1.a,obj1.b,obj1.c)
# obj2=C1()
# obj2.a=20
# obj2.b=30
# print(obj1.a,obj1.b,obj1.c,obj2.a,obj2.b)


# #New Program
# a,b,c,d,e,f=1,2,3,4,5,6
# L1=[]
# L2=[]
# L1.append(a)
# L1.append(b)
# L1.append(c)
# L2.append(d)
# L2.append(e)
# L2.append(f)
# print(L1,L2)

"""
All user defined classes are mutable in nature.

L1=[10,20,30]       #L1 Address 1000
L2=L1               #L2 address 1000
L1.append(40)       #L1 address 1000
print(L2)       #[10,20,30,40]
"""

"""
Object inside class is called self. If we make some changes
in self then these changes will also be reflected in corresponding
object
"""

# #New Program
# class C1:
#     def func1(self):    #self address 1000
#         self.a=5        #self address 1000
#         self.b=7        #self address 1000
#
# obj=C1()        #obj address 1000
# obj2=C1()       #obj2 address 2000
# obj.func1()     #self=obj, self address 1000
# print(obj.a,obj.b)









