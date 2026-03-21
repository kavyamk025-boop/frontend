# class Person:
#     def __init__(self):
#         self.name="kavya"
#         self.db=self.Dob()
#     class Dob:
#         def __init__(self):
#           self.mm=2
#           self.dd=1
#           self.yy=2027
#         def display(self):
#             print("DOB is",self.dd,"-",self.mm,"-",self.yy)
# P=Person()
# P.db.display()                
class Human:
    def __init__(self,name,hrrate,age,iq):
        self.name=name
        self.age=age
        self.hrrate=hrrate
        self.iq=iq
        self.brain=self.Brain(self.iq)
        self.heart=self.Heart(self.hrrate)
    def display(self):
            print("name is",self.name,"of age",self.age,"with heartrate",self.hrrate)
    class Heart :
        def __init__(self,hrrate):
            self.hrrate=hrrate
        def fun(self):
            print("Heart is beating")
        def modify (self):
            self.hrrate+=10
            print("heart rate is",self.hrrate)            
    class Brain :
        def __init__(self,iq):
            self.iq=iq
        def fun(self):
            print("Brain is braining")
        def modify (self):
            print("iq is",self.iq+10)                   
H=Human("kavya",21,90,433)
H.display()
H.brain.fun()
H.heart.fun()
H.brain.modify()
H.heart.modify()