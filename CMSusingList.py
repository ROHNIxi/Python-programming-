""
"""
Project Customer Management System (CMS):

Fields Customer: id,name,age,mob

Management System: using List: data type, 
date will be stored in python variables ie in RAM ie in volatile
memory.

CRUD: Create, Read, Update and Delete
Add Customer
Search Customer
Delete Customer
Modify Customer
Display All Customers

Basic Operations develop and you need to develop the advance or
more operations. 

Generally in table we always have one primary key. Primary key
is always unique and not null. Customer id will be the primary
key for our customers.

Initially we won't make any checks in the system, checks like
mob nos is of 10 digits or not, age is in numbers or not as well
withing some range like 5 years to 100 years. 


"""
#BLL: Business Logic Layer
id_list=[]
name_list=[]
age_list=[]
mob_list=[]
def addCustomer(id,name,age,mob):
    id_list.append(id)      #id_list=[10,20,30]
    name_list.append(name)  #name_list=["Vikas","Anil","Amit"]
    age_list.append(age)    #age_list=[39,41,45]
    mob_list.append(mob)    #mob_list=[1234,2345,3456]
def searchCustomer(id):     #id=20
    i=id_list.index(id)     #i=1
    return i
def deleteCustomer(id):     #id=20
    i=id_list.index(id)     #i=1
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
    mob_list.pop(i)
    return      #Optional
def modifyCustomer(id,name,age,mob):    #id=30,name="Prashant",age=55,mob=9999
    i=id_list.index(id)         #i=2
    name_list[i]=name
    age_list[i]=age
    mob_list[i]=mob



#PL
def showCustomer(i):    #i=1
    print("Cust ID:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i],"Cust Mob:",mob_list[i])


print("Welcome to Ashraf's CMS")

while(1):
    print("""1 for Add Cust, 2 Search Cust, 3 Delete Cust, 
    4 Modify Cust, 5 Display All, 6 for Exit:""")
    choice=input("Enter Choice 1 to 6:")
    if(choice=="1"):        #Add Customer
        id=input("Enter Customer ID:")      #10,20
        name = input("Enter Customer Name:")#Vikas,Anil
        age = input("Enter Customer Age:")  #39,41
        mob = input("Enter Customer Mob:")  #1234,2345
        addCustomer(id,name,age,mob)
        print("Customer Added Successfully")
    elif(choice=="2"):      #Search Customer
        id=input("Enter Cust ID to search:")    #id=20
        i=searchCustomer(id)    #i=1
        showCustomer(i)
    elif(choice=="3"):   #Delete Customer
        id=input("Enter Cust Id to delete:")
        deleteCustomer(id)
        print("Customer Deleted Successfully")
    elif(choice=="4"):  #Modify Customer
        id=input("Enter Cust Id to modify:")    #30
        name=input("Enter Cust updated name:")  #Prashant
        age = input("Enter Cust updated age:")  #55
        mob = input("Enter Cust updated mob:")  #9999
        modifyCustomer(id,name,age,mob)
        print("Customer modified successfully")
    elif(choice=="5"):      #Dsiplay All Customers
        for i in range(len(id_list)):   #range(3), i=0,1,2
            showCustomer(i)
    elif(choice=="6"):      #Exit
        print("Thanks for using Ashraf's CMS")
        break
    else:
        print("Incorrect choice")








