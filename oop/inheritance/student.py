class Student:
    colg = "JMC"
    def __init__(self,name,rollno,dept):
        self.name=name
        self.rollno=rollno
        self.dept=dept

    def printval(self):
        print(self.name,self.rollno,self.dept,Student.colg)

    def __str__(self):
        return self.name + str(self.rollno)# can't use int variable so u should convert it into string
st = Student("sahila",17,"computer science")
st.printval()
print(st)