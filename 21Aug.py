"""
"""
"""
User Interaction in Python:

Extended version of print:


"""
# #New Program
# a=5
# print(a)

# #New Program:
# a=5
# b=7
# temp=a      #temp=5
# a=b;        #a=7
# b=temp      #b=5
# print(a,b)

# #New Program
# a,b=5,7
# a,b=b,a
# print(a,b)

# #New Program
# s="CETPA"
# print(s)
# print(len(s))


"""
Python support Unpacking directly
"""
# a,b,c,d,e="CETPA"
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

"""There is no negative marking in our session"""

# #New Program
# a,b,c,d="CAT"       #ValueError
# print(a)
# print(b)
# print(c)
# print(d)

"""
Whenever we call a print function then it prints the space separated
arguments on the screen ie space is automatically in between the
arguments, in parallel after printing all the arguments, a new line
in printed ie cursor automatically moves to next line after print
statement is executed.
space in print function is printed on the screen automatically
if there are more than 1 arguments, space is made to separate the
arguments on the screen. 
 
"""

# #New Program
# a,b,c,d,e=2,3,4,5,6
# print(a,b,c)
# print(d,e)

"""
Ek bhee lecture chhuta, guarantee kavach toota.


"""
# #New Program
# print()
# print()
# print()

# #New Program
# a,b=5,7
# print(a)
# print(b)


"""
Escape Characters in Python: These characters leaves behind a special
functionality on the screen but in actual these characters are not
printed itself on the screen
\t:  Tab Character
\n: New Line Character

"""
# #New Program
# s="CE\tTP\tA"
# print(s)

# #New Program
# s="CE   TP  A"
# print(s)

# #New Program
# s="CE\nt\n\nPA"
# print(s)

# #New Program
# s="CETPA"
# print(s)

# #New Program
# s='CETPA'
# print(s)

# #New Program
# s='"CETPA"'
# print(s)

# #New Program
# s="'CETPA'"
# print(s)

"""

Optional parameters in print statement: 'end' and 'sep'
Default value of end = '\n'
Default of sep = ' ' ie space
We can consider end and sep as variables in python. When we print
our arguments then in between the arguments automatically sep is
printed and at the end of the arguments end is printed.

"""
# #New Program
# a,b,c,d,e=1,2,3,4,5
# print(a,b,c)        #asepbsepcend  print(a,sep,b,sep,c,end)
# print(d,e)          #dsepeend   print(d,sep,e,end)


# #New Program
# a,b,c,d,e=1,2,3,4,5
# print(a,b,c,sep="*",end="$")
# print(d,e,end="@")

"""
sandbox: Development Environment
Production Environment: Live Environment publish

cetpa
"""
# #New Program
# s="ce't'p'a"
# print(s)

# #New Program
# a,b,c,d,e=1,2,3,4,5
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# #New Program
# a,b,c,d,e=1,2,3,4,5
# print(a,end=" ")        #end space
# print(b,end=" ")
# print(c,end=" ")
# print(d,end=" ")
# print(e,end="")     #end empty string

# #New Program
# a,b,c,d,e=1,2,3,4,5
# print(a,end="")        #end empty string
# print(b,end="")
# print(c,end="")
# print(d,end="")
# print(e,end="")     #end empty string

# #New Program
# a,b,c,d,e=1,2,3,4,5
# print(a,b,c,d,e,sep="")

"""There is no negative marking in our session"""

# #New Program
# a,b,c,d,e=1,2,3,4,5
# print(a,b,sep="*")
# print(c,sep="#",end="$")
# print(d,e,end="CETPA")

"""
Perfect Communication: If I am transmitting something, I should
get a response whether you are getting it or not.
"""

# #New Program
# a,b,c,d,e=1,2,3,4,5
# print(a,b,c,sep="\t\cetpa\t\t",end="\n\n**")
# print(d,e)

# #New Program
# print("\tCETPA")
# print("C\tCETPA")
# print("CE\tCETPA")
# print("CET\tCETPA")
# print("CETP\tCETPA")
# print("CETPA\tCETPA")

# #New Program
# a,b,c,d,e,f,g,h=1,2,3,4,5,6,7,8
# print(a,b,c,sep="\t",end="*")
# print(d,sep="\t",end="*")
# print(e,f,sep="",end="\n")
# print(g,h,sep="CETPA",end="CETPA")

"""
Variable: Data Storing Element whose value varies in the program.

How variables are created in Python: By assigning the value
"""
# a=b     #NameError: name 'b' is not defined
# print(a)

# #New Program
# a=5
# print(a)

"""
Predefined names: Keywords

User Defined Names: Identifiers
Examples of Identifiers: Variable names, function names, class names  
Rules to define identifiers in Python: Possible valid identifiers:
1. All english alphabets are allowed ie upper case and lower case
2. Numbers are allowed from 0 to 9 but identifier name should not start with numbers.
numbers can be used in between or end of the identifiers.
3. Special Symbol: Only underscore ie _ is allowed
4. Can't have any special symbol other than underscore
5. Can't have any keyword names.
"""
# a b=5         #Not allowed space
# print(a b)
# cetpa=7       #Allowed
# print(cetpa)
# a*b=9         #Not allowed *
# print(a*b)
# true=5        #Allowed
# print(true)
# True=5        #Keywords not allowed
# print(True)
# _a=5          #Allowed
# print(_a)
# __a__="CETPA" #Allowed
# print(__a__)
# 5a="CETPA"      #Not allowed, can't start with numbers
# print(5a)
# a5=100      #Allowed
# print(a5)

# #New Program
# _5a=6
# print(_5a)

"""
Assignment:
8.	If i = 3, j = 2 what is the result of following expressions?
a.	i + 5 >= j – 6 
b.	j * 10 < i ** 2 
c.	i < j + 5 > j ** 4


"""
# #New Program
# i = 3
# j = 2
# print(i + 5 >= j - 6)   #8>-4
# print(j * 10 < i ** 2)      #20 <9
# print(i < j + 5 > j ** 4)   #    3<7 >16

# #New Program
# # 7.	If the radius of a circle is 3 meters, find the area of the circle.
# r=3
# a=3.14*r*r
# print(a)

# #Another way
# import math
# pi=math.pi
# print(pi)
# r=3
# a=pi*r*r        #a=(math.pi)*r*r
# print(a)
# a=round(a,2)
# print(a)

"""
Assignment jaroor karna hai.

No perfect practise means no learning.

10 AM till the next update
"""



