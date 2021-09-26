# Polymorphism ...same name different method
# Overriding & Overloading
# overloading....... same method name different number of parameters not use in python
# overrinding.....same method name and same number of arguments

# ex of overloading

class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(self.num2,self.num3)

p =Student()
p.show(4,5)
p.show(5)
