""
"""
Any doubt:



"""
# #New Program
# r="CETPA123"
# print(r.isalnum())

"""
To create our own count function.

"""
# #New Program
# L=["Aman","Umesh","Aman","Umesh","Harshit","Tanya"]
# print(L.count("Umesh"))



# #New Program: Count Function
# #BLL
# def myCount(s,ele):     #s='Welcome to Cetpa', ele='e'
#     count=0
#     for e in s:         #e='W','e'
#         if(e==ele):
#             count+=1        #count=count+1
#     return count
# #PL
# s=input("Enter Any String:")    #'Welcome to Cetpa'
# ele=input("Enter the element:") #ele='e'
# n=myCount(s,ele)        #s.count(ele), L1.append(40)
# print(ele,"is present in list",n,"times")

#asq+bsq+csq!=(a+b+c)sq

# #New Program: WAP to find the sum of square of even elements of a list
# L=[2,5,7,11,14,9,8]     #4+196+64,
# res=0
# for e in L:         #e=2
#     if(e%2 == 0):
#         t=e**2
#         res=res + t
# print(res)


# #New Program
# L=[10,20,30]
# res=0
# res=res+L[0]        #res=10
# res=res+L[1]        #res=10+20
# res=res+L[2]        #res=10+20+30
# print(res)
# L=[10,20,30]
# res=0
# for e in L:
#     res=res+e
# print(res)

"""
break and continue keywords
break: to stop the loop at some particular iteration
continue: to skip the particular iteration

No Practise means no learning:
Again I m requesting, weekend aane wala hai, Delhi ke malls bade
sundar hai, please apne mun ke chhakar mai weekend waste mat
kar dena.
"""
# #1sq+2sq+3sq+4sq+5sq+6sq+7sq
# r=0                         #r=0
# for i in range(1,8):        #i=1, 2...7
#     t=i**2                  #t=1sq, 2sq
#     r=r+t                   #r=0+1sq=1sq, r=1sq+2sq,  1sq+2sq+...7sq
# print(r)

# #New Program
# #1sq+2sq+3sq+5sq+6sq+7sq
# r=0                         #r=0
# for i in range(1,8):        #i=1, 2...7
#     if(i==4):
#         continue
#     t=i**2                  #t=1sq, 2sq
#     r=r+t                   #r=0+1sq=1sq, r=1sq+2sq,  1sq+2sq+...7sq
# print(r)

# #I run the loop 10 times and want to stop at iteration 5
# for i in range(10):     #0 to 9
#     if(i==5):
#         break
#     print(i)


# #New Program
# L=[10,20,98,77,66,30,40,50,60,70,90,110,]
# ele=50
# for e in L:
#     if(e==ele):
#         break
#     print(e)

# #New Program
# L=["Prashant","Hritik","Umesh","Manoj","Kajal","Jahnvi"]
# for i in range(len(L)): #range(6), i=0 to 5
#     if(i==3):
#         break
#     print(L[i])

"""
In Python, even we can use else with loop.
else is executed only if loop is executed completely without break
"""
# for i in range(5):      #Lower bound=0, upper bound=5, step size=1
#     print("Loop1",i)
# else:
#     print("Loop1 Completed")
#
# for i in range(5):
#     if(i==2):
#         break
#     print("Loop2",i)
# else:
#     print("Loop2 Completed")

"""
While Loop: Similar to for loop with different syntax
Python while loop is similar to C Lang while loop with minute
syntax difference.
Syntax:
index initialize
while(condition):       #If condition is True, loop will run, else loop will stop
    set of statements
    increment or decrement index


for i in range(n):  #lower bound=0, upper bound=n, step size=1
    print(i)        #range(0,n,1)
    
while in place of for loop above, will be as follows
i=0     #i=lower bound
while(i<n):     #while(i<upper bound):
    set of statement
    i+=1        #i+=step_size
    
3 ka table print: range(3,31,3)
i=3
while(i<31):
    print(i)
    i+=3

In Python, as per my experience or as per syntax, its
better to use for loop but we use while loop for running infintite
loop.
for loop:
1. for loop will work directly on any iterator.
2. for loop is having simple or less line of syntax

while loop:
1. used to execute infinite loop
2. Can also work on float lower, upper bounds or step size

range class works only on integer arguments ie in for loop,
lower bound, upper bound and step size should be of int type only
"""
# #New Program
# for i in range(1.1,1.7,0.1):
#     print(i)

# #New Program
# i=1.1
# while(i<1.7):
#     print(i)
#     i+=0.1      #i=i+0.1

# len(5)      #Length function works only on iterator

# #New Program
# while(1):       #while(True): Infinte Loop, whiile(-1.97):
#     print("CETPA")

"""
False values in Python
0
None
False
Empty values lie [], {}, ""....

Rest all values are True

"""


# #New Program
# #BLL
# import math
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def pow(a,b):
#     return a**b
#
# #PL
# print("Welcome to Harshit's Calculator")
# while(1):
#     no1=int(input("Enter First No:"))
#     no2=int(input("Enter Second No:"))
#     choice=input("Enter Any operation +,-,*,/,pow,log,exit:")
#     if(choice=="+"):
#         res=add(no1,no2)
#         print("Result:",res)
#     elif(choice=="-"):
#         res = sub(no1, no2)
#         print("Result:", res)
#     elif(choice=="*"):
#         res = mul(no1, no2)
#         print("Result:", res)
#     elif(choice=="/"):
#         res = div(no1, no2)
#         print("Result:", res)
#     elif(choice=="pow"):
#         res = pow(no1, no2)
#         print("Result:", res)
#     elif(choice=="log"):
#         res = math.log(no1,no2)
#         print("Result:", res)
#     elif(choice=="exit"):
#         print("Thanks for using Harshit's Calci")
#         break
#     else:
#         print("Incorrect Choice")

"""
Nested Loops:


"""

# #New Program
# #BLL
# import math
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def pow(a,b):
#     return a**b
#
# #PL
# print("Welcome to Harshit's Calculator")
# while(1):
#     pwd=input("Enter the Password:")
#     if(pwd=="akshat"):
#         print("Correct Password")
#         while(1):
#             no1=int(input("Enter First No:"))
#             no2=int(input("Enter Second No:"))
#             choice=input("Enter Any operation +,-,*,/,pow,log,exit:")
#             if(choice=="+"):
#                 res=add(no1,no2)
#                 print("Result:",res)
#             elif(choice=="-"):
#                 res = sub(no1, no2)
#                 print("Result:", res)
#             elif(choice=="*"):
#                 res = mul(no1, no2)
#                 print("Result:", res)
#             elif(choice=="/"):
#                 res = div(no1, no2)
#                 print("Result:", res)
#             elif(choice=="pow"):
#                 res = pow(no1, no2)
#                 print("Result:", res)
#             elif(choice=="log"):
#                 res = math.log(no1,no2)
#                 print("Result:", res)
#             elif(choice=="exit"):
#                 print("Thanks for using Harshit's Calci")
#                 break
#             else:
#                 print("Incorrect Choice")
#     else:
#         print("Incorrect Password, Try Again")

"""
Nested loop: Loop inside loop:

if outer loop runs n times and inner loop runs m times then
statements inside inner loop wil run n*m times
"""
# for i in range(5):      #i=0, i=1
#     for j in range(3):  #j=0,1,2,   j=0,1,2
#         print("CETPA")      #5*3 ie 15 times CETPA will be printed
#         print(i,j)












