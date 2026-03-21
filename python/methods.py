class Employee:
    def __init__(self,ename,eno,esal):
        self.ename=ename
        self.eno=eno
        self.esal=esal
    def display(self):
        print("hi                                                                                   ",self.ename)    
        print("your salary is",self.esal)
        print("your eno is",self.eno)
class Test:
    def __init__(self, emp):
        emp.esal = emp.esal+10000
        emp.display()

        
    # def modify(emp):
    #     emp.esal+=10000
    # def modify(em):
    #     em.eno+=12    

e=Employee("kavya",25,100000000)
t = Test(e)
# Test.modify(e)             
# e.display()   