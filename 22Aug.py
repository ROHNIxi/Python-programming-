""
"""
My Day starts with good morning and ends with good morning only.

Life me kuch karna hai to ya to 3 baje jagna shuru karo ya 
3 baje sona shuru karo. 

StackOverflow.com : World's biggest website technical Q&A



Conditional Statements: To execute set of statements on the basis
of some conditions.




"""
# #New Program
# print("CETPA")
# print("Hello")
# print("Welcome")
# x=5
# y="CETPA"

# #New Program
# x=input("Enter Your Name:")     #x="007"
# print(x)
# print(type(x))


# #New Program
# x=int(input("Enter First No:"))     #x=007=7
# print(x)
# print(type(x))

"""
Print the Nos 1 to 5 at screen with a gap of two lines in between using 5 print 
statements. 
"""
# #New Program
# print(1,end="\n\n\n")
# print(2,end="\n\n\n")
# print(3,end="\n\n\n")
# print(4,end="\n\n\n")
# print(5)

"""
Conditional Statements: 3 Keywords: These keywords
plays the role of a heading: Heading in python is a statement
which is having some sub-statements inside it or a block of code
inside it. 
Syntax to create a heading in python:
heading_name:
All the statements inside a heading will be indented statements.
Indentation: Statements at a fixed gap (spacebars) w.r.to heading
 
if
elif
else

If condition will be true then only statements will be executed.
if is a condition
elif is a condition
else executes if conditions above else are false
"""
# #New Program
# x=6
# if(x==5):
#   print("CETPA")    #Execute if value of x is 5
#   print("Welcome")  #Execute if value of x is 5
# print("ABCD")   #Always execute

"""Statements inside a heading ie the block of code inside heading
in python is called a suite.
There should be al least one statement inside a heading.
"""
# #New Program
# x=5
# if(x<=5):
#     print("CETPA")
#     print("Welcome")
# print("ABCD")

# #New Program
# id=2345
# if(id==2345):
# print("Welcome to the System")    #IndentationError: expected an indented block

# #New Program
# id=2345
# if(id==2345):
#   print("Welcome to the System")

"""
Single Liner headings: Then we can mention the statement directly
next to heading in same line
"""
# #New Program
# x=5
# if(x==5):print("CETPA")
# print("Welcome")

# #New Program
# x=5
# if(x==5):pass
# print("Welcome")


# #New Program
# x=5
# if(x==5):
#   pass
#   print("CETPA")
# print("Welcome")

# #New Program
# x=5
# if(x==5):
#   pass
# print("CETPA")
# print("Welcome")

# #New Program
#   print("CETPA")    #IndentationError: unexpected indent
#   print("Hello")

# #New Program
# id=int(input("Enter the ID:"))
# if(id==1000):
#   print("Welcome to the System")
# else:
#   print("You are not allowed the entry")

# #New Program
# id=input("Enter the ID:")
# if(id=="1000"):
#   print("Welcome to the System")
# else:
#   print("You are not allowed the entry")

"""Akshat
Great Names think alike
"""
# #New Program
# id=input("Enter the ID:")
# if(id=="1000"):
#     print("Welcome to the System")
# else:
#   print("You are not allowed the entry")

"""
Multiple Conditions: if, elif, else
elif and else can't work without if

elif: else if


"""
# day=input("Enter the day:")
# if(day=="Sunday"):
#   print("Take Rest")
# elif(day=="Saturday"):
#   print("Go to Movie")
# elif(day=="Friday"):
#   print("Go for Shopping")
# else:
#   print("Go for CETPA Class")

"""If we want to check multiple conditions in single heading:
we can use logical operators 'and'  and 'or' 
"""

# #New Program: Better way
# day=input("Enter the day:")
# if(day=="Sunday"):
#   print("Take Rest")
# elif(day=="Saturday"):
#   print("Go to Movie")
# elif(day=="Friday"):
#   print("Go for Shopping")
# elif(day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday"):
#   print("Go for CETPA Class")
# else:
#   print("Incorrect input")

# #New Program
# id=input("Enter the ID:")
# pwd=input("Enter the Pwd:")
# if(id=="bond" and pwd=="007"):
#   print("You are authorized")
# else:
#   print("Incorrect id or pwd")

"""
Nested Conditions: Conditions inside conditions:
heading inside heading.
If there is a heading inside heading, then statements of the inner
heading will be indented with respect to inner heading
"""
# #New Program
# a=5
# b=9
# if(a==5):
#   print("CETPA")
#   print("ABCD")
#   if(b==7):
#     print("Welcome")
#     print("PQRS")
#   print("UVWR")
# else:
#   if(a==6):
#     print("1234")

# #New Program
# a=5
# b=7
# if(a==5):
#   print("CETPA")
#   print("ABCD")
#   if(b==7):
#     print("Welcome")
#     print("PQRS")
#   print("UVWR")
# else:
#   if(a==6):
#     print("1234")


# #New Program
# a=6
# b=7
# if(a==5):
#   print("CETPA")
#   print("ABCD")
#   if(b==7):
#     print("Welcome")
#     print("PQRS")
#   print("UVWR")
# else:
#   if(a==6):
#     print("1234")

# #New Program
# a,b=5,6
# if(a==5):
#   print("CETPA")
# if(b==6):
#   print("Hello")
# print("Welcome")

"""
if, elif we get True inside condition then block will execute else
won't
"""
# #New Program
# a,b=5,7
# print(a==b)
# print(a<b)
# print(a!=b)
# #New Program
# a,b=5,5
# if(a==b):
#   print("CETPA")

"""
False Values in Python:
0
False
None
All empty values
Rest all are True values

"""

# #New Program
# if(55):
#   print("CETPA")

# #New Program
# if(""):
#   print("CETPA")


# #New Program
# a=6
# b=7
# if(a==5):
#   print("CETPA")
#   print("ABCD")
#   if(b==7):
#     print("Welcome")
#     print("PQRS")
#   print("UVWR")
# else:
#   if(a==6):
#     print("1234")
#

# #New Program
# a,b,c,d=1,1,3,4
# if(a==1):
#   if(b>=2):
#     if(c>=3):
#       print("CETPA")
#     elif(c==2):
#       print("ABC")
#     else:
#       print("BCD")
#   elif(b==1):
#     print("CDE")
# elif(a==5):
#   print("DEF")
# elif(a==6):
#   print("EFG")

"""
Weekend: Golden Opportunity: Please jitna padha hai revise kar liya
karo, still always follow the Indian Railway Rule.
"""


