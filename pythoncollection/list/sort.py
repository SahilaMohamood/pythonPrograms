# lst =[2,3,32,56,30,57,87,90]
# print(lst)
# lst.sort()
# print(lst)

# def selectionsort(lst):
#     for i in range(len(lst)-1):
#         minpos=i
#         for j in range(i,len(lst)):
#             if lst[j]<lst[minpos]:
#                 minpos=j
#         temp=lst[i]
#         lst[i]=lst[minpos]
#         lst[minpos]=temp
# lst  = [23,12,32,43,-3,45,63,22,1]
# print(lst)
# selectionsort(lst)
# print(lst)


lst = [3,2,4,32,45,34,23,12,-2]
print(lst)
sort=[]
while lst:
    min = lst[0]
    for i in lst:   #i=3,2,4,32,45,23,12,-2
        if i<min:   #3<3 2<3 4<2 32<2 45<2 23<2 12<2 -2<2   # repeat the while loop till each element checked
            min = i #min=2,-2
    sort.append(min)
    lst.remove(min)

print(lst)
print(sort)