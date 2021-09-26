def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

num = int(input("Enter a number"))
print("factorial of",num,"is",factorial(num))
# print("factorail of 5",factorial(5))