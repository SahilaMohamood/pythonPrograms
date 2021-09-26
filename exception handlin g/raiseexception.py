# costamatic exeption
a=int(input("num1 : "))
b=int(input("num2 : "))
if b>a:
    raise Exception("num 2 is greater")
else:
    print(a/b)