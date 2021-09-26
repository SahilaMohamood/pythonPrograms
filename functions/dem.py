# functions

# num1 = int(input("Enter num1"))
# num2 = int(input("Enter num2"))
# result = num1 + num2
# print("result =",result)

# 1. function without arguments
# def add():
#     num1 = int(input("Enter num1"))
#     num2 = int(input("Enter num2"))
#     result = num1 + num2
#     print("result =",result)
# add()

# 2. function with argument

# def add(num1,num2):
#     print(num1,"+",num2,"=",num1 + num2)
#
# add(5,4)
# add(78,57)
# add(25,25)

# 3. function with argument and return type

def add(num1,num2):
    return num1+num2

print(add(5,8))
print(add(10,20))