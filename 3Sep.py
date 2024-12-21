""
"""
First Thing First: 
Variable: Whose value varies in the program
Why we copy variable in another variable? To create backup of old
variable value.
"""
# #New Program
# a=5         #a address 1000
# b=a         #b address 1000
# a=7         #a address 2000
# print(b)    #data of address 1000
# a="CETPA"
# b=a
# a="METPA"
# print(b)

# #New Program
# a=[10,20,30]    #a address 1000
# b=a             #b address 1000, all variables are of ref type
# a=[80,20,30]    #a address 2000, b address 1000, Python supports dynamic memory allocation
# print(b)        #[10,20,30]
# a="CETPA"       #a address 3000, Python supports dynamic memory allocation
# print(b)

"""
In mutable type variables if we modify the elements of list
then base address of list doesn't change
"""
# #New Program
# L1=[10,20,30]       #L1 address 1000
# L2=L1               #L2 address 1000
# L1[0]=80            #L1 address 1000
# print(L2)
# print(L1)

# #New Program
# s="CETPA"
# s[0]="M"        #Error, string is immutable

# #New Program
# s="CETPA"       #s address 1000
# print(s,id(s))
# s="M" + s[1:]   #s address 2000
# print(s,id(s))

# #New Program
# L1=[10,20,30]
# L2=L1
# L1[0]=80
# print(L2)

"""
copy method created the copy of the list but at a different base 
address
"""
# #New Program
# L1=[10,20,30]
# L2=L1       #
# print(id(L1),id(L2))


# #New Program
# L1=[10,20,30]
# print(id(L1))
# L2=L1.copy()
# print(id(L2))
# print(L1,L2)
# L1[0]=80
# print(L1,L2)

"""
Till now we have discussed functions in python: 
How to call a function: 
function_name(arguments)
Above functions are created outside class.

Next Concept after few python sessions, we will study about 'Class'
concept in python.
Class is a collection of variables and functions(methods)
How to call a function, created inside class: 
Syntax:
obj_name.method_name(arguments)

"""
# #New Program
# s="Cetpa"
# r=s.upper()     #Upper function is created inside str class
# print(r)


# #New Program
# L1=["ab","cd"]
# L2=L1.upper()       #AttributeError: 'list' object has no attribute 'upper'
# print(L2)

# #New Program
# L1=[10,20,30]
# L2=L1.copy()

"""
Functions: 
"""
# #New Program
# def func1(L1):      #L1 address, L1 is Banti
#     L1[0]=80        #L1 address 1000
#
# L2=[10,20,30]       #L2 address 1000, L2 is Vikas
# func1(L2)           #L1=L2, L1 address 1000
# print(L2)



# #New Program
# def func1(L1):      #L1 address, L1 is Banti
#     L1[0]=80        #L1 address 1000
#
# L2=[10,20,30]       #L2 address 1000, L2 is Vikas
# func1(L2)           #L1=L2, L1 address 1000
# print(L2)
# print(L1)           #Error: L1 is local variable


# #New Program
# def func1(L1):      #L1 address, L1 is Banti
#     L1[0]=80        #L1 address 1000
#
# L2=[10,20,30]       #L2 address 1000, L2 is Vikas
# res=func1(L2)           #L1=L2, L1 address 1000
# print(res)
# print(L2)

# #New Program
# def func1(L1):      #L1 address, L1 is Banti
#     L1[0]=80        #L1 address 1000
#     return
# L2=[10,20,30]       #L2 address 1000, L2 is Vikas
# res=func1(L2)           #L1=L2, L1 address 1000
# print(res)
# print(L2)

"""
String methods

How to call a method (function inside class):
obj_name.function_name(arguments)
obj_name.method_name(arguments)
"""
# #New Program
# s="Welcome To CETPA"
# r=s.lower()
# print(r)


"""
index and find methods: Returns the index of the element or
substring. By default returns index of first matching element

s="Welcome" #index 0 to 6
"""
# #New Program
# s="Welcome to Cetpa"        #
# ele="t"
# index=s.index(ele)
# print(index)

