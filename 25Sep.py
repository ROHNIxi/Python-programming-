""
"""
Multiple Inheritance: One Child Multiple Parents
"""
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     # def showData(self):
#     #     print("I am in Class C1")
# class C2:
#     def __init__(self):
#         self.c=3
#         self.d=4
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3:
#     def __init__(self):
#         self.e=5
#         self.f=6
#     def showData(self):
#         print("I am in Class C3")
# class C4(C1,C2,C3):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C2.__init__(self)
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# obj=C4()        #object of C4. obj.__init__()
# obj.showData()
# print(obj.a,obj.b,obj.c,obj.d,obj.e,obj.f,obj.g,obj.h)


"""
In above program, if we have showData method in all 3 parents but
not in child. Now if we call showData method using child object
then it may create an ambiguity or in Java it creates ambiguity
that which parent showData method will be called? So this ambiguity
in Java is called Diamond Problem and there is no direct solution
made for diamond problem in Java ie Java doesn't support Multiple
Inheritance. But in Python this a solution is made for this ambiguity
using Priority setting and making MRO (Method Resolution Order)
If there are multiple parents of one child ie C1, C2, C3 then
direct priority will be given from left to right as we mention
parents name in child class.

Now in above program as we have multiple parents for one child
so to create variables of all parents, we need to call constructor
of all the parents in child class.
  
"""
# class C1:
#     pass
# print(type(C1))
# print(C1)

# """
# Parent/Super    Class
#
# Child/Sub/Derived Class
#
# Hybrid Inheritance:
# Case 1 as shared in painting:
# """
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3(C1):
#     def __init__(self):
#         self.e=5
#         self.f=6
#         super().__init__()
#     # def showData(self):
#     #     print("I am in Class C3")
# class C4(C2,C3):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# obj=C4()
# print(obj.a,obj.b,obj.c,obj.d,obj.e,obj.f,obj.g,obj.h)
# obj.showData()


"""
Hybrid Inheritance:
Case 2 as shared in the painting:
"""
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     # def showData(self):
#     #     print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3:
#     def __init__(self):
#         self.e=5
#         self.f=6
#     def showData(self):
#         print("I am in Class C3")
# class C4(C2,C3):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# obj=C4()
# print(obj.a,obj.b,obj.c,obj.d,obj.e,obj.f,obj.g,obj.h)
# obj.showData()
# print(C4.__mro__)
# print(C3.__mro__)

"""
In most of the programming languages, Python, Java, C, PHP..
all classes (user defined or predefined) have one common parent
class ie object class.
object class is the parent to all user defined and pre defined
classes
"""
# #New Program
# L1=[2,3,4]

"""
Let's see one method of object class. 
Method name is __str__
Very....powerful method. This method decided when we print
an identifier or variable or function or class or object then
what data to print on the screen.
Sometimes we see values are printed on screen using print
function, sometimes address are printed and sometimes some
other text is printed, how this is possible using __str__
method.

Whenever we use print function in our program, then this
function firstly call __str__ method on all its arguments.
And whatever value is returned from this method is actually
printed on the screen

a=5
L=[10,20,30]
print(a,L)
then how above print statement will work.
Firstly print will call __str__ method on a as well L.
a.__str__()
L.__str__()
Now whatever output comes from above two methods is actually
printed on the screen
this __str__ method always returns string type of data.
So in python both input and print function always works on
string type of data.
"""
# #New Program
# a=5
# L=[10,20,30]
# a_intermediate=a.__str__()
# L_intermediate=L.__str__()
# print(type(a_intermediate))
# print(type(L_intermediate))
# print(a_intermediate)
# print(L_intermediate)

# #New Program
# class C1:
#     def __str__(self):
#         return "CETPA"
# obj=C1()
# print(obj)      #Actually obj.__str__()

# #New Program
# for i in range(5):
#     print(i)

# #New Program
# r=range(5)
# print(type(r))
# print(r)        #r.__str__()

"""
Polymorphism: 
Overloading: is also called compile time polymorphism

Overriding: is also called run time polymorphism

"""

"""
Try to make a project on Inheritance:

HRMS: Human Resource Management System means Employee Management
System

3 types of employees
1. SalesManager: 
id,name,age,mob,salary,territory

2. Trainer
id,name,age,mob,salary,technology

3. Director
id,name,age,mob,salary,share

Hierarchical Inheritance:
Employee Class is the Parent to SalesManager Class, Trainer Class
and Director Class. One Parent and 3 Children.
Employee Class Variables: id,name,age,mob,salary
Director Class Variable: Variables of Employee Class + Shares
..
..

"""

"""
Access Specifiers: 3 types
Are used to specify variables or functions.

Following is the Real definition of access specifiers as per 
OOPS concepts used in C++ or Java or other:
Public: Can be accessed anywhere in itself or child or outside class
Protected: Can be accessed only in itself or in child class
Private: Can be accessed only in itself.

But in Python provisions are made to make 3 types of access 
specifiers but these all types of variables or methods can be 
accessed anywhere in the program.

Python works on belief based system.
Public Variable or method: Make it directly as we made till now.
Protected: Add extra underscore before variable or function name
self._a=5, but Python says that this extra underscore is just to
inform other developers that this is a protected variable and try
not to use it outside parent or child class, still if you want to
use it, no issues, use it.

Private: Add two  extra underscores before variable or function name
self.__a=5, but Python says that these extra underscore is just to
inform other developers that this is a private variable and try
not to use it outside parent class, still if you want to
use it, no issues, use it but you need to a follow a different 
syntax to access it outside ie obj_name._Class_Name__variable_name
"""
# #New Program
# class C1:
#     def __init__(self):
#         self._a=5       #Protected variable
# obj=C1()
# print(obj._a)

# #New Program
# class C1:
#     def __init__(self):
#         self.__a=5       #Private variable
# obj=C1()
# # print(obj.__a)          #AttributeError: 'C1' object has no attribute '__a'
# print(obj._C1__a)

"""
No Practise means No Learning
"""





