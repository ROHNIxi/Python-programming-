""
"""

"""
# #New Program
# a,b=5,2
# r=a/b       #Division
# print(r)

"""
input function: always returns string in the program
"""
# #New Program
# name=input("Enter Cust Name:")
# print(type(name),name)
# age=input("Enter Cust Age:")        #age="39"
# print(type(age),age)

"""
Concatenation: When we use + operator on strings then it 
concatenate (join) the strings.
a="ram"
b="shyam"
r=a+b       #"ramshyam"


Addition: When we use + operator on numbers then it add the numbers.
"""

# #New Program
# a=input("Enter First No:")      #a="5"
# b=input("Enter Second No:")     #b="7"
# r=a+b                   #r="57"
# print(r)

# #New Program
# a="ram"
# b="shyam"
# r=a+b       #"ramshyam"
# print(r)

# #New Program
# a="5"
# b="7"
# r=a+b       #"57"
# print(r)
# a=5
# b=7
# r=a+b       #12
# print(r)


# #New Program
# a=input("Enter First No:")      #a="5"
# b=input("Enter Second No:")     #b="7"
# r=a+b                   #r="57"
# print(r)

"""
Mai chahe late ho jayu, lekin aap logo ne late nahi hona hai
Ek bhee lecture chhuta to guarantee kavach toota. 
"""

# #New Program: Addition of 2 numbers: Aditya
# a=input("Enter First No:")      #a="5"
# b=input("Enter Second No:")     #b="7"
# r=a+b                   #r="57": Incorrect approach
# print(r)

"""
There is no negative marking in our session.

Type Casting: Conversion of one data type to another data type.
Syntax:
res=dest_type(data)
"""
# #New Program
# a="5"
# a=int(a)
# print(a,type(a))
# a="5"
# a=float(a)
# print(a,type(a))

# #New Program
# a=5
# a=bool(a)
# print(a)

# #New Program
# no1=input("Enter First No:") #no1="5"
# no1=int(no1)                #no1=5
# no2=int(input("Enter Second No:"))      #no2=7
# res=no1+no2
# print("Result:",res)


# #New Program
# weight=float(input("Enter Your weight:"))
# print(weight,type(weight))

# #New Program
# s="CETPA"
# L=list(s)
# print(L)

"""
Conditional Statements:

If we get any assignment statement or print statement in a 
program then it always execute directly.
But if we want to run a set of statement by checking some
conditions then we can use conditional statements: if, elif and 
else
if and elif need True or False values:
if True then statements inside if will run otherwise won't

if, elif, else are called headings.
Heading is a statement in python which is having some set of
statements inside it ie a block of code inside it. This block 
of code inside a heading is called suite.
One heading should at-least one sub statement inside it.

Indentation: Used to separate block of codes in python.
(In C Lang we were using curly braces for code separation, in
python we are using indentation) 
How to achieve indentation: By writing all the statements at
a fixed gap (space) from the conditional heading.


Syntax:
if(condition):
    indented set of statements
elif(condition):
    indented set of statements
elif(condition):
    indented set of statements
elif(condition):
    indented set of statements
else:
    indented set of statements
"""
# #New Program
# code="1234"
# if(code=="007"):
#     print("Code is correct")
#     print("You are welcome")
# else:
#         print("Code is incorrect")
#         print("You are not allowed to enter")
# print("Code is Complete")

# #New Program
# code=input("Enter the Code:")
# if(code=="007"):
#     print("Code is correct")
#     print("You are welcome")
# else:
#         print("Code is incorrect")
#         print("You are not allowed to enter")
# print("Code is Complete")

#New Program
# a=5
# b=7
# r=a+b
# print(r)

"""
if alone is possible
but elif and/or else can only be used with if statement

elif: else if

"""

# #New Program
# day = input("Enter the day:")
# if(day=="Sunday"):
#     print("Take Rest")
# elif(day=="Saturday"):          #else if its Saturday
#     print("Go to Movie")
# elif(day=="Friday"):
#     print("Go for shopping")
# else:
#     print("Go to CETPA Class other than Vikas Sir Class")

