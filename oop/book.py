class Person:
    def setvalue(self,name,age):
        self.name=name      #defining that it is a variable inside class
        self.age=age        # instance variables
    def printvalue(self):
        print("name = ",self.name)
        print("age = ",self.age)
ob=Person()
ob.setvalue("anu","26")
ob.printvalue()

ob2=Person()
ob2.setvalue("sahla","26")
ob2.printvalue()