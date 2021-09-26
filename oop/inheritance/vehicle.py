class Vehicle:
    def __init__(self,model,range,color):
        self.model = model
        self.range = range
        self.color = color

    def printval(self):
        print("model",self.model)
        print("range",self.range)
        print("color",self.color)
    def __str__(self):  # to string method comonising with a string
        return self.model + self.color # use +

vr = Vehicle("KTM",242,"black")
vr.printval()
print(vr)
