class Person:
    def set(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)

class Child(Person):
    def setc(self,hobby,favcolor):
        self.hobby=hobby
        self.favcolor=favcolor
        print(self.hobby,self.favcolor)

class Student(Child):
    def sets(self,rollno,std,div):
        self.rollno=rollno
        self.std=std
        self.div=div
        print(self.rollno,self.std,self.div)

# p=Person()
# p.set("sulthan",9,"ellakki house")
#
# c=Child()
# c.set("sulthan",9,"ellakki house")
# c.setc("gaming","black")

s=Student()
s.set("sulthan",9,"ellakki house")
s.setc("gaming","black")
s.sets(23,"4th","A")