"""
Operators:
Conditional operators: returns True or False 
==
!=      Not equals to
>
<
>=
<=


Logical operators:
and     #English wala and, hindi wala aur
or      #Englsih wala or ya hindi wala ya
not     #Wahi nahi
and: if both inputs are True then output is True else False
or: if at least one of the inputs is True then output is True else False
"""
# #New Program
# a,b=5,7
# print(a==5 and b==7)
# print(a>=5 and b<7)
# print(a>=5 or b<7)

# #New Program
# a,b=5,7
# print(a==b)
# print(a<b)

# #New Program
# id=input("Enter the id:")
# pwd=input("Enter the pwd:")
# if(id=="007" and pwd=="bond"):
#     print("Correct id and pwd")
# else:
#     print("Incorrect id or pwd")


# #New Program
# pwd=input("Enter the pwd:")
# if(pwd=="abcd"):
#     print("CETPA")
#     print("Hello")
#     print("Vikas")
#     print("ABCD")
# else:
#     print("Incorrect pwd")

# #New Program
# a,b=3,9
# if (a==43, b==44):      #if(True,True)      #if ( (True,True) )
#     print(a+b)
# elif (a==3 and b==9):
#     print("not bond")

"""
Packing and unpacking concept
"""
# #New Program
# a,b=5,7
# print(a,b)

# #New Program
# a,b="AB"        #Python supports Unpacking directly
# print(a,b)

# #New Program
# a,b,c,d,e="CETPA"        #Python supports Unpacking directly
# print(a,b,c,d,e)

# #New Program
# a,b,c,d="CETPA"        #Error
# print(a,b,c,d)

# #New Program
# a,b,c,d,e,f="CETPA"        #Error
# print(a,b,c,d,e)

# #New Program
# a="C","E","T","P","A"
# print(a,type(a))

# #New Program
# a=False,False
# print(a)
# print(type(a))

"""
Practise karte rehna
No Practise means No Learning
"""

"""
Nested Conditions:
Conditions inside conditions

Kasam Khalo: Koi bhee question poocha jaaye, answer jarror
dena hai, chahe answer pata hai ya nahi pata hai.
"""
# #New Program
# a,b,c=1,2,3
# if(a>=1):
#     print("Inside First If")
#     if(b<=2):
#         print("Inside Second If")
#     elif(b==3):
#         print("Inside First elif")
#     else:
#         print("ABCD")
# elif(a==0):
#     print("BCDE")
#     if(b==1):
#         print("CDEF")

# #New Program
# a=5
# if(a==5):
#     print("CETPA")
# elif(a==5):         #else if
#     print("Hello")
# else:
#     print("ABCD")

"""
Comparison of 3 numbers:


"""

# #Find the bigger between 2 numbers
# no1=input("Enter First No:")
# no2=input("Enter Second No:")
# if(no1>no2):
#     print(no1,"is the bigger no")
# else:
#     print(no2,"is the bigger no")

# #Find the bigger between 2 numbers or check if they are equal
# no1=input("Enter First No:")
# no2=input("Enter Second No:")
# if(no1>no2):
#     print(no1,"is the bigger no")
# elif(no1<no2):
#     print(no2,"is the bigger no")
# else:
#     print("Both numbers are equal")


# #New Program: Find the biggest of 3 numbers: Using nested conditions
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# no3=int(input("Enter Third No:"))
# if(no1>no2):    #If no2 is not the biggest, we will go inside if
#     if(no1>no3):
#         print(no1,"is the biggest no")
#     else:
#         print(no3,"is the biggest no")
# else:       #If we reach at else, it means no1 is not the biggest no
#     if (no2 > no3):
#         print(no2, "is the biggest no")
#     else:
#         print(no3, "is the biggest no")

# #New Program
# print("1" > "5")
# print("1" < "5")
# print("11" > "5")
# print(11 > 5)
# print("ABC" > "AAC")

"""

"""