""
"""
Fibonacci Series:
Print the Fibonacci series in single line with 50 elements like as follows 
1, 1, 2, 3, 5, 8, 13, 21…….. 
a=1
b=2

a=1
b=2
print(b)
a,b=b,a+b       #,temp=a=1, a=b=2 ,b=temp+b=1+2
a=2
b=3
a,b  =b,a+b





"""
# #New Program
# i,j=0,1         #i,j=1,1,    #i,j=1,2   #i,j=2,3
# for k in range(50):   #0 to 49
#     print(j)              #1,       2
#     i,j=j,i+j


"""
Write a program to check whether a number input by the 
user is a palindrome or not.
1489841    n=7//2= 3
"""
# #New Program
# no=input("Enter Any Number:")       #"1489841"
# for i in range(len(no)//2):     #range(3), 0,1,2
#     if(no[i]!=no[-i-1]):     #no[0]!=no[-1]
#         print("The entered no is not palindrome")
#         break
# else:
#     print("The entered no is palindrome")

"""
Categories of Functions:
1. Required Argument Functions: Where the no of arguments
and sequence of arguments should match in formal and actual.
Till now all functions we created, were required argument
type
2. Keyword Argument Functions: Where the no of arguments
should be same in formal and actual but there position
can vary.
while calling, we mention formal_var_name=actual_var_name 
3. Default Argument Functions: Where we assign a default
value to a variable. Now while calling, if we pass the
value in actual then new values is used otherwise
default value is used.
4. Variable Length Argument Functions (Tuple Based):
In formal parameter, we add one extra star immediately
before variable name. Python recommends that the formal
variable name should be 'args' in case of variable length argument
functions
5. Variable Length Keyword Argument Functions (Dictionary Based):
In formal parameter, we add two extra stars immediately
before variable name. Python recommends that the formal
variable name should be 'kwargs' in case of variable length 
keyword argument functions
6. Lambda Functions: Anonymous Functions:
Lambda functions are single liner anonymous functions.
lambda arguments_passed:expression_calculated&returned 
"""
#1. Formal Arguments
# #New Program
# def add(a,b):
#     return a+b
#
# u,v,w=5,7,9
# s1=add(u,v,w)       #Error
# print(s1)


# #New Program
# def add(a,b):
#     return a+b
# u=5
# s1=add(u)       #Error
# print(s1)

# #2. Keyword Arguments       #addCustomer(id=id,name=name...)
# def sub(a,b):
#     return a-b
# u,v=5,7         #u-v
# r=sub(b=v,a=u)
# print(r)


# #3. Default Arguments
# def add(a=1,b=2):
#     return a+b
# r1=add()        #r1=3
# r2=add(5)       #r2=7
# r3=add(b=9)     #r3=10
# r4=add(5,7) #r4=12
# r5=add(b=8,a=2) #r5=10
# print(r1,r2,r3,r4,r5)


#4. Variable Length Argument Functions (Tuple Based):
# #New Program
# def func1(*t):      #Formal Variable name is t
#     print(t)
# func1(2,3,4)
# func1(10,20,30,40,50,60)
# func1()

# #New Program
# def func1(*args):
#     print(args)
# func1(2,3,4)
# func1(10,20,30,40,50,60)
# func1()


#New Program: Generalized add function which can
#add any no of variables/data/actual
# #BLL
# def add(*args):     #args=(2, 3, 4, 5, 6)
#     r=0
#     for e in args:
#         r=r+e
#     return r
# #PL
# r1=add(2,3,4,5,6)
# r2=add(1,2)
# print(r1,r2)

#
# #BLL
# def add(*args):     #args=(2, 3, 4, 5, 6)
#     r=0
#     for i in range(len(args)):
#         r=r+args[i]
#     return r
# #PL
# r1=add(2,3,4,5,6)
# r2=add(1,2)
# print(r1,r2)


#5. Variable Length Keyword Argument Functions (Dictionary Based):
# #New Program
# def func1(**d):
#     print(d)
# u,v,w,x,y,z=2,3,4,5,6,7
# func1(a=u,b=v,c=w)
# func1(m=w,n=x,p=z,q=u)
# func1()


# #New Program
# def add(**kwargs):
#     r=0
#     for e in kwargs.values():
#         r=r+e
#     return r
#
# r1=add(a=5,b=7,c=9)
# r2=add(a=1,b=2,c=3,d=4,e=5)
# r3=add()
# print(r1,r2,r3)


# #New Program
# def func1():        #func1 address 1000
#     print("CETPA")
# print(func1)
# def func1():        #func1 address 2000
#     print("Welcome")
# print(func1)
# func1()
# print(type(func1))


# #New Program
# x=5         #x address 1000
# x=7         #x address 2000
# print(x)
# print(type(x))      #object of int class

# #New Program
# def add(u,v):            #add address 1000
#     return u+v
#
# a=add     #a address 1000, here a is called function pointer
# r1=a(5,7)
# print(r1)
# r2=add(5,7)
# print(r2)


"""
Function Pointer: Function pointer is a variable
which holds the address of a function.
def func1():
    pass
    
a=func1()
here a is a function pointer which is holding the 
address of a function.

In case of anonymous function we save the address
of function in a variable and access that function
through that variable (function pointer) name only

lambda arguments_passed:expression_calculated&returned

"""
# print(lambda a,b:a+b)

# #New Program
# a=lambda a,b:a+b        #a is a funciton pointer
# r=a(5,7)
# print(r)

#New Program
add=lambda a,b:a+b        #a is a funciton pointer
r=add(5,7)
print(r)