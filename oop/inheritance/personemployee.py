class Person:
    def personal(self,name,address,age,qualification,phoneno):
        self.name = name
        self.address = address
        self.age = age
        self.qualification = qualification
        self.phoneno = phoneno
        print(self.name,self.address,self.age,self.qualification,self.phoneno)

class Employee(Person):
    def emp(self,empid,designation,salary):
        self.empid =empid
        self.designation = designation
        self.salary = salary
        print(self.empid,self.designation,self.salary)

em = Employee()
em.personal("Sahila","Ajayarakath house",25,"MCA",9567912806)
em.emp(1223,"Data Scientist",25000)