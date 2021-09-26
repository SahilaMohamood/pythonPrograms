class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return  self.a + self.b

    def subst(self):
        return  self.a - self.b

    def multy(self):
        return  self.a * self.b

    def divsn(self):
        return  self.a / self.b

a=int(input("Enter a"))
b=int(input("Enter b"))
obj = Calculator(a,b)
print(obj.add())
print(obj.subst())
print(obj.multy())
print(obj.divsn())
