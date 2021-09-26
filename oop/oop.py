# oop ..............  Object Oriented Programming
# class.........design pattern
# object........real world entity
# reference........operations

# class
class Person:
# rules for class name
# should be start with capital letter
# function inside class is called method
    def walk(self):     #self->instance keyword
        print("person is walking")
    def read(self):
        print("Person reading a book")
# object creation by using reference , object can created without reference bt cant operate on it
ref=Person()
ref.walk()
ref.read()

ref2=Person()
ref2.read()