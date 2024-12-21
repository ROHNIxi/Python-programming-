# #New Program
# i=1
# name_list=["Vikas","Anil","Amit","Umesh","Akshat","Prashant"]
# print(name_list[i])
# name=name_list.pop(i)
# print(name)
# name=name_list.remove("Akshat")
# print(name)


# #New Program
# i=1
# name_list=["Vikas","Anil","Amit","Umesh","Akshat","Prashant"]
# name_list[i]="Sonu"
# print(name_list)
#
#Customer Management System
#BLL: Business Logic Layer
import random
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
def get_age():
    while(1):
        age=input("Enter Cust Age:")    #age="3$", "1000"
        if(age.isdecimal()):
            age=int(age)
            if(age>=5 and age<=100):
                return age
            else:
                print("Enter Age within 5 to 100 years only")
        else:
            print("Enter Age in whole numbers only")
def get_id():       #"*&^%$..."
    while(1):
        id=input("Enter Cust Id:")
        if(id not in id_list):
            if(id.isdecimal()):
                return int(id)
            else:
                print("Enter Id in numbers only")
        else:
            print("Warning:Duplicate Id!")
def generate_random_id():
    while(1):
        id=random.randint(1,999999)
        if(id not in id_list):
            return id           #"vi39922345678"
def generate_serial_id():
    if(len(id_list)==0):
        id=1
    else:
        id=id_list[-1]+1
    return id



print("Welcome to Ashraf's CMS")

while(1):
    print("""1 for Add Cust, 2 Search Cust, 3 Delete Cust,
    4 Modify Cust, 5 Display All, 6 for Exit:""")
    choice=input("Enter Choice 1 to 6:")
    if(choice=="1"):        #Add Customer
        id=generate_serial_id()        # generate_random_id()                 #get_id()      #10,20
        name = input("Enter Customer Name:")#Vikas,Anil
        age = get_age()  #39,41
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


""""""
"""
Possible Change in the Project:
1. Id should be unique, so we should check
2. Better is, id should be system generated and can be a random id
3. Can add Checks: mob no, age,
4. Add Fields: address, pin code, city, state, email_id, dob, gender...
5. Can add pwd and user name
6. Search Customer: Criteria: Search by mob, email, name..
7. Modify Customer: Again can take selected entries.
8. Can display only modified data before and after changes
9. Can ask again if to delete cust or not 
.
.
.

"""
# #New Program
# import random
# a=random.randint(1,6)
# print(a)

# #New Program
# import random
# r=random.randint()

"""
Apne resume me likh lena k apne CMS project banaya hai,


"""