class Animal:
    def eat(self):
        print("eating")
class Tiger(Animal):
    @override
    def eat(self):
        print("Hunting")        
T=Tiger()
T.eat()        
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"

s = Student("Kavya")
print(s)