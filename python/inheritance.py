            # # class Mobile:
# #     def __init__(self,brand,price):
# #         self.brand=brand
# #           self.price=price
# # class Smartphone(Mobile):
# #     def __init__(self, color,brand, price):
# #         super().__init__(brand, price)
# #         self.color=color        
# #     def display(self):
# #         print(self.brand,self.color,self.price)
# # s=Smartphone("white","Iphone",100000)
# # s.display()            
# # s1=Smartphone("blue","Vivo",1002340)
# # s1.display()
# # s2=Smartphone("black","Realme",104300)
# # s2.display()

# class Card:
#     def __init__(self,cardno,exp,cvv,balance):
#         self.balance=balance
#         self.exp=exp
#         self.cardno=cardno
#         self.cvv=cvv
#     def withdraw(self,amt) :
#         if amt>self.balance or amt<0:
#          print("cant with draw")   
#         else :
#            self.balance-=amt
#     def swipe(self):
#        print("you are swiping the card")
#     def checkbal(self):
#        print("balance is",self.balance)
# class Creditcard(Card):
#     def __init__(self, cardno, exp, cvv, balance,cardlimit):
#       self.cardlimit=cardlimit
#       super().__init__(cardno, exp, cvv, balance)
#       print("constructor of creditcard") 
#     def  paybill(self,bill):
#        if bill>self.balance or bill<0 or bill>self.cardlimit:
#           print("cannot process this transction")
# class Debitcard(Card):
#     def __init__(self, cardno, exp, cvv, balance):
#       super().__init__(cardno, exp, cvv, balance)
#       print("constructor of debitcard")
#     def deposit(self,amt):
#         if amt<0 :
#             print("cannot complete this trnscation ")
#         else:
#            self.balance+=amt
# class Forexcard(Card):
#     def __init__(self, cardno, exp, cvv, balance):
#       super().__init__(cardno, exp, cvv, balance)
#       print("constructor of Forexcard")
#     def load(self,amt):
#         if amt<0:
#           print("cannot process this transaction")
#         else:
#            self.balance+=amt
#     def convert(self):
    
#         if self.balance<0 :
#            print("convertion is not possible")
#         else:
#            print("after conversion this becomes",self.balance*0.0444)
# c=Creditcard(12,"23-04-2098",234,1000000,5000)
# c.checkbal()
# c.paybill(9000)
# d=Debitcard(12,"23-04-2098",234,10000000)
# d.checkbal()
# d.deposit(100)
# d.checkbal()
# f=Forexcard(12,"23-04-2098",234,1000000)
# f.load(230)
# f.checkbal()
# f.convert()
# class Vehicle:
#     def __init__(self,vehino,brand,fuel):
#         self.vehino=vehino
#         self.brand=brand
#         self.fuel=fuel
#         print("vehicle constructor is running...")
#     def start(self):
#         print("starting.....")
#     def stop(self):
#         print("stopping......")
#     def display(self):
#         print("vehicle ni=os is",self.vehino,"brand is",self.brand,"fuel typs is",self.fuel)
# class Bike(Vehicle):
#     def __init__(self,vehino,brand,fuel):
#         super().__init__(vehino,brand,fuel)
#         print("bike constructor is running")
#     def kick(self):
#         print("kickstarrt is on")    
# class Car(Vehicle):
#     def __init__(self,vehino,brand,fuel):
#         super().__init__(vehino,brand,fuel)
#         print("Car constructor is running")
#     def opentrunk(self):
#         print("opening the trunk...") 
# class Elct:
#     def __init__(self,vehino,brand,fuel):
#         super().__init__(vehino,brand,fuel)
#         print("electric bike constructor is running")
#     def chargebatt(self):
#         print("charging battery on")    
#     def checkbet(self):
#         print("checking the battery level")
# b=Bike(123,"hero","diesel")
# b.kick()
# b.display()
# b.start()
# b.stop()
# class Animal:
#     def __init__(self):
#         print("This is animal constructor")
# class Dog(Animal):
#     def __init__(self):
#         print("Dog's constructor")

# class Animal:
#     def __init__(self):
#         print("This is animal constructor")
# class Dog(Animal):
#     def __init__(self):
#         print("Dog's constructor")        
# class Puppy(Animal):
#     def __ini__(self):
#         print("this is puppy constructor")

# class Animal:
#     def __init__(self):
#         print("This is animal constructor")
# class Dog(Animal):
#     def __init__(self):
#         print("Dog's constructor")        
# class Puppy(Dog):
#     def __ini__(self):
#         print("this is puppy constructor")


# class Animal:
#     def __init__(self):
#         print("This is animal constructor")
# class Dog(Dog):
#     def __init__(self):
#         print("Dog's constructor")        
# class Puppy(Animal,Dog):
#     def __ini__(self):
#         print("this is puppy constructor")

# class Father:
#     def drive(self):
#         print("father")
# class Mother:
#     def drive(self):
#         print("father")
# class Son(Father,Mother):
#     pass        
# c=Son()
# c.drive()
# print(Son.mro())



# class Os:
#     def __init__(self):
#         print("os cons")
#     def checkos(self):
#         print("os is working")
# class Charger:
#     def __init__(self):
#         print("charger cons")
#     def checkcharger(self):
#         print("charger is working")
# class Mobile:
#     def __init__(self):
#         self.o=Os()
#     def hasA(self,c):
#         print("charger is connecteed")

# m=Mobile()
# c=Charger()
# del m
# m.hasA(c)  
# # m.o.checkos()          
# c.checkcharger()

# class Heart:
#     def __init__(self):
#         print("Heart cons")
#     def checkos(self):
#         print("heart is working")
# class Mobile:
#     def __init__(self):
#         print("Mobile cons")
#     def checkcharger(self):
#         print("Mobile  is working")
# class Person:
#     def __init__(self):
#         self.o=Heart()
#     def hasA(self,c):
#         print("mobile is connected")

# m=Person()
# c=Mobile()
# m.hasA(c)  
# m.o.checkos()          
# c.checkcharger()
