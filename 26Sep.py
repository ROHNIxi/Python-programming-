""
"""
Exception Handling
"""
# class Count:
#     object_count = 0
#     def __init__(self):
#         Count.object_count+= 1
#     # classmethod
#     def my_object_count(cls):
#         return cls.object_count
# #PL
# obj1 =Count()
# obj2 =Count()
# obj3 =Count()
# obj4 =Count()
# print(Count.object_count)

# #New Program
# x=5             #x address 1000
# class x:        #x address 2000
#     pass
# print(x)


"""
Advanced Python:

Exception Handling: How to handle exceptions (errors)

In real life projects, if we get errors while program execution
then program doesn't stop working or doesn't throw the error
at the output rather some error message is given and projects
keep on running. 

The target of exception handling is: Catching/Managing the errors
while program execution and try not to stop the program.

"""
# #New Program
# id_list=[10,20,30,40]
# id=int(input("Enter the ID:"))      #id=50
# i=id_list.index(id)
# print(i)

# #New Program
# ele="M"
# s="CETPA"
# i=s.index(ele)      #ValueError: substring not found
# print(i)
# #New Program
# ele=100
# L=[10,20,30,40]
# i=L.index(ele)      #ValueError: 100 is not in list
# print(i)

# #New Program
# import Module12     #ModuleNotFoundError: No module named 'Module12'
#

"""
To handle exceptions in the program there are 4 keywords designed
for exception handling. 
try: 
except:
finally:
raise:

"""
# #New Program
# x=int(input("Enter First No:"))     #ValueError: invalid literal for int() with base 10: 'cetpa'
# y=int(input("Enter Second No:"))
# res=x/y                     #ZeroDivisionError: division by zero
# print("Result:",res)

# #New Program
# while(1):
#     try:
#         x=int(input("Enter First No:"))     #ValueError: invalid literal for int() with base 10: 'cetpa'
#         y=int(input("Enter Second No:"))
#         res=x/y                     #ZeroDivisionError: division by zero
#         print("Result:",res)
#         break
#     except:
#         print("Error!")

"""
In Python we have multiple error classes for different type of 
errors examples:
ValueError
ZeroDivisionError
ModuleNotFoundError
.
.
The 'Exception' Class is the parent to all error classes.
While managing the 'except' block of code, then we can mention
the Error class name or we can mention Exception Class name which
is parent to all error classes or in case we don't mention the 
error class name then by default Exception Class is Considered.
"""
#New Program
# 5/0     #ZeroDivisionError: division by zero

#New Program
# int("$")        #ValueError: invalid literal for int() with base 10: '$'


# #New Program
# while(1):
#     try:
#         x=int(input("Enter First No:"))     #ValueError: invalid literal for int() with base 10: 'cetpa'
#         y=int(input("Enter Second No:"))
#         res=x/y                     #ZeroDivisionError: division by zero
#         print("Result:",res)
#         break
#     except ValueError:
#         print("Error! Enter whole numbers only")
#     except ZeroDivisionError:
#         print("Error! Enter Non Zero Second Input Only")
#     except Exception as err:       #Exceptional is optional word here
#         print("Error!",err)
#         print(type(err))

# #New Program
# try:
#     pr("CETPA")
# except Exception as err:
#     print("Error:",err)
#     print(type(err))


# #New Program
# while(1):
#     try:
#         x=int(input("Enter First No:"))     #ValueError: invalid literal for int() with base 10: 'cetpa'
#         y=int(input("Enter Second No:"))
#         res=x/y                     #ZeroDivisionError: division by zero
#         print("Result:",res)
#         break
#     # except ValueError as err:       #err will become the object of particular error class
#     #     print("Error!",err)
#     # except ZeroDivisionError as err:
#     #     print("Error!", err)
#     except Exception as err:       #Exceptional is optional word here
#         print("Error!",err)
#         print(type(err))


"""
Kasam No: 8
Now whenever we will create any program even to add two numbers, we
will add minimum one layer of try and except:

"""
# #New Program
# while(1):
#     try:
#         no1=int(input("Enter First No:"))
#         no2=int(input("Enter Second No:"))
#         res=no1+no2
#         print("Result:",res)
#         break
#     except Exception as err:
#         print("Error!",err)

"""
When we make the live projects then we use both the exception
handling and we use input checks using string methods or normal
program syntax
"""
# mob=int(input("Enter Mobile No:"))
# print(mob)

