# # class Car :
# #     def start(self):
# #         print("car started")
# #     def shift(self,gn):
# #         print("gear number",gn)
# #         if gn==0:
# #             self.stop()              
# #     def stop(self):
# #         print("car stopped")

# # class Driver:
# #     def drive(self):
# #         self.c=Car()
# #         print("driver has a car")
# #         self.c.shift(1)
# #         self.c.shift(2)
# #         self.c.shift(5)
# #         print("driver with highseed")
# #         self.c.shift(0)  
# # d=Driver()
# # d.drive()                            
# # class Mobile:
# #     def switchon(self):
# #         print("switching ON.....")
# #     def switchoff(self):
# #         print("switching Off.....")
# #     def listeningtomusic(self,num):

    
# #         print("listening to music...........")
# #         if num==100:
# #             print("volume too high we are swiching off the Mobile")
# #             self.switchoff()


# # M=Mobile()

# # M.brand="samsung"
# # M.color="black"
# # M.Price=10000000
# # print(M.brand,
# # M.color,
# # M.Price)
# # M.switchon()   
# # M.switchoff()
# # M.listeningtomusic(100)



# class Employee:
#     def setdata(self,name,id,dept):
#         self.name=name
#         self.id=id
#         self.dept=dept
#     def dis(self):
#         print(self.name)
#         print(self.id)

# e=Employee()
# e.setdata('kavya',25,'cs')
# e.dis()            


# a=10
# def fun():
#     global a
#     a=50
#     print(a)
# fun()
# print(a)


class bankAccount:
    def set(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amt):
        if amt<=0:
            print("amount should be positive")
        else:
            self.balance+=amt
            print("deposited =",amt)    
    def withdraw(self,amt):
        if amt>self.balance:
            print("Not sufficient balance to withdraw")
        elif amt<=0:
             print("amount should be always positive")
        else:
            self.balance-=amt
            print("withdrawing",amt)     
    def display(self):
        print('Current amount',self.balance)
e=bankAccount()
e.set("Kavya",0)
e.holder="Kavana"
e.balance=100
print("Account holder name is",e.holder)
print("Initial Balance of ",e.holder,"is",e.balance)
e.deposit(10000)
e.display()
e.withdraw(20000)
e.display()                  