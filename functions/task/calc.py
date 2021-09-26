# def add():
#     num1 = int(input("Enter num1"))
#     num2 = int(input("Enter num2"))
#     print(num1+num2)
# def sub():
#     num1 = int(input("Enter num1"))
#     num2 = int(input("Enter num2"))
#     print(num1 - num2)
# def mul():
#     num1 = int(input("Enter num1"))
#     num2 = int(input("Enter num2"))
#     print(num1 * num2)
# def div():
#     num1 = int(input("Enter num1"))
#     num2 = int(input("Enter num2"))
#     print(num1 / num2)
# print("Select operation")
# print(" 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division")
# while True:
#     i = int(input("Enter the choice"))
#     if i==1:
#         add()
#     elif i==2:
#         sub()
#     elif i==3:
#         mul()
#     elif i==4:
#         div()
#     else:
#         print("Invalid option")

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select operation")
print(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
while True:
    i = int(input("Enter the choice"))
    num1 = int(input("Enter num1"))
    num2 = int(input("Enter num2"))
    if i==1:
        print(add(num1,num2))
    elif i==2:
        print(sub(num1,num2))
    elif i==3:
        print(mul(num1,num2))
    elif i==4:
        print(div(num1,num2))
    else:
        print("Invalid option")
