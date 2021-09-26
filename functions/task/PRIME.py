# print number from min to max
min = int(input("Enter min value"))
max = int(input("Enter max value"))
for a in range(min,max+1):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                break
        else:
            print(a)