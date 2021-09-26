a=input("enter a string")
b=""
for i in a:
    if i not in b:
        b=b+i
    else:
        print("frist recursive character in",a,"is",i)
        break