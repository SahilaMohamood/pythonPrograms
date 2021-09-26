# inheritance.......oru class nte properties vere class nu kodukka
# single inheritance

class Person:       #   base class/parent class/super class
    def walk(self):
        print("Person is Walking")
    def read(self):
        print("Person is Reading")

class Student(Person):      # inherit person class in student class / student class called derived class/sub class/child class
    def exam(self):
        print("Student attending Exam")

pr = Person()
pr.walk()
pr.read()


st = Student()
st.exam()
st.walk()
st.read()