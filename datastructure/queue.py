que=[]
size = int(input("Enter the size : "))
front = 0
rear = 0
n = 0
def insert():
    global front,rear,size,que
    if rear>=size:
        print("The Queue is full")
    else:
        p = int(input("Enter the element : "))
        que.append(p)
        rear += 1
        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rear,size,que
    if rear == front:
        print("Queue is empty")
    else:
        front += 1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    print("Enter the operation you want to perform")
    opt = int(input("press \n 1.Enqueue\n 2.Dequeue\n"))
    if opt==1:
        insert()
    elif opt==2:
        delete()
    else:
        print("Invalid option")
    n=int(input("Do you want to continue press 1 for exist\n"))