""
"""
By using first, second and last characters of the string, create a new string.  
str="Hi, How are you?"

"""
# #New Program
# str="Hi, How are you?"
# res=str[0]+str[1]+str[-1]
# print(res)

"""
Write a Python program that lowercase the first letter of all words in a given 
string and capitalize the remaining letters in a given string. 
"""
# #New Program
# str="""CETPA clients list include Fiserv, Cadence, Samsung, IGT and more"""
# str=str.title()
# print(str)
# str=str.swapcase()
# print(str)


"""
Topic of the day: 
Loops:

for loop:
for element in iterator:
    set of statements
"""
# #New Program
# for i in range(5):      #Lower bound=0, upper bound=5, step_size=1
#     print("*")

# #New Program
# for i in 5:     #TypeError: 'int' object is not iterable
#     print(i)


# #New Program
# for i in "CETPA":
#     print(i)

# #New Program
# for i in "":
#     print(i)

# #New Program
# L=[10,20,30,40,50]
# for e in L:
#     print(e)
#     print(e/2)
#     print(e**3)
# print("CETPA")


# #New Program
# for i in range(3,31,3):
#     print(i)


"""
First:
We can access the elements of an iterator directly in for loop
for e in iterator:
    print(e)
    
Second:
Another way to access the elements of an iterator is using indexing in
for loop with range class. 
Yaad rakhna hai ie indexing with range class
for i in range(len(iterator)):
    print(iterator[i])
Second syntax we can preferably use in case, we want to access
a) More than one element in one iteration
b) We have more than one iterators
"""

# #New Program
# s="CETPA"
# for e in s:     #e="C"
#     print(e)

# #New Program
# s="CETPA"       #index: 0 to 4, s[0],s[1],s[2],s[3],s[4]
# for i in range(5):      #i=0,1,2,3,4
#     print(s[i])


# #New Program
# s="CETPA"       #index: 0 to len-1, s[0],s[1],s[2],s[3],s[4],
# for i in range(len(s)):      #i=0,1,2,3,4, range(5), for e in s:
#     print(s[i])

# #New Program
# L=[10,20,30,40]
# for e in L:
#     print(e**2)

# #New Program: Sum of consecutive 2 elements, ie 0th+1st then 1st+2nd
# L=[10,20,30,40]     #Indices: 0 to 3
# for i in range(len(L)-1):  #range(3) 3 times, i=0,1,2
#     print(L[i]+L[i+1])

# #New Program
# L=[10,20,30,40]     #i=0
# i=0
# print(i,L[i])
# i+=1        #i=i+1
# print(i,L[i])
# i+=1        #i=i+1
# print(i,L[i])
# i+=1        #i=i+1
# print(i,L[i])


# #New Program
# L=[10,20,30,40]     #i=0
# for i in range(len(L)):      #i=0,1,2,3
#     print(i,L[i])
# i=0
# print(i,L[i])
# i+=1        #i=i+1
# print(i,L[i])
# i+=1        #i=i+1
# print(i,L[i])
# i+=1        #i=i+1
# print(i,L[i])

# #New Program
# L1=[10,20,30]       #index 0,1,2
# L2=[100,200,300]    #index 0,1,2
# L3=[30,40,50]       #index 0,1,2
# for i in range(len(L1)):      #range(3), i=0,1,2
#     print(L1[i]+L2[i]+L3[i])

# #New Program
# L1=[10,20,30]       #index 0,1,2
# L2=[100,200,300]    #index 0,1,2
# L3=[30,40,50]       #index 0,1,2
# for i in range(len(L1)):      #range(3), i=0,1,2
#     print(L1[0]+L2[0]+L3[0])

"""
How to print elements of a Series
2sq
3sq
4sq
.
.
9sq
Step 1: Check no of elements, 
Step 2: Check any common operator or common condition.
Step 3: Decide the range wrto i. Leave common things
for i in range(2,10):
Step 4: Create a table of i and terms to print/use
i       term_to_print
2       2sq
3       3sq
.
.
9       9sq
Step 5: Now leave python and use mathematics to find the relationship
between i and term
term=i**2

"""
# #New Program
# for i in range(2,10):       #i=2,3,4,...9
#     t=i**2
#     print(t)            #print(i**2)

"""
Print:
(2sq+3sq)/3,   (3sq+4sq)/4,    (4sq+5sq)/5,   .....(8sq+9sq)/9

"""
# #New Program
# for i in range(2,9):        #i=2,3,4....8
#     t=(i**2+(i+1)**2)/(i+1)
#     print(t)

"""
Till now we have discussed Level 1 in loops: Basic Level: ie how
to access elements of iterator and use them in loop. 
or How to print elements of a Series

Level 2 in Loops: Now put some common operation on all elements
of a Series and print the result.

2,4,6......20 till now we have printed elements
Now: 2+4+6+8+....20
Steps: 
1. no of elements: 10
2. Table:
i       term
0       2
1       4
2       6
.
9       20
3. Formula between term and i: t=  (i+1)*2      
"""
# #New Program
# for i in range(10):       #Way 1
#     t=(i+1)*2
#     print(t)

# #New Program: Way2
# for i in range(2,21,2):
#     print(i)



"""
2,4,6......20 till now we have printed elements
Now: 2+4+6+8+....20
Steps: 
1. no of elements: 10
2. range: i in range(2,21,2)
3. Table:
i       term
2       2
4       4
6       6
.
20       20
4. Formula between term and i: t= i      
5. For common operation on elements of a series, use the formula
result=result operator term
6. Before loop starts, initiate the result in such a way that 
when first time loop runs, result should have the value of first
term
7. Come out of the loop and print the result

t=5
r=r+t
print(r)        #Error, r undefined

"""
# #New Program
# r=0
# for i in range(2,21,2):     #i=2,4,6....20
#     t=i         #t=2,4,6,8,...20
#     r=r + t     #Result=Result operator term, r=2, 2+4. 2+4+6, 2+4+6+8...2+4+6+8+...20
# print(r)

# #New Program: Sum of elements of a list
# L=[10,20,30,40,50]      #10+20+30+40+50
# r=0
# for e in L:
#     t=e
#     r=r + t     #r=10+20+30..50
# print(r)


#New Program: Make your own upper method for string
# s=input("Enter Any String:")    #"cetpa123"
# for e in s:         #e="c"
#     code=ord(e)        #code=99
#     if(code>=97 and code<=122):
#         code=code-32        #code=67
#     ch=chr(code)           #chr="C"
#     print(ch,end="")

# #New Program
# def myUpper(s):     #s="cetpa123"
#     r=""
#     for e in s:  # e="c"
#         code = ord(e)  # code=99
#         if (code >= 97 and code <= 122):
#             code = code - 32  # code=67
#         ch = chr(code)  # chr="C"
#         r=r+ch                    #"C" + "E" + "T" ..."3"
#     return r
# #PL
# s=input("Enter Any String:")    #"cetpa123"
# res=myUpper(s)
# print("The string in upper case is:",res)







