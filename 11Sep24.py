""
"""
Take X as int input from user, print the 10 element of following series: 
X, X3,, X5, X7……….  
range(10):  i=0....9
i       t
0       1
1       3
2       5


9       19
t=(2*i+1)

input x
for i in range(10):
    t=(2*i+1)
    print(x**t)
"""
# #New Program
# x=int(input("Enter Any Number:"))
# for i in range(1,20,2):
#     print(x**i)


"""
Create your own generalized index function. Print all the matching index 
positions of an element present in a list [2,3,4,5,6,2,3,4,2,3,4,2]. Take the 
element as input from the user.  

"""

# #New Program
# L=[2,3,4,5,6,2,3,4,2,3,4,2]
# ele=int(input("Enter Any No:"))     #ele=4
# if(ele not in L):
#     print("Element not present in data")
# else:
#     for i in range(len(L)):     #range(12), i=0,1,2,...11
#         if(L[i]==ele):  #i=0,L[0]=2, i=1,L[1]=3, i=2,L[2]=4
#             print(i)

"""
7. Take an int number input from user and print the sum of digits of the number.  
or even can take the data in a list ie sum of elements of a list
"""
# #New Program
# data=input("Enter Any big number:")     #data="2342378"
# r=0
# for e in data:      #e="2"
#     t=int(e)        #t=2
#     r=r+t
# print(r)

"WAP to check whether a number input by user is ArmStrong number or not? "
""""""
# #New Program
# data=input("Enter Any number:")     #data="153"
# r=0
# n=len(data)
# for e in data:
#     t=int(e)**n
#     r=r+t
# if(r==int(data)):
#     print("Its an ArmStrong No")
# else:
#     print("Its not an ArmStrong No")

"""

"""


""
"""
CMS:
Add a Customer
Search a Customer
Delete a Customer
Update/Modify Customer
Display All Customers

Customer Properties: id,name,age,mob
"""

"""
Dictionary:
1. Dictionary is a collection of heterogeneous data types.
2. Dictionary is a collection of key-value pairs. One key-value
pair is called one item.
3. Dictionary is mutable in nature
4. Dictionary can have only unique keys ie can't have duplicate keys.
5. Dictionary is a collection of unordered items. Dictionary 
elements don't have direct index.

Syntax:
{comma separated key-value pairs}
dict_var={key1:value1,key2:value2,key3:value3....}

Syntax to access elements of a dictionary:
dict_var[key]


"""
# #New Program
# d={1:10,2:50,"CETPA":80,90:"ABC",50:[2,3,4]}
# print(d[1])
# print(d["CETPA"])
# print(d[50])

# #New Program: Aditi says if duplicate keys are there
# d={1:10,2:20,3:30,2:50,4:40,2:80}
# print(d)

# #New Program
# d={1:10,2:20,3:30}      #d address 1000
# print(d,id(d))
# d[2]=80                 #d address 1000
# print(d,id(d))

"""
Benefit of using dictionary:
In real life, in almost all cases, we are not aware about the
index of a data rather we are aware about the actual data elements.
Now if data is stored in a list or tuple,
and if we want to find the index of a particular element and in case
the element is far away from starting or end point, then it takes 
a lot of time to search the element in a big data. 

But the better approach can be, we can store the data in a 
dictionary and can make the unique values of data as a key
like customer id, employee id, student roll no etc. And now
if we are aware about the key, we can immediately access the 
data element.

cus_dict={10:["Vikas",39,9212468020],20:["Anil",41,9654444252],...}
id=20
print(cus_dict[id])

In dictionary, the keys are first converted to hash codes,

List
L=[10,20,30,40] 
"""
# L=[10,20,30,40,50,60,70]      #40 index








