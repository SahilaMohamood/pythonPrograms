class Person:
    def printval(self,name):
        self.name=name
        print("person",self.name)
class Child(Person):
    def printval(self,classs):
        self.classs=classs
        print("Child",self.classs)
c=Child()
c.printval("dsd")