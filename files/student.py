class Stud:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
    def __str__(self):
        return self.name
f1=open("stud",'r')
for line in f1:
    # print(line)
    l=line.split(",")
    # print(l)
    name=l[0]
    age=l[1]
    st = Stud(name,age)
    st.printval()
    print(st)