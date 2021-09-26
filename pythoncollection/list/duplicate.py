a=[2,3,4,5,6,7,4,6,4,8,9,]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    elif i not in c:
        c.append(i)
print("duplicates : ",c)