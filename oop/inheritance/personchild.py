# multiple inheritance
class Person:
    def set(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age
        print(self.name,self.address,self.age)

class Child:
    def setval(self,std,school):
        self.std=std
        self.school=school
        print(self.std,self.school)
class Student(Person,Child):
    def printv(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
st =Student()
st.set("Sulthan","PAlliparambil house",9)
st.setval("4th std","LF School")
st.printv("24",56)

# Student....parent...Person Child
