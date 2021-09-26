class Vscode:
    def compile(self):
        print("compiling using vscode")
    def execute(self):
        print("executing using vscode")
    def debud(self):
        print("debuging using vscode")

class Pycharm:
    def compile(self):
        print("compiling using pycharm")
    def execute(self):
        print("executing using pycharm")
    def debud(self):
        print("debuging using pycharm")

class Programmer:
    def coding(self,Ide):
        Ide.compile()
        Ide.execute()
        Ide.debud()

dev = Programmer()
pyc = Pycharm()
dev.coding(pyc)