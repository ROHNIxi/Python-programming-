""
"""
Python 
"""
# #New Program
# def func1(L1):      #L1 address, L1 is Banti
#     L1[0]=80        #L1 address 1000
#     return
# L2=[10,20,30]       #L2 address 1000, L2 is Vikas
# res=func1(L2)           #L1=L2, L1 address 1000
# print(res)
# print(L2)


"""
Function:
def function_name(arguments):
        set of statements
        return argument (Optional)

Formal and actual parameters can have same or different names
#BLL
# def len(a):
#     Block of code to calculate length
#     return length
# 
# #PL
# s="CETPA"
# n=len(s)
# print(n)


# #New Program
# import operator
# 
# 
# a,b=5,7
# r=operator.add(a,b)
# print(r)


# #New Program
# def add(a,b):   #Purpose to add a and b
#     s=a+b
#     return s
# 
# a,b=5,7
# r=add(a,b)
# print(r)

Program/Computer/Microprocessor/Game/Mobile Application/Web Application:
Take the data from the user, process the data and generate the
outputs:
Take the data and generate the outputs: PL
To process the data: BLL


"""
# s="CETPA"
# n=len(s)
# print(n)

# #New Program
# no1=int(input("Enter 1st No:"))
# no2=int(input("Enter 1st No:"))
# res=no1+no2
# print("Result:",res)

# #New Program:
# #BLL
# def func1(a,b):
#     r=a+b
#     return r
#
# #PL
# no1=int(input("Enter 1st No:"))
# no2=int(input("Enter 1st No:"))
# res=func1(no1,no2)
# print("Result:",res)

"""
Manoj Question: what is the exact use of isdecimal if it can be used for string only ?
Ans:
In Python string is having around 50 different functions while
list is having around 10 different functions. Why string is having
too many numbers, because data is generally travelled in string
format. Like input is provided by user and input is always of
string type. So wherever user gives input in the program, there
are chances that user can pass incorrect or wrong data, so to
validate the correct format data, we have multiple functions in 
string format.
Still if you have say int data, you can caste it to string and then
can validate

If we want to take more than one input in python, there is
no standard way, in python input is always of string type

"""
# a=9212468020


# #New Program
# nos=input("Enter 5 numbers:")
# print(nos,type(nos),len(nos))

# #New Program
# name="Vikas*Kumar*Kalra"
# res=name.split("*")
# print(res)

# #New Program
# name="Vikas Kumar Kalra"
# res=name.split()    #By default works on space
# print(res)

# #New Program
# name=input("Enter Your Name:")
# res=name.split()    #By default works on space
# print(res)

# #New Program
# name=input("Enter Your Name:").split()
# print(name)

# #New Program
# n=input("Enter Five Numbers:").split()
# print(n)
# no0=int(n[0])
# print(no0,type(no0))

"""
Kasam No 3:
input and print, try to use in PL
"""

"""
Loops in Python: Loops are the only hurdle for new programmers.

Loop: is used to execute block of code repeatedly. 
To execute set of statements again and again.

In Python we have two types of loops:
for
while

For loop: Few people say, for loop is of 2 types but I say, its
of only 1 type but we can use same for loop in different ways.

Shiv Khera: 
Winners don't do different things, they do things differently. 

Syntax:
for element in iterator:
    set of statements to execute repeatedly
How above loop works: Everytime loop runs, one element from left
to right is retrieved from iterator and set of statements execute    
How many times loop will run by default: ie no of elements present
                                        in iterator

How loop works: Firstly loop statement run one time, then loop
inner statements run one time, then again loop run one time and 
loop inner statements one time and so on. 

iterators: str, list, tuple, dict, set, frozenset, range
"""
# #New Program
# s="CETPA"
# for e in s:
#     print("Hello")
#     print(e)

# #New Program
# L=[10,20,30,40]
# for e in L:
#     print(e)
#     print("ABC")
#     print(95)

