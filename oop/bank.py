class Bank:
    bankname="SBI BANK"
    def acCreate(self,acno,name):
        self.acno=acno
        self.name=name
        self.minbal=2000
        self.bal=self.minbal
    def deposite(self,amnt):
        self.amnt=amnt
        self.bal += self.amnt
        print("your",Bank.bankname,"account has been credited with amt",self.amnt)
        print("your current balance=",self.bal)

    def withdrw(self,amt):
        self.amt=amt
        if self.amt > self.bal:
            print("Insufficient balance",self.bal)
        else:
            print("Account debited with",self.amt)
            self.bal -= self.amt
            print("available balance is ",self.bal)

obj = Bank()
num=int(input("Enter ac num :"))
obj.acCreate(num,"sahila")
obj.deposite(5000)
obj.withdrw(2500)
