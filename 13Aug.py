""
"""
Operators:  Like there are 7 Wonders of World, similarly 
there are 7 Types of Operators in Python.
1. Arithmatic Operators: 7 Operators
+       Addition
-       Subtraction
*       Multiplication
/       Division
**      Exponent
%       Remainder/Modulus
//      Floor Division

Comments : Single Line Comment: # character
First Kasam: Always write at least 1 comment in the program ie
type the purpose of the program. Try to use as much comments
as possible.

Multi Line Comment: There is no direct option in python for
multiline comment. Now IDE's provides us some shortcut keys to
make multiple lines as comments but line by line comments
Pycharm Shortcut key: Cntrl + /

There is a Jugaad in Python which is not an official way of making
multiline comments but developers use this style frequently. 
ie make any set of statments as strings and don't save it in a 
variable then it can be seen as multiline comments
"""
# #New Program
# a=5
# b=2
# r=a/b
# print(r)
# a=5
# b=2
# r=a//b
# print(r)
# a=5
# b=-2
# r=a//b
# print(r)

# #New Program
# a=5
# b=3
# r=a**b      #a to the power b
# print(r)

# #New Program
# "cetpa"



# #New Program
# a=5
# b=3
# r=a%b      #a remainder b
# print(r)

"""
Relational/Conditional Operators: 6 Types: Returns bool value
ie True or False: Generally used to check conditions
==      Equals to :Compares and check values are equal or not
!=      Not Equals to
>       Greater Than
<       Less Than
>=      Greater Than Equals to
<=      Less Than Equals to
"""
# #New Program
# x=5
# print(x>5)


# #New Program
# pwd=input("Enter the Password: ")     #pwd=vikas123
# print(pwd=="Vikas123")

"""
There is no negative marking in our session, if ans is True or
False in your exam then what will you do?
"""

# #New Program
# a,b=5,7
# r=a==b
# print(r)

# #New Program
# a,b=5,5
# r=a>=b
# print(r)

"""
Logical Operators: Generally used to check multiple conditions.
and : When both the inputs are True, output is True
or  : When at least one of the input is True, output will be True 
not : Toggle the output: Input True then output False and vice versa

What are False values in python:
False
0
None
All empty values
Rest all are True values

s=""        #Empty String, 
u=[]        #Empty List



If inputs are not boolean value:
and: if first input is False then output is first input else
output will be second input
or: If first input is True then output is first input else 
output will be second input. 

"""
# #New Program
# user="Vikas"
# pwd="Kalra"
# res=(user=="Vikas" and pwd == "Kalra")  #True and True
# print(res)


# #New Program
# user="Vikas"
# pwd="cetpa"
# res=(user=="Vikas" and pwd == "Kalra")  #True and False
# print(res)



# #New Program
# a,b=5,7
# r= a and b      #First input is True output will be second
# print(r)

# #New Program
# a,b="",7
# r= a and b      #First input is False output will be first
# print(r)

# #New Program
# a,b=0,7
# r= a and b      #First input is False output will be first
# print(r)


# #New Program
# a,b=-89000,7
# r= a and b      #First input is True output will be second
# print(r)


# #New Program
# a,b=5,7
# r= a or b      #First input is True output will be first
# print(r)

# #New Program
# a,b="",7
# r= a or b      #First input is False output will be second
# print(r)

# #New Program
# a,b=0,7
# r= a or b      #First input is False output will be second
# print(r)


# #New Program
# a,b=-89000,7
# r= a or b      #First input is True output will be first
# print(r)

"""
Bitwise Operators: 6 in numbers: Works on bits
Bits are checked at same position level or index level. 

&   : and: If both bits are 1, output will be 1   
|   : or: If at least 1 of the bit is 1, output will be 1
~   : not: Toggle  
^   : xor: If both bits are different then output will be 1
<<  : shift left with 0 filling: 
>>  : shift right with upper bit filling
a << b means a will be shifted to left, b times
Shift Left: All the bits will be shifted to left, MSB (Most 
significant bit ie left most bit) will be discarded and LSB 
will be filled with 0.

Decimal
00
01
2
.
.
9
10
11
.
19
20


0000        : 0
0001        : 1
0010        : 2
0011        : 3
0100        : 4
0101        : 5

"""
# #New Program
# a=5         #  0101
# b=3         #  0011
# r= a & b    #  0001     #r=1
# print(r)


# #New Program
# a=5         #  0101
# b=3         #  0011
# r= a ^ b    #  0110     #6
# print(r)


# #New Program
# a=3         #  0011 #Right most 1 is called LSB (Least Significant bit)
# b=2
# r= a << b    #  First time shift left: 0110
#              #Second time shift left:  1100 : 12
# print(r)

"""
All variables in python are of reference type ie when we assign
one variable to another variable in python then address of RHS
variable is assigned to LHS variable.

Assignment Operators: 1 (Equals to) + 7 (Arithmatic operators)
                        +5 (Bitwise operator) + 1 (walrus)= 14
=       Equals to 
+=      a+=b means a=a+b
-=
*=
/=
**=     a**=b means a=a**b
%=
//=     a//=b means a=a//b
&=      a&=b means a=a & b
|=
^=      a ^= b means a = a ^ b
<<= 
>>=     a >>= b means a = a >> b
:=  Walrus operator: used to assign a value to a variable inside
an expression


"""
# #New Program
# a=5     #
# b=a
# print(id(a))
# print(id(b))

# #New Program
# a,b=5,7
# a+=b        #a=a+b
# print(a)

# #New Program
# a=5
# a+=1        #a=a+1
# print(a)

# #New Program
# a,b=5,3
# a**=b       #a=a**b
# print(a)


# #New Program
# a,b=5,3
# a^=b       #a=a ^ b
# print(a)


# #New Program
# a,b=3,2
# a<<=b       #a=a << b
# print(a)


# #New Program
# print(a=5)      #TypeError: 'a' is an invalid keyword argument for print()

# #New Program
# print(a:=5)

# #New Program
# r=(a:=5+5)
# print(r)



