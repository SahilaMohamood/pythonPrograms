num1 = int(input("enter the number"))
num2 = int(input("enter the number"))

print("enter the value before swapping =", num1)
print("enter the value before swapping =", num2)

# first approach
temp = num1
num1 = num2
num2 = temp

print("1st enter the value after swapping =", num1)
print("1st enter the value after swapping =", num2)

# second approach (only used in python)
print(num1)
print(num2)

(num1,num2)=(num2,num1)
print("2nd enter the value after swapping =", num1)
print("2nd enter the value after swapping =", num2)

# third approach
print(num1)
print(num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2

print("3rd enter the value after swapping =", num1)
print("3rd enter the value after swapping =", num2)