num = [1,2,3,4,5,6,7,8,9,346,341]
# odd=[]
# even=[]
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd",odd)
# print("even",even)

even=[i for i in num if i%2==0]
odd=[i for i in num if i%2!=0]
print(even)
print(odd)