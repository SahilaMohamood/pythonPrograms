class Employee:
    def __init__(self,name,id,designation,salary):
        self.name=name
        self.id=id
        self.designation=designation
        self.salary=salary
    def printval(self):
        print(self.name,self.id,self.designation,self.salary)
obj=Employee("sahila",768,"Data Scientist",50000)
obj.printval()