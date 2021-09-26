set1={6,4,3,2,5,8,0,1}
set2={2,11,0,32,43,5,8,9}
common=set()
for i in set1:
    if i in set2:
        common.add(i)
print(common)