# #New Program
# s="Welcome to Cetpa"
# i=s.index("e",3)
# print(i)

"""
Upper bound is discarded in index and find method

Gaurav: What is difference between find and index
In index method if element/substring is not found then we get
the error: ValueError: substring not found

In find method if element/substring is not found then we get
-1: 
 
"""
# #New Program
# s="Welcome to Cetpa"
# i=s.index("e",3,6)      #will search between 3 to 5 index including 3 and 5
# print(i)

"""
HW: Study for 10 minutes about different CMMI Levels
"""

# #New Program
# s="Welcome to Cetpa. Cetpa is a CMMI Level 5 Company"
# i=s.index("Cetpa")
# print(i)

# #New Program
# s="Welcome to Cetpa. Cetpa is a CMMI Level 5 Company"
# i=s.find("Cetpa")
# print(i)

"""




"""


# #New Program
# cus_list=["Vikas","Gaurav","Prashant","Roshni","Janhvi","Kajal"]
# cus=input("Enter Cust Name:")       #"Kajal
# i=cus_list.index(cus)
# print(i)

# #New Program
# s="Welcome to CETPA"
# r=s.find("z")
# print(r)

"""
Akash:
Why index in programming starts with 0 ie in real life we
say 1st element and in programming we say 0th element
Because these indices, represents the array addresses ie
indirectly represents the memory addresses.
Memory addresses starts with 0 ie actually they starts with
binary numbers. If you have a memory of 3 bits then how many
total memory elements or memory addresses will be there?
8 addresses: Starting from 0 to 7
000 :   0
001 :   1
010
011
100
101
110
111 :   7
Why with 0 because in binary we have two numbers only ie 0 and 1
0 represents 0 volt and 1 represent 5 volt these are the
voltage levels in the background.
"""

"""
There is one small difference in most of the string and list
methods.
String methods, when called, returns new string
list methods, when called, change the original list
"""
# #New Program
# s1="Cetpa"
# s2=s1.upper()
# print(s2,s1)
# #New Program
# L1=[10,20,30]
# L2=L1.append(40)
# print(L2,L1)

"""
If we have 'is' in starting of any method, then method will
return bool value ie True or False
"""
# #New Program
# s="9212468020"
# r=s.isdecimal()
# print(r)

# #New Program
# s=9212468020
# r=s.isdecimal()     #Error  :   AttributeError: 'int' object has no attribute 'isdecimal'
# print(r)

"""
idecimal method: checks whether all the elements of strings
are whole numbers or not
"""

# #New Program
# mob=input("Enter Your Mob No:")
# res=mob.isdecimal()
# if(res==True and len(mob)==10):
#     print("The Correct format mobile no")
# else:
#     print("Incorrect format mobile no")

# #New Program
# s="Welcome"
# r=s.isalpha()   #Checks all alphabets or not
# print(r)


# #New Program
# s="Welcome123"
# r=s.isalnum()       #Alphabets and numbers
# print(r)

# #New Program
# s="Welcome 123"
# r=s.isalnum()       #Alphabets and numbers
# print(r)

# #New Program
# s="Welcome 123"
# r=s.count("z")
# print(r)

# #New Program
# s="Welcome 123m"
# r=s.replace("m","***")
# print(r)

# #New Program
# s="Cetpa"
# r=s.replace("C","M")
# print(r)

# #New Program
# s="Cetpa123"
# r=s.swapcase()
# print(r)

"""
strip method: Removes spaces in the starting and end of the 
string
"""
# #New Program
# s="   Welcome to Cetpa123  "
# print(len(s),s)
# r=s.strip()
# print(len(r),r)


"""
Kasam 5: Always use strip method with input function
"""
# #New Program
# s=input("Enter Your Name:").strip()
# print(s,len(s))

# #New Program
# s="Vikas      Kalra"
# r=s.replace(" ","")
# print(r)



