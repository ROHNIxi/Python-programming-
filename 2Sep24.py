""
"""
Functions:

Identity Operators: Address check
is
is not

Comparison Operator: == Value check

"""
# print(5%2)      #Remainder

# #New Program
# a=5         #a address 1000
# b=a         #b address 1000
# print(a is b)
# print(id(a),id(b))
# a=7
# print(a is b)

"""
All variables in Python are of reference type. When we
assign one variable to another variable in Python, the address of
RHS variable is assigned to LHS variable. Generally the quality of
ref type variable is that we can change the value of one variable
the other variable should also get changed, but this effect is
generally not directly visible in python why? Because Python 
supports dynamic memory allocation, whenever we assign a new
value to a variable in python, it is stored at a new address. 

How variables are created in Python: By assigning the value.
If assign int value, variable will become of int type
If assign str value, variable will become of str type

All variables are stored in RAM, the moment we stop our program, 
all the location get free ie values of variables are washed. 


C Lang: Value type variables
int a,b;       a address 1000   b address 2000
a=5;        5 will be at 1000 address
a=7;        7 will be at 1000 address
b=a;        7 will be stored at 2000 address
Through the program a and b can have only int type values in C.
In C Lang, each data type have its data storage limit.
If int takes 2 bytes then int range is -32768 to +32767  

Python: Dynamic memory allocation: 
How variables in created: By assigning the value.
Every time we assign a new value in Python, new addresses will
be allocated. 
a=5
Steps:
1: Will check what is the data type of 5 and how much memory is 
needed to store 5, say 10 bytes are needed
2. That much memory (say 10 bytes) will be searched in RAM and will be blocked, say
1000 address onwards 10 bytes are blocked (say 1000 to 1009 
locations are blocked to store 5)
3. 5 Will be stored at that location ie at say 1000 address onwards.
4. a will start referring to that location ie 1000 address. 
Now if we write a=7 or a="CETPA" again all above steps will be
repeated, why
Now say to store "CETPA" we need 20 bytes so if these 20 bytes will
be written at same 1000 location then these bytes may store
at 1000 to 1019 locations (20 bytes) but it may be that 1010 onwards
some other variable of the same program is stored then what will
happen, the value of that variable will also be overwritten by "CETPA"
and that data will be lost, to avoid this, python made a rule ie
whenever we assign a new value to a variable of same size or
different size it will stored at different location. 

Variables are temp data storage elements, to permanently store
data, we can store in hard disk using file handling, in database
or other locations.

a=5     #a address 1000
a=7     #a address 2000,     
The moment a particular location is not referred by any variable
then automatically garbage collector process starts in the 
background and make that location free.
Here once 7 is stored at 2000 location, a will starts referring
to 2000 location and after referring to 2000 location, it will
stop referring to 1000 location and now 1000 location will be 
made free by garbage collector. 

a=5     #a address 1000
b=a     #b address 1000, why all variables in python are of ref type
a=7     #a address 2000
print(a is b)   False




Banti and Vikas
"""
# a=5                 #address 1000
# print(id(a))
# a=7                 #address 2000
# print(id(a), type(a))
# a="CETPA"           #address 3000
# print(id(a), type(a))

# #New Program
# a=5     #a address 1000
# print(id(a))
# b=a     #b address 1000, why all variables in python are of ref type
# print(id(a),id(b))
# a=7     #a address 2000
# print(id(a),id(b))
# print(a,b)


# #New Program
# a=5
# a=7
# del a
# print(a)        #NameError: name 'a' is not defined


# #New Program: Check Even Odd
# #BLL
# def checkEvenOdd(a):        #a=7
#     if(a%2 == 1):
#         return "Odd"
#     else:
#         return "Even"
# #PL
# no=int(input("Enter Any Whole Number:"))    #no address 1000
# res=checkEvenOdd(no)    #a=no, a address 1000
# print("The entered number is",res)

# #New Program
# def func1(a):           #a local variable, a address, a=7
#     a=5                 #a address 2000, python support dynamic memory allocation
#     print(a)
# a=7             #a address 1000, 7, a is global variable
# print(a)        #output: 7
# func1(a)        #a=a, left a ie formal variable address 1000
# print(a)
#557: 1
#757: 3
#755: 10


# #New Program
# def func1(a):           #a local variable, a address 1000, a=7
#     print(a, id(a))
#     a=5                 #a address 2000, python support dynamic memory allocation
#     print(a,id(a))
# a=7             #a address 1000, 7, a is global variable
# print(a,id(a))        #output: 7
# func1(a)        #a=a, left a ie formal variable address 1000
# print(a,id(a))

"""
There is no negative in our session. 

Mutable vs Immutable:
Mutable: Value can be changed at same address
Immutable: Value can't be changed at same address

list, dict and set are mutable type
Rest int, float, complex, bool, NoneType, str, tuple, frozenset
at immutable type

List vs Tuple

x=5 #int address 1000
x=7 #x will be stored at a new address 2000, so int is not mutable
means it is immutable because we can't make the changes at 1000
address at same address, why python supports dynamic memory 
allocation.

Mutable: If we change elements of list then base address of list
won't change.
But if we change the list value as a whole then base address
will be changed and list will be stored at different address why
because all variables in python support dynamic memory allocation
ie python supports dynamic memory allocation
"""
# #New Program
# L=[10,20,30,40,50]      #L address 1000
# print(L,id(L))
# L[0] = 80               #L address 1000
# print(L,id(L))

# #New Program
# L=[10,20,30,40,50]      #L address 1000
# print(L,id(L))
# L=[80,20,30,40,50]      #L address 2000
# print(L,id(L))
# L="CETPA"
# print(L,id(L))

# #New Program
# s="CETPA"
# print(s,id(s))
# s[0]="M"        #Error: Because str is immutable in nature
# print(s,id(s))

# #New Program
# t=(10,20,30,40,50)
# print(t,id(t))
# t[0]=80             #Error, tuple is immmutable in nature
# print(t,id(t))

"""
As a whole if we try to change any variable, mutable or immutable,
it will be stored at a different address
"""
# #New Program
# s="CETPA"
# print(s,id(s))
# s="METPA"
# print(s,id(s))

"""
list and tuple are collection of heterogeneous data type.
list is mutable and tuple is immutable
If we change the elements, increase or decrease the no of elements
in list, the base of address doesn't change
"""
# #New Program
# s1="CETPA"      #s1 address 1000
# s2=s1           #s2 address 1000
# s2="METPA"      #s2 address 2000
# print(s1)

# #New Program
# L1=[10,20,30]       #L1 address 1000
# L2=L1               #L2 address 1000
# L1[0]=80            #L1 address 1000, list is mutable
# print(L2)
# print(id(L1),id(L2))

# #New Program
# L1=[10,20,30]       #L1 address 1000
# L2=L1               #L2 address 1000
# L1=[80,20,30]       #L1 address 2000, dynamic memory allocation
# print(L2)
# print(id(L1),id(L2))

"""
Why we create copy of a variable in programming language, to
reuse old values
"""

# #New Program
# L1=[10,20,30]       #L1 address 1000
# L2=L1               #L2 address 1000, all varaibles are of ref type
# L1[0]=80            #L1 address 1000, list is mutable
# print(L2)
# print(id(L1),id(L2))