"""
finally keyword: 
finally is the block of code which always executes in the program
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
#     try:
#         pwd=input("Enter the Password:")
#         if(pwd=="akshat"):
#             print("Correct Password")
#             while(1):
#                 no1=int(input("Enter First No:"))
#                 no2=int(input("Enter Second No:"))
#                 choice=input("Enter Any operation +,-,*,/,pow,log:")
#                 if(choice=="+"):
#                     res=add(no1,no2)
#                     print("Result:",res)
#                 elif(choice=="-"):
#                     res = sub(no1, no2)
#                     print("Result:", res)
#                 elif(choice=="*"):
#                     res = mul(no1, no2)
#                     print("Result:", res)
#                 elif(choice=="/"):
#                     res = div(no1, no2)
#                     print("Result:", res)
#                 elif(choice=="pow"):
#                     res = pow(no1, no2)
#                     print("Result:", res)
#                 elif(choice=="log"):
#                     res = math.log(no1,no2)
#                     print("Result:", res)
#                 else:
#                     print("Incorrect Choice")
#         else:
#             print("Incorrect Password, Try Again")
#     except Exception as err:
#         print("Error!",err)
#     finally:
#         ch=input("Whether you want to continue, enter Y/N:")
#         if(ch=="N" or ch=="n"):
#             print("Thanks for using Harshit's Calci")
#             break


# #CMS
# #BLL
# class Customer:
#     cus_list=[]     #cus_list=[1000,2000,3000
#     def __init__(self): #self=1000
#         self.id=0       #1000.id=0
#         self.name=0     #1000.name=0
#         self.age=0      #1000.age=0
#         self.mob=0      #1000.mob=0
#     def addCustomer(self):  #self=1000, self.id=10,self.name="Vikas", self=2000, self.id=20
#         Customer.cus_list.append(self)
#     def searchCustomer(self):   #self=8000,self.id=20,self.name=0,self.age=0,self.mob=0
#         for e in Customer.cus_list:
#             if(e.id==self.id):
#                 self.name=e.name    #self.name="Anil", 8000.name="Anil"
#                 self.age=e.age
#                 self.mob=e.mob
#     def deleteCustomer(self):   #self=9000, self.id=30, self.name=0..
#         for e in Customer.cus_list:
#             if(e.id==self.id):
#                 Customer.cus_list.remove(e)
#                 return
#     def modifyCustomer(self):    #self=10000, self.name="Sonu", self.age=55
#         for e in Customer.cus_list:
#             if(e.id==self.id):
#                 e.name=self.name
#                 e.age=self.age
#                 e.mob=self.mob
#                 return
#



# #PL
# def showCustomer(cus):      #cus=8000
#     print("Cust ID:",cus.id,"Cust Name:",cus.name,"Cust Age:",cus.age,"Cust Mob:",cus.mob)
# print("Welcome to Tulsi's CMS")
#
# while(1):
#     try:
#         choice=input("Enter Choice:1 for Add Cust,"
#                      "2 for Search Cust, 3 for Delete Cust,"
#                      "4 for Modify Cust, 5 Display All, "
#                      "6 for Exit: ")
#         if(choice=="1"):    #Customer Add
#             try:
#                 cus=Customer()  #cus 1000, cus.id=0,cus.name,cus.age,cus.mob=0, cus=2000, cus.id=0, cus=3000, cus.id=30, 3000.id=30
#                 cus.id=int(input("Enter Cust Id:"))  #1000.id, cus.id=10, cus.id=20
#                 cus.name=input("Enter Cust Name:")  #cus.name="Vikas", 2000.name="Anil"
#                 cus.age=input("Enter Cust Age:")    #cus.age="39"
#                 cus.mob=input("Enter Cust Mob:")    #cus.mob="1234"
#                 cus.addCustomer()   #self=cus
#                 print("Customer Added Successfully")
#             except Exception as err:
#                 print("Error!",err)
#         elif(choice=="2"):   #Search Customer
#             try:
#                 cus=Customer()  #cus address 8000, cus.id=0, cus.name=0, cus.age=0,cus.mob=0
#                 cus.id=int(input("Enter Customer ID:"))  #cus.id=20
#                 cus.searchCustomer()
#                 showCustomer(cus)       #cus=8000
#             except Exception as err:
#                 print("Error!",err)
#         elif(choice=="3"):  #Delete Customer
#             try:
#                 cus=Customer()      #cus address 9000, cus.id.=0,cus.name=0
#                 cus.id=int(input("Enter cust id to delete:"))    #cus.id=30
#                 cus.deleteCustomer()
#                 print("Customer Deleted Successfully")
#             except Exception as err:
#                 print("Error!",err)
#         elif (choice == "4"):  # Modify Customer
#             cus = Customer()  # cus address 10000, cus.id.=0,cus.name=0
#             cus.id = int(input("Enter cust id to modify:"))  # cus.id=30
#             cus.name=input("Enter Cust Updated Name:")  #cus.name="Sonu"
#             cus.age = input("Enter Cust Updated Age:")  # cus.age="55"
#             cus.mob = input("Enter Cust Updated Mob:")  # cus.mob="9999"
#             cus.modifyCustomer()
#             print("Customer Modified Successfully")
#         elif (choice == "5"):  # Display All Customers
#             for e in Customer.cus_list:
#                 showCustomer(e)
#         elif (choice == "6"):  # Exit
#             print("Thanks for using Tulsi's CMS")
#             break
#         else:
#             print("Incorrect Choice")
#     except Exception as err:
#         print("Error!",err)


"""
raise keyword:
To raise ie to throw the errors/exceptions intentionally
 in the program

Syntax:
raise ErrorClass_Name(Message for user)
"""
# raise ValueError("Error!")


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

