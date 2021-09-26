class Parent:
    def __init__(self,name,adrs):
        self.name = name
        self.adrs =adrs
    def printp(self):
        print(self.name,self.adrs)

class Teacher(Parent):
    def __init__(self,id,depart,name,adrs):
        super().__init__(name,adrs)
        self.id = id
        self.depart = depart

    def printt(self):
        print(self.id,self.depart,self.name,self.adrs)

    def __str__(self):
        return self.name + str(self.id)

t = Teacher(2321,"maths","anu","sfsusfi")
t.printp()
t.printt()
print(t)