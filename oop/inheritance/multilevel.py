# multilevel inheritance / hierarchical inheritance
class A:
    def prA(self):
        print("Inside A")
class B(A):
    def prB(self):
        print("inside B")
class C(B):
    def prC(self):
        print("inside C")

a=A()
a.prA()

b=B()
b.prB()
b.prA()

c=C()
c.prC()
c.prB()
c.prA()
