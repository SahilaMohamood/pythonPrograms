from functools import reduce
lst=[1,2,3,4,5]
sums=sum(lst)
print(sums)
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)

largest= reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(largest)

smallest = reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(smallest)

num1=int(input("enter no"))
# if num1<0:
#     print("-ve")
# else:
#     print("+ve")

print("-ve" if num1<0 else "+ve")