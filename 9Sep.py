""
"""
user_list=['10', '20', '30', '40', '50']
i=0
user_list[i]=int(user_list[i])      #user_list[0]=int("10")

"""

# #New Program
# user_input = input("Enter the number with separated space:")    #"10 20 30 40 50"
# user_list = user_input.split() # convert into list, ["10","20"...
# print(user_list)
# for i in range(len(user_list)):     #i=0,1,2,3,4
# # convert each element into integer
#     user_list[i]= int(user_list[i])     #user_list[i]: "10"
# print("No are:",user_list)


# r =0
# for x in range(len(user_list)+1): #i=1, 2...7
# if(x==5):
# continue
# t=x**2 #t=1sq, 2sq # r=r+t #r=0+1sq=1sq, r=1sq+2sq, 1sq+2sq+...7sq


# #New Program
# L1=[10,20,30]       #index 0,1,2
# L2=[100,200,300]    #index 0,1,2
# L3=[30,40,50]       #index 0,1,2
# for i in range(len(L1)):      #range(3), i=0,1,2
#     print(L1[i]+L2[i]+L3[i])

# #New Program
# id_list=[10,20,30]                      #index=0,1,2
# name_list=["Vikas","Anil","Amit"]       #index=0,1,2
# age_list=[39,41,45]                     #index=0,1,2
# for i in range(len(id_list)):       #range(3), i=0,1,2
#     print("Cust ID:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i])

"""
Umesh: Projects in Python:
Python:
1. Management System: Customer Management System
I request you: Student Management System
2. Virtual Assistant
3. Language Translator:
Parallely: Search on Github and try to make few projects on your own and
discuss the problems with me.

DA:

ML:
"""

"""
Nested Loops: Loop inside loop
"""
# #New Program
# L1=[10,20,30,40]
# L2=[60,70,80]
# for e1 in L1:
#     for e2 in L2:
#         print(e1,e2)

# #New Program
# L=[ [10,20], [30,40], [50,60]  ]   #3 elements
# for e in L:     #   e=[10,20], e=[30,40]
#     print(e)
#     for a in e: # a=10, 20
#         print(a)



# #New Program
# L=[ [10,20], [30,40], [50,60]  ]   #3 elements
# print(L[0])
# a=L[0]          #a=[10,20]
# print(a[0])     #10
# print(L[0][0])
# print(L[2][0])

"""
Check whether a number input by user is a Prime no or not?
"""
#BLL
def checkPrime(no):     #no=11
    for i in range(2,no):       #i=2, 3
        if(no%i==0):
            return "not Prime"
    return "Prime"
# #PL
# no=int(input("Enter any number:"))      #no=9
# res=checkPrime(no)
# print("The entered no is:",res)

# #Find all the primary and non-primary numbers in a given limit:
# no_low=int(input("Enter lower limit:"))      #7
# no_high=int(input("Enter higher limit:"))    #13
# for no in range(no_low,no_high+1):  #no=7 to 13
#     res=checkPrime(no)
#     print("The no",no,"is",res)

# #New Program: Check all Prime nos in a given list
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

"""
Please practise jarror kar lena
"""

"""
*
**
***
****
*****
Step 1: No of lines:5, so exteranl loop will run for 5 times
n=5
for i in range(5):
Step 2:
Table:
i   n       j_range
0   5       1
1   5       2
2   5       3
3   5       4
4   5       5
no Python, maths starts:
Find relation between j_range and i and n:
j_range=i+1
 

"""
# #New Program
# for i in range(5):          #i=0, i=1
#     for j in range(4):      #i=0,j=0,1,2,3  i=1,j=0,1,2,3
#         print("*",end="")
#     print()

# #New Program
# for i in range(5):          #i=0, i=1,...4
#     for j in range(i+1):
#         print("*",end="")
#     print()

# #New Program
# n=int(input("Enter No of Lines:"))      #n=7
# for i in range(n):          #i=0, i=1,...4..6
#     for j in range(i+1):
#         print("*",end="")
#     print()


"""
*****
****
***
**
*
n=5
i       n       j_range
0       5       5
1       5       4
2       5       3
3       5       2
4       5       1
j_range=n-i


"""
# #New Program
# n=int(input("Enter no of lines:"))      #n=7
# for i in range(n):          #i=0 to 6,n=7
#     for j in range(n-i):
#         print("*",end="")
#     print()


"""
    *
   **
  ***
 ****
*****
n=5
i       n       j_range     k_range
0       5       4           1
1       5       3           2
2       5       2           3
3       5       1           4
4       5       0           5
j_range=n-i-1
k_range=i+1    

"""
# #New Program
# n=5
# for i in range(n):      #i=0,1,....4
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()

"""
    *
   ***
  *****
 *******
*********
n=5
i       n       j_range     k_range
0       5       4           1
1       5       3           3
2       5       2           5
3       5       1           7
4       5       0           9
j_range=n-i-1
k_range=2*i+1    
k=
"""
# #New Program
# n=5
# for i in range(n):      #i=0,1,....4
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()

