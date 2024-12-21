""
"""
Python Programming:


IDE: Software:
1. PyCharm: Python Install, Pycharm Community Edition

Types of Application:
1. Console Applications
2. Windows Applications


User Interaction: 
1. print function
2. input function

Function Calling Syntax:
function_name(arguments)

print function syntax: Basic Syntax
print(values,variables,expressions, conditions,functions,classes)

If we pass functions inside functions then firstly inner function are
executed and then outer functions are executed.
"""
# #New Program
# a,b=5,7
# c="CETPA"
# print(5,True,"a",a,c,a+b,a>b,len(c),type(c) )
# n=len(c)
# print(n)

"There is no negative marking in our session"
# #New Program
# s=print("CETPA")
# n=len("CETPA")
# print(s)
# print(type(n))
# print(type(s))

"""
Data Types: To represent different types of values 
Single element:
int: Whole Numbers  22      -563
float   : Decimal Point:    2.0     3.62
complex:    2+3j    Real+Imaginary
bool:  Only 2 values,  True, False
NoneType:   None

Multi element: Iterators
str
list
tuple
dict
set
frozenset

"""
# # print(true)       #Error
# print(True)         #bool
# # print(a)        #Error


# #New Program
# a=b         #NameError: name 'b' is not defined
# print(a)

# #New Program
# a=2+3j
# print(type(a))

"""
Mai chahe late ho jaau apko late nahi hona hai,

str: Syntax: characters in a sequence included within single quotes,
double quotes, triple quotes
str is a collection of homogeneous data types ie collection of characters.

Single Line String: Single, Double or Triple Quotes

Multi Line String: Only triple quotes
"""
# s='Welcome to CETPA'
# print(s)
# s="Welcome to CETPA"
# print(s)
# s='''Welcome to CETPA'''
# print(s)
# s="""Welcome to CETPA"""
# print(s)

# #New Program
# a="a"
# print(type(a))

# #New Program
# s='''Welcome to CETPA.
# CETPA is an award winning training company.
# CETPA is awarded by Chetan Bhagat, Shasho Tharoor and ...'''
# print(s)
# s="""Welcome to CETPA.
# CETPA is an award winning training company.
# CETPA is awarded by Chetan Bhagat, Shasho Tharoor and ..."""
# print(s)

"""
len function is created to find the length of iterators
len function won't work on single elements data type
"""

"There is no negative marking"
# #New Program
# s=25
# n=len(s)    #Error
# print(n)

"""
input function: 
Syntax:
input("Message for user")
var_name=input("Message for user").
Input function will hold the program till the time we press enter
or pass the value and press enter.


"""
# #New Program
# s=input("Enter Your Name:")
# print(s)

# #New Program: Addition of two input numbers
# a=input("Enter First No:")      #a=5
# b=input("Enter Second No:")     #b=7
# r=a+b                   #
# print(r)                #

"""
Whenever we interact with the user in python then data is 
always travelled in string format.
input function always returns strings type of data in our 
program.
print function firstly call a __str__ method on the arguments
of the print function, and this str method always returns 
string data type and this string value returned from __str__
method is printed on the screen. 


"""
# # print(25)
# L=[10,20,30]
# s=str(L)
# print(s)
# print(L)
# r=L.__str__()
# print(r)


# #New Program
# x=5
# print(x,type(x))
# x="5"
# print(x,type(x))

"""
+ operator if applied on string then it concatenate the 
strings ie join the strings.
+ operator works as a concatenation operator in case of
strings.
"""

# #New Program
# a=5
# b=7
# s=a+b
# print(s)
# a="Ram"
# b="Shyam"
# s=a+b
# print(s)


# #New Program
# a="5"
# b="7"
# r=a+b
# print(r)

# #New Program: Addition of Two numbers: Incorrect Approach
# no1=input("Enter First No:")    #no1="5"
# no2=input("Enter Second No:")   #no2="7"
# res=no1+no2                     #res="57"
# print(res)

"""
Whenever we take input from user then first and foremost
thing is plan to consider the data type of input.

To convert one data type to another data type in programming
then this concept is called type casting.

Type Casting Syntax:
dest_var=dest_type(src_var)

"""
# #New Program
# x=5
# y=float(x)
# print(y,type(y))

# #New Program
# x="5"
# y=float(x)
# print(y,type(y))

# #New Program
# x="5"
# y=int(x)
# print(y,type(y))

# #New Program
# x=2.35
# y=int(x)
# print(y,type(y))

# #New Program
# x=2.35
# y=str(x)
# print(y,type(y))

# #New Program
# no1=input("Enter First No:")    #no1="5"
# no1=int(no1)                    #no1=5
# no2=int(input("Enter Second No:"))  #no2=7
# res=no1+no2     #res=12
# print("Result:",res)

# #New Program
# print(int("5"))

# #New Program
# a="Ram"
# b="Shyam"
# r=a+" "+b
# print(r)

"""
str data type:

"5" vs 5 in memory
str and int

integers are directly converted to binary and saved
5: 101

ASCII Standard: American Standard Code for Information Interchange
ASCII code were initially developer of 7 bit length and later
it was designed with 8 bit length.

8 Bits numbers:
Smallest No of 8 bits: 00000000: 0
Biggest value of 8 bit number: 11111111: 2 Power 8 -1= 255
Unique nos in 8 bits: 256 (0 to 255)
ASCII is a standard to represent different standard keys of
English Keyboard.
A:      65          a:  97
B:      66          b:  98
C:      67          c:  99


Z:      90          z:  122

0:  48
1:  49
2:  50
3:  51
4:  52
5:  53

9:  57

"5":

Through ASCII numbers we can represent only English Alphabets,
Numbers or some special symbols because ASCII code is of 
only 8 bits.
To consider alphabets or special symbols of other languages
of the world, a new standard was created ie Unicode Standard.
16 Bits Combinations: 2 power 16: 65536
Unicode support 16 bits, 32 bits, 64 bits...

Now Python 3 support unicode
the ascii codes were given same number representation in unicodes
also
A: ASCII Code 65, and Unicode 65

ord function returns the Unicode of the character passed
chr function returns the Character of the unicode passed 
 
"""
# print(2**16)
# print(2**8)
# print(ord("a"))
# print(ord("0"))
# print(ord(" "))
# print(ord("$"))
# print(chr(47))
# print(chr(65))

# #New Program
# print(chr(2346))
# print(ord("प"))

"  "