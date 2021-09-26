class Add:
    def set(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
add1=Add()
num1=int(input("num1 : "))
num2=int(input("num2 : "))
add1.set(num1,num2)
