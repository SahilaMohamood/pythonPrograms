# a = int(input("Enter a number"))
# fac=1
# i=1
# while(i<=a):
#     fac = fac*i
#     i+=1
# print(fac)

# a = int(input("Enter a number"))
# fac=1
# for i in range(1,a+1):
#     fac = fac*i
#     i+=1
# print(fac)

a = int(input("Enter a number"))
if a>0:
    fac=1
    for i in range(1,a+1):
        fac = fac*i
        i+=1
    print(fac)
elif a==0:
    print("factorial of 0 is 1")
else:
    print("Factorial doesn't exist for negative number")
