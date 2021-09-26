class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printv(self):
        print("name",self.name)
        print("age",self.age)

class Employee(Person):
    def __init__(self,job,salary,name,age):
        super().__init__(name,age)
        self.job = job
        self.salary = salary

    def printval(self):
        print("Job",self.job)
        print("salary",self.salary)

kr = Employee("Data Scientist",30000,"Sahila",26)
kr.printv()
kr.printval()
