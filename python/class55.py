# # #question1

# # def check_eligibility(age,quali):
# #     if age>=21 and quali!="":
# #         return print("eligible")
# #     else:
# #         return print("not eligible")
# # check_eligibility(20,"")  
# # check_eligibility(21,"")  
# # check_eligibility(23,"BE")

# # #question2
# # class BankAccount:
# #     def __init__(self,account_holder,balance):
# #         self.account_holder=account_holder
# #         self.balance=balance
# #     def deposit(self,amount):
# #         self.amount=amount
# #         if amount>=0:
# #             print("can't deposit this amount") 
# #         else:
# #             self.balance+=amount
# #             print("successfully withdrawed the amount:",self.amount)
# #     def withdraw(self,amount):
# #         self.amount=amount
# #         if amount>self.balance or amount==0:
# #            print("withdraw is not possible")
# #         else:
# #             self.amount-=amount
# #             print("Succefull withdraw")    
# #     def checkbalance(self):
# #         print("Your current balance is :",self.balance)
# # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


# # a=BankAccount("kavya",100000)
# # a.checkbalance()
# # a.deposit(1000)
# # a.withdraw(2000)

# # #question3
# # class Car:
# #     company_name="Hero"
# #     def __init__(self,brand,model,price):
# #         self.brand=brand
# #         self.model=model
# #         self.price=price
# #         print("The brand is ",self.brand,"model name:",self.model,"with price:",self.price)
# # c1=Car("asd","dsfsd",22334324)
# # c2=Car("hghgh","dsfgd",2238984)        
# # c3=Car("asdfdgdfg","dsdsfsfsd",2222324)
# # c1.company_name="honda"
# # Car.company_name="bmw"
# # print(c1.company_name)
# # print(c2.company_name)
# # print(c1.company_name)


# # #question4

# # class Company:
# #     total_employee=0
# #     def __init__(self,employee_id):
# #         self.employee_id=employee_id
# #         Company.total_employee+=1
# #         print("Total_employee",self.total_employee)
# # e1=Company(21)
# # e2=Company(54)
# # e1.total_employee        

# class Vehicle:
#     no=4
#     @classmethod
#     def ride(cls,name,no):
#         cls.no=no
#         print(name,"'s the number of wheel is",cls.no)
# Vehicle.ride("hero",2)       
# Vehicle.ride("car",4)
# Vehicle.ride("bike",2)
# Vehicle.ride("truck",8) 

class Student:
    marks=89
    def __init__(self,name):
        self.name=name
    @classmethod
    def setmarks(cls):
        print("name is with marks",cls.marks)
    @staticmethod
    def getmarks(name):
        print("name is",name)    
    def nam(self,branch):
        self.branch=branch
        print("name is",self.branch)    
S1=Student("kavya") 
S1.setmarks()    
S1.getmarks("kavana")   
S1.setmarks()  
S1.nam("cs")     