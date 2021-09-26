s={2,1,3,4,5,6,7,78,9,8,66,54,55,77,23,22,43,44}
odd = set()
even = set()
print(s)
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
# print("odd =",odd)
# print("even =",even)
print(even,odd)