"""
str is a data type which is made through class
list is a data type which is made through class
range is a data type which is made through class
Syntax for range object:
range(lower_bound,upper_bound,step_size)
Upper bound will be discarded in range object

To extract the elements of range object, we can type caste it 
or we can use it in loops

range is used to create set of integers in a particular series

All rules of slicing will work on range also
"""
# s="CETPA"
# print(s)
# r=range(2,10,3)
# print(r)

# #New Program
# r=range(2,10,2)
# print(r)
# L=list(r)
# print(L)

# #New Program: Table of 2
# r=range(2,21,2)
# print(list(r))

# #New Program
# L=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# for e in L:
#     print(e)

# #New Program
# for e in range(2,21,2):
#     print(e)

# #New Program
# for e in range(-2,-22,-2):
#     print(e)

# #New Program
# for i in range(22,2,2): #No output, loop won't run even for single time
#     print(i)

"""
Now few people who doesn't know the background of range class,
they say, for loop is of 2 types, one directly used on iterator
and other used on range class.

for element in iterator:
    set of statements

for i in range(arguments):
    set of statements
    
Generally range class in loops is used to run set of statement
for a fixed no of times.

range class requires at least one argument, which is called
the upper bound.
Further syntax:
range(a,n,s)    : a lower bound, n upper bound, s step size
range(a,n)      : a lower bound, n upper bound, default s = 1
range(n)        : n upper bound, default lower bound=0, default s = 1

If we want to run a loop n times: 
range(n)    : loop will run from 0 to n-1 with step size=1


"""
# for i in range():       #Error
#     print(i)

# #New Program
# for i in range(5):       #lower bound=0, upper bound=5, step size=1
#     print(i)

# #New Program
# for i in range(2,21,-2):
#     print(i)

"""
We want to perform some common operation on all or selected elements
of an iterator then we can use loops

Print the square of all elements of a list
"""
# #New Program
# L=[10,20,30,40,50]
# for e in L:
#     print(e**2)     #print(e*e)



# #New Program
# L=[10,20,30,40,50]
# for e in L:
#     print(e**2)     #print(e*e)
#     print(e+2)

"""
Selected elements like square the even elements of a list
"""
# #New Program
# L=[22,12,33,44,55,67,99,12]
# for e in L:
#     if(e%2==0):
#         print(e*e)

"""
Rohit wants to input the data from user.
"""
# data=input("Enter few space separated numbers:").split() #2 3 4 5, data=['2','3','4','5']
# print(data)
# for e in data:      #e="2"
#     e=int(e)        #e=2
#     if(e%2==0):
#         print(e**2)

# #New Program
# s="10 20 30 40 50"
# L=s.split()
# print(L)
# L.append(60)
# print(L)

# #New Program
# L="10 20 30 40 50".split().copy()
# print(L)

# #New Program
# print(type(len("CETPA")))   #print(type(5))

# #New Program
# res="    Welcome to CETPA    ".strip().upper()
# print(res)

"""
To access elements of an iterator in a loop, we can have 2 ways:
Directly through iterator
or using indexing with range class
"""
# #New Program
# s="CETPA"
# for e in s:
#     print(e)
#
# s="CETPA"       #index: 0 to 4, ie 0,1,2,3,4, s[0], s[1],...s[4]
# for i in range(len(s)):   #range(5): 0,1,2,3,4
#     print(s[i])


# #New Program
# L=[10,20,30,40]
# print(0,L[0])
# print(1,L[1])
# print(2,L[2])
# print(3,L[3])
#
# L=[10,20,30,40]
# for i in range(len(L)):     #range(4): i=0,1,2,3
#     print(i,L[i])       #0 L[0]    1 L[1]    2 L[2]    3 L[3]

# #New Program
# x=5
# y=5
# print(id(x),id(y))

# #New Program
# x=[10,20]
# y=[10,20]
# print(id(x),id(y))


