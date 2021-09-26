lst=[2,3,4,5]
total=int(input("enter no: "))
for i in lst:
    for j in lst:
        if(i!=j):
            if(total==(i+j)):
                print(i,j)

# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if(lst[i]+lst[j]==total):
#             print((lst[i],lst[j]))

# low=0
# upp=len(lst)-1
#
# while (low<upp):
#     sum=lst[low]+lst[upp]
#     if(sum==total):
#         print(lst[low],lst[upp])
#         break
#     elif(sum>total):
#         upp-=1
#     elif(sum<total):
#         low+=1

