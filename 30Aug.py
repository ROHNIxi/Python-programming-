""
"""
1. Umesh: Compiler vs Interpreter:
2. Umesh: Explicit vs Implicit Conversion
3. Umesh: Match Case Statement: Python 3.10 version
4. Aman: Reverse Slicing Alternate Direction
5. Manoj: How to get last element using negative slicing
6. Hemant: Default lower and upper bounds 
7. Roshni: What happen, if we assign a new value to an existing variable.
8. Akshat: CETPA Full Form

Compiler vs Interpreter:

Compiler: Where the complete code is compiled in one go and then
the compiled code is executed line by line.
Interpreter: Where code is compiled and executed line by line.

Python is an interpreter based langauge, still we can compile our
code in python and generate intermediate compiled file. Compiled
file is python is having extension .pyc (Python Compiled File)

C, C++, Java are compiler based: Major things happen at compile
time
Python is interpreter based language: Things happen at run time.

Compiled Code is an intermediate code which is also called object
code, this code is not human understandable code.

Syntax Errors in the program are checked by compiler

How to compile a file:
import py_compile
py_compile.compile("Prog1.py")

Where to find the compile file: Current directory: folder:
__pycache__

There are hackers or ogranizations which claims that we can
decompile the compiled file but 100% decompilation is not
possible

Try to become Ethical Hacker ie make the hardware and software
infra so secure that hackers can't hack it.

Prove that Python is an interpreter based language.
Write any program having 5 print statements and make some error
in 3rd statement. We will get the output of first 2 statements
in python but we won't get any output in C or Java.

Why compilation? So that we can secure our code and compiled
executes executes at a faster speed.

Type Conversions are of two types:
1. Explicit Type Conversion: Type Casting which is important for us.
Where we intentionally change the data type.

2. Implicit Type Conversion: Where type conversion happens automatically
and result is converted to bigger data type.
"""
#
# import py_compile
# py_compile.compile("Prog1.py")

# #New Program
# import Prog2
# r1=Prog2.add(5,7)
# r2=Prog2.sub(5,7)
# print(r1,r2)

# #New Program
# print("ABC")
# print("BCD")
# pr("CDE")
# print("DEF")
# print("EFG")

# #New Program: Explicit type conversion: type casting
# L=[10,20,30,40,50]
# s=str(L)
# print(s)
# print(type(s))
# print(len(s))
# print(len(L))
# print(L[0])
# print(s[0:6])

# #New Program: Implicit Type Conversion
# a=5
# b=2.5
# r=a+b
# print(r)

"""
At some places, you will find type casting is of 2 types, implicit
and explicit, but at most of the places, you will find type
conversion is of 2 types where explicit is called type casting.
"""

"""
In C Lang, there was a concept of Switch Case, in Python same
concept is known as Match Case. Match case can be used in
place of if, elif and else statements.
Syntax:
match variable_name:
    case value1:
        set of statements
    case value2:
        set of statements
    case value3:
        set of statements
    case _:             #It like else
        set of statements
        
Match Case is used generally when we have multiple options
against single variable and we want to perform different
operations against different options of the variable
Like in Calculator, for different values of choice variable, 
we need different mathematical operations so we can use
match case.

But if we want to check multiple variables in same program like
checking id and pwd then we can better use, if, elif, else

Till now, most of the interviewers in the industry are not 
aware that match case is introduced in Python.
 
"""
# #New Program
# day=input("Enter any day:")
# match day:
#     case "Sunday":
#         print("Take Rest")
#     case "Saturday":
#         print("Go to Movie")
#     case "Friday":
#         print("Go for Shopping")
#     case _:
#         print("Go for CETPA Class")


"""
Reverse Slicing

Upper bound is always discarded in slicing
+ve step size: Move from left to right
Default lower bound will give left most element at the output
Default upper bound will give right most element at the output
+indices varies from 0 to n-1, 
default lower bound=0
default upper bound=n
 

-ve step size:  Move from right to left
Default lower bound will give right most element at the output
Default upper bound will give left most element at the output 
-indices varies from -1 (right most element) to -n (Left most) 
default lower bound=-1
default upper bound=-n-1
"""

"""
Roshni: What happens, if we assign a new value to an existing variable.

How variables are made in C Lang: By defining the data type:
int a;
a=5;

How variables are made in Python: By assigning the value:
a=5     #Variable is made of int type
a="CETPA"       #Variable is made of str type

Variable vs Object: Python indirectly stores the data
Variable is just the name and object is the actual memory. 
x=5         #Say 5 is stored at 1000 location
            #Say x is representing 100 location having address
            #of 5 
            #Now the 
x=7         #Say 7 is stored at 2000 location
            #Now x is still representing 100 location but
            #having address of 7 in it

Python supports dynamic memory allocation, so whenever we 
pass a new value then it is stored at a new address and the
variable starts referring to new address.

In Python to store one address, it require 8 bytes.

CETPA Full form:
In the year 2004, I have completed my Engineering from COER
Roorkee in ET Branch.
VHDL: Very Hard and Difficult Language: VLSI designing.
Society: Computer Education and Technology Promotion Association
(CETPA) in the year 2003. 
In 2005 started our company: CETPA Infotech Pvt. Ltd. 
We are 3 partners in CETPA: 

So job is not the only line to enter into professional world,
you can think about the other option also ie Entrepreneurship

IIT Roorkee:
"""

