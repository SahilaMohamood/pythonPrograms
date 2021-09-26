stk=[]
size=int(input("Enter the size : "))
top=0
n=0
def push():
    global top,size
    if(top>size):
        print("Stack is full")
    else:
        p=int(input("Enter the elemenet want to push"))
        stk.append(p)
        top+=1
def pop():
    global top,size
    if(top<=0):
        print("Stack is empty")
    else:
        stk.pop()
        top-=1
def display():
    print(stk)
while(n!=1):
    print("Enter the opertaion want to perform ")
    opt=int(input("Press\n1.Push \n 2.Pop \n 3.Display"))
    if opt==1:
        push()
    elif opt==2:
        pop()
    elif opt==3:
        display()
    else:
        print("Invalid option")
    n=int(input("Do you want to continue press 1 for exist"))
