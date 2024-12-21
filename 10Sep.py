""
"""

"""
# #New Program
# L=[]
# e=10
# L.append(e)
# print(L)
# e=20
# L.append(e)
# print(L)


# #New Program
# #BLL
# def checkPrime(no):     #no=35, 37
#     L=[]
#     for i in range(2, no):  # i=2, 3,4,5,...34 no=35
#         if (no % i == 0):
#             break
#     else:
#         L.append(no)        #L=[7,11]
#     return L
#
# #PL
# no=int(input("Enter Any No:"))       #no=35
# res=checkPrime(no)
# print(res)


# #New Program: Check all Prime nos and store in a given list
# #BLL
# def checkAllPrime(no_low,no_high):
#     L=[]
#     for no in range(no_low,no_high+1):        #no=7,8,9,...13
#         for i in range(2, no):  # i=2, 3,4,5,6, no=7
#             if (no % i == 0):
#                 break
#         else:
#             L.append(no)        #L=[7,11]
#     return L
#
# #PL
# no_low=int(input("Enter lower limit:"))      #7
# no_high=int(input("Enter higher limit:"))    #13
# res=checkAllPrime(no_low,no_high)
# print("The Prime Nos are:",res)



# #New Program
# #BLL
# def checkPrime(a,b):     #a=5, b=15
#     L=[]
#     for no in range(a,b+1):     #5 to 15
#         for i in range(2, no):  # i=2, 3,4,5,...34 no=35
#             if (no % i == 0):
#                 break
#         else:
#             L.append(no)        #L=[7,11]
#     return L
#
# #PL
# no_a=int(input("Enter lower value:"))       #no_a=5
# no_b=int(input("Enter upper value:"))       #no_b=15
# res=checkPrime(no_a,no_b)
# print(res)

# #New Program
# def func():
#     pass
# r=func()
# print(r)

# #New Program
# s="cetpa"
# r=s.upper()
# print(r)

# #New Program
# L1=[10,20,30]
# L2=L1.append(40)
# print(L2, L1)

# #New Program
# """
# s="adfda"
# """

# #New Program
# s="CETPA"
# for e in s:
#     print(e)


# # #New Program
# s="cetpa infotech"
# r=s.replace("e","*")
# print(r)

"""
one more doubt from assignment 8. 
Write a Python program to swap commas and dots in a string. 
Sample string: "127.0.34,1" Expected Output: "127,0,34.1"
"""
# #New Program
# s="127.0.34,1"
# print(s)
# r=s.replace(".","*")
# print(r)
# r=r.replace(",",".")
# print(r)
# r=r.replace("*",",")
# print(r)

# #New Program
# s="abcde efdbe"     #d to be replaced by *
# print(s)
# r=s[:3]+"*"+s[4:]     #"abc*e efdbe"
# print(r)
# r=r[:8]+"*"+r[9:]
# print(r)

# #New Program
# s="abcde efdbe"     #d to be replaced by *
# print(s)
# ele1="d"
# ele2="*"
# i=3         #d is there ie ele1 is there at 3 index
# r=s[:i]+ele2+s[i+1:]     #"abc*e efdbe"# r=s[:3]+"*"+s[4:]     #"abc*e efdbe"
# print(r)
# r=r[:8]+"*"+r[9:]
# print(r)




"""
Create your own replace method
"""
# #New Program
# def myReplace(s,ele1,ele2):  #s="abcde efdbe", ele1="d",ele2="*"
#     for i in range(len(s)):     #range(11), i=0,1,2,....10
#         if(s[i]==ele1):     #i=0,"a"=="d"; i=1,"b"=="d", i=2,"c"=="d", i=3,i=0,"d"=="d"
#             s=s[:i]+ele2+s[i+1:]
#     return s
#
#
# #PL
# s=input("Enter Any string:")        # s="abcde efdbe"     #d to be replaced by *
# ele1=input("Enter character to be replaced:")   #"d"
# ele2=input("Enter character to replace other character:") #*
# res=myReplace(s,ele1,ele2)
# print("The modified string is",res)

"""
Practice jarrooooooooor kar lena
"""

"""List Methods

"""
# #New Program
# L=[10,20,30]
# print(id(L))
# L.append(40)
# print(L)
# print(id(L))

# #New Program
# L=[10,20,30]
# print(id(L))
# L[0]=100
# print(L)
# print(id(L))

# #New Programm
# L=[10,20,30]
# L.extend(40)        #Error: Extend method works on iterator
# print(L)


# #New Programm
# L=[10,20,30]
# L.append("ABC")
# print(L)
# L=[10,20,30]
# L.extend("ABC")
# print(L)

# #New Programm
# L=[10,20,30]
# L.append([100,200,300])
# print(L)
# L=[10,20,30]
# L.extend([100,200,300])
# print(L)

# #New Program
# L=[10,20,30]
# L.append(40)
# print(L)

# #New Program
# L=[10,20,30]
# L.append([20,30,40])
# print(L)
# print(L[0])
# print(L[3])

# #New Program
# L=[10,20,30]
# L.extend([20,30,40])
# print(L)

# #New Program
# L=[10,20,30]
# L.insert(1,100)
# print(L)

# #New Program
# L=[10,20,30]
# L.insert(0,100)
# print(L)



# #New Program
# L=[10,20,30,20]
# ele=20
# L.remove(ele)       #First Matching element
# print(L)

"""
Remove all matching elements in a list
"""

# #New Program
# L=[10,20,30]
# r=L.pop()
# print(L)
# print(r)

# #New Program
# L=[10,20,30]
# r=L.pop(1)      #index is optional to pass
# print(L)
# print(r)

# #New Program
# L=[10,20,30,40,50,60]
# i=2
# L.pop(i)
# print(L)

# #New Program
# L=[10,20,30,20,40]
# ele=20
# r=L.count(ele)
# print(r)
# print(L)

# #New Program
# L=[10,20,30]
# print(id(L))
# L1=L.copy()
# print(id(L1))
# print(L,L1)

# #New Program
# L=[10,20,30,20]
# ele=20
# i=L.index(ele)      #First Matching elelemt ka index print karta hai
# print(i)

# #New Program
# L=[10,20,30,40,20,15,19,11]
# L.sort()
# print(L)

# #New Program
# L=[10,50,20,30,40,20,15,19,11]
# L.sort(reverse=True)
# print(L)

# #New Program
# L=[10,20,30]
# print(id(L))
# L.clear()
# print(L)
# print(id(L))

# #New Program
# L=[10,20,30]
# L.reverse()
# print(L)

# #New Program
# L=[10,20,30]
# r=L.__len__()
# print(r)

"""

"""
# #New Program
# L1=[10,20,30]
# L2=L1.clear()
# print(L2)
# print(L1)

"""
First Project: Basic Model: 
4 Basic Operations: CRUD Operations

CRUD: Create, Read, Update, Delete

CRM: Customer Relationship Management 

CMS: Customer Management System

World's most popular CRM: Salesforce

CRUD: Create, Read, Update, Delete

Customer Management System: CMS
Basic Operations:
1. How to Add a Customer
2. How to Search a Customer
3. How to Delete a Customer
4. How to Update a Customer
Next:
5. Display all Customers

Customer Parameters: id,name,age,mob
4 Lists:
id_list=[]
name_list=[]
age_list=[]
mob_list=[]

"""
# #New Program
# L=[10,20,30]
# i=1
# ele=100
# L[i]=ele        #L[1]=100
# print(L)

"""

"""

