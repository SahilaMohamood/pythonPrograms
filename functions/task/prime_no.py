# prime number
# number divisible by 1 and number itself
# 2,3,5,7,11
a = int(input("Enter the number"))
flag=0
if a>1:
    for i in range(2,a):
        if a%i==0:
            break
    else:
        flag=1
if flag==1:
    print("Prime")
else:
    print("Not Prime")
