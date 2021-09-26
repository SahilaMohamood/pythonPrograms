# 2 types of variables

# 1 instance varible..............related to method......access using self
# 2 static variable  ..............related to class......-access using class name
class Student:
    schoolname= "masm school"   # static variable
    def setval(self,name,rollno,std):
        self.name=name
        self.rollno=rollno
        self.std=std
    def printval(self):
        print(self.name)
        print(self.rollno)
        print(Student.schoolname)
        print(self.std)
obj=Student()
obj.setval("sahila",56,"Plus2")
obj.printval()
st1=Student()
st1.setval("nimi",32,"plus2")
st1.printval()

# instant variables......related to methods