"""
Topic Functions:
PL (Presentation Layer): Responsible for user interaction
BLL (Business Logic Layer): Responsible for writing the business logic

Kuch Kasame maine apko khilayee thee.

First Kasam: Always take logical names of identifiers.
Second Kasam: Write as much comments as possible in the program
Third Kasam: Divide your program at least into 2 layers ie 
Presentation Layer and Business Logic Layer.

Camel Nomenclature: These are guidelines designed by Developers
community to take logical identifier names.
1. Function Name should start with small letter and rest all
trailing words should start with capital letters
Example:
add_Customer() or addNewCustomer()
2. Class Name should be in title case: First letter of all
words should start with Capital Letter
MyCustomer   or M_Customer
Above 2 guidelines are as per camel nomenclature
rest other guidelines for identifier names
1. Try to use underscore in between words
2. Variable names should not have capital letter
3. Identifiers names should be logical names ie they should
represent the purpose of identifier.
Ex: Variable names
cus_id, cus_age, cus_name, cus_mob, cus_email, cus_add, cus_city,
cus_dob, cus_state, cus_gender......

Functions:
The formal parameters and actual parameters names can be same or
can be different as per the interest or requirement.

Whenever we call a function in any programming langauge, the 
actual parameters are assigned to formal parameters.

Now if we want a program for calculator then try to make it using
2 layers.
"""
# #BLL
# def add(a,b):       #a,b formal parameters
#     r=a+b
#     return r
# def sub(a,b):
#     return a-b
# #PL
# a,b,c,d=1,2,3,4     #This statement can be a part of PL or BLL
# r1=add(a,b)
# r2=sub(c,d)
# print(r1,r2)

"""
In Python return statement is optional.
The functions which return nothing in the program then they
return None value.
"""

# #New Program
# def func1(a,b):
#     r=a+b
#
# r=func1(5,7)
# print(r)

# #New Program
# s=input("Enter Your Name")

# #New Program
# s=print("CETPA")
# print(s)

# #New Program
# def add(a,b):
#     r=a+b
#     return r
# u,v=5,7
# s=add(u,v)      #a=u, b=v
# print(s)
"""u and v are actual variables in above program.
a and b are formal variable in above program
"""
"""There is no negative marking in our session. Agar mai ya
Examiner ya interviewer apse question poochta hai aur negative 
marking nahi hai to answer jarror dena hai.

Fourth Kasam: Alayws give the answer.
"""
# #New Program
# #New Program: Not a better approach to create a function
# def add():
#     r=a+b
#     return r
# a,b=5,7
# s=add()
# print(s)
# #New Program: Better approach
# def add(a,b):       #a,b,r are called local variables
#     r=a+b
#     return r
# a,b=5,7
# s=add(a,b)      #a,b,s are called global variables
# print(s)

"""
We can access global variables inside functions directly but
we can't access local variables outside functions.

Hemant vs Harshit.
"""
# #New Program
# def func1():
#     a=5         #Local Variable
#     print(a)
# func1()
# print(a)        #NameError: name 'a' is not defined


# #New Program
# def func1():
#     print(a)        #a global variable
# a=5
# func1()
# print(a)            #a global variable

"""
If there are two variables with same name, one inside function
and one outside function then inside function local variable
will be accessed and outside function global variable will be
accessed.
In following program, why global variable is not modified, becuase
in python, how variables are created? By assigning the value.
If we have a variable outside function (Global variable) and 
we try to access it inside function then it is accessible, 
but the moment we try to modify the global variable inside
function, what happens, a new local variable is created.
Still if we want to modify global variable inside function.

  

"""
# #New Program
# def func1():
#     a=5             #
#     print(a)
# a=7
# func1()
# print(a)

# #New Program
# def func1():
#     global a
#     a=5             #
#     print(a)
# a=7
# print(a)
# func1()
# print(a)

# #New Program
# def func1():
#     a=5             #local variable
#     print(a)
#
# func1()
# print(a)        #NameError: name 'a' is not defined

# #New Program
# def func1():
#     global a
#     a=5             #global variable
#     print(a)
#
# func1()
# print(a)

"""
10 AM: Monday
If there is some change, I will update in the group
"""

