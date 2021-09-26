# name subject depatmnt tid collage name using constructors

class Teacher:
    collegename = "CCSIT Dr.John Matthai Center"
    def __init__(self,tid,name,subject,depart):
        self.tid = tid
        self.name = name
        self.subject = subject
        self.depart = depart

    def printval(self):
        print(self.tid)
        print(self.name)
        print(self.subject)
        print(self.depart)
        print(Teacher.collegename)

obj = Teacher(123,"Naima","Cryptography","Computer Science")
obj.printval()
obj1 = Teacher(124,"Jisha","Embedded System","Computer Science")
obj1.printval()