lst=[1,2,3,4,5,6,90,32,43,0]
# sort=[]
# while lst:
#     min = lst[0]
#     for i in lst:   #i=3,2,4,32,45,23,12,-2
#         if i<min:   #3<3 2<3 4<2 32<2 45<2 23<2 12<2 -2<2   # repeat the while loop till each element checked
#             min = i #min=2,-2
#     sort.append(min)
#     lst.remove(min)
# print("min :",sort[0])
# print("max :",sort[-1])

print(lst)
lst.sort()      # sort function doesn't work in nested list
print(lst)
print("min :",lst[0])
print("max :",lst[-1])
