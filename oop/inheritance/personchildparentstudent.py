# person child parent student
# child parent....person
# student.....child

class Person:
    def setpe(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)

class Child(Person):
    def setc(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)

class Parent(Person):
    def setpa(self,designation,phnno):
        self.designation=designation
        self.phnno=phnno
        print(self.designation,self.phnno)

class Student(Child):
    def sets(self,rollno,div):
        self.rollno=rollno
        self.div=div
        print(self.rollno,self.div)

p=Parent()
p.setpe("sahila",26,"ashfdios")
p.setpa("mca",980978356865)

s=Student()
s.setpe("Amina",1,"fgsuafo")
s.setc("lf","lkg")
s.sets(1,"A")
