# min = int(input("Enter min value"))
# max = int(input("Enter max value"))
# while(min<=max):
#     if min%2==0:
#         print(min)
#     min+=1

min = int(input("Enter min value"))
max = int(input("Enter max value"))
for i in range(min,max+1):
    if i%2==0:
        print(i)
