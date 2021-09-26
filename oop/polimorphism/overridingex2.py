class Person:
    def pri(self,name):
        self.name=name
        print("1st",self.name)
    def pri(self,age):
        self.age=age
        print("2nd",self.age)
s=Person()
s.pri("sakl")