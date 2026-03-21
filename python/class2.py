# # # # #TYPE CASTING
# # # # # x=10
# # # # # b=float(x)
# # # # # print(b,type(b))
# # # # # a=10.889
# # # # # print(a+x,type(a+x))
# # # # # s=True
# # # # # v="true"
# # # # # print(s==v)
# # # # class Employee:
# # # #     company="DCL"
# # # #     def setd(self,name,salary,dept):
# # # #         self.name=name
# # # #         self.salary=salary
# # # #         self.dept=dept
# # # # E1=Employee()
# # # # E1.setd("kavya",25000000,"testing")
# # # # print("Name is",E1.name," with Salary ",E1.salary,"Department is",E1.dept,"From company",E1.company)        
# # # # E2=Employee()
# # # # E2.setd("kavana",2000000,"development")
# # # # print("Name is",E2.name,"with Salary",E2.salary,"Department is",E2.dept,"From company",E2.company)      
# # # a=[1,2,3,1,32,3,332,434,312]
# # # def max1(a):
# # #     maxo=a[0]
# # #     maxt=a[0]
# # #     for i in range(1,len(a)):
# # #         if a[i]>maxo:
# # #             maxo=a[i]
# # #     for i in range(1,len(a)):
# # #         if a[i]>maxt and a[i]<maxo:
# # #             maxt=a[i]
# # #     return maxt        
# # # print(max1(a))












# # class Test:
# #     count=0
# #     def __init__(self):
# #         Test.count+=1
# # t1=Test()
# # t2=Test()
# # t3=Test()
# # t4=Test()
# # print("Test count is",t1.count)     
# # t1.count=5
# # print(t2.count)   
# class Train:
#     count=100
#     def __init__(self,seat):
#         Train.count-=seat
#         if Train.count<0:
#             print("cant do remaining ")
#             Train.count+=seat
#         else:
#            print("remaining seats",Train.count)
# t1=Train(20)        
# t2=Train(30)
# t3=Train(60)
class Laptop:
    count=0
    def __init__(self,model,price,ram):
        self.model=model
                       self.price=price
        self.ram=ram
        Laptop.count+=1
l1=Laptop("iphone",1000000,100)
l2=Laptop("samsung",50000,200)
l3=Laptop("vivo",30000,200)
print("Number of instances created",Laptop.count)        
        