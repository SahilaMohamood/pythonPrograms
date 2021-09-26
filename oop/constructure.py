# constructor used for initialising instance variable
# values are assigned here when object created

class Person:
    def __init__(self,name,age,address):# __init__ is the constructor
        self.name=name
        self.age=age
        self.adress=address

    def printval(self):
        print(self.name,self.age,self.adress)
obj=Person("anu",25,"asguayhs")
obj.printval()