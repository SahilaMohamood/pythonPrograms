class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printval(self):
        print("name",self.name)
        print("age",self.age)

class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno = rollno
        self.mark = mark
    def prin(self):
        print("roll no",self.rollno)
        print("mark",self.mark)

pr = Student(2,35,"sasedr",34)
pr.printval()
pr.prin()