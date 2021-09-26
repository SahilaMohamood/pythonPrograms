# class Employee:
#     def setval(self,name,id,salary,company_name):
#         self.name=name
#         self.id=id
#         self.salary=salary
#         self.company_name=company_name
#     def printval(self):
#         print(self.name,self.id,self.salary,self.company_name)
# emp=Employee()
# emp.setval("anu",3,23000,"jkhuasf")
# emp.printval()


class Employee:
    company_name = "Luminar"
    def setval(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def printval(self):
        print(self.name,self.id,self.salary,Employee.company_name)
emp=Employee()
emp.setval("anu",3,2300)
emp.printval()
