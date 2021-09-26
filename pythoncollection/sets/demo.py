# set is used to store elements
# a = {1,2,3,4,5}
# print(a)
# print(type(a))
# b={5,6,7,8,9,}
# print(b)

# a=set()
# a.add(2)
# a.add(4)
# a.add(7)
# a.add("hello")
# a.add(9.2)
# a.add(True)     # set is a heterogeneous it can store different type of elements
# print(a)
# print(type(a))

# b={9,4,12,6,3,8}
# print(b)  # A set doesn't keep order

# a={1,2,3,4,1} # set doesn't store duplicate elements
# print(a)

# b={1,"hello",5,6,7,8,8.6,False}
# print(b)
# for i in b:
#     print(i)   # by using for loop we can iterate set and get elements from the set

# set is mutable it means updation is possible in set

# s={1,3,7,9,5,8,3,0}
# print(s)
# s.remove(3)
# print(s)
# s.clear()
# print(s)
# del s
# print(s)

# d={6,8,7,9,4}
# print(d)
# del d
# print(d)


# 1.not keeping order
# 2.not support duplicate element
# 3.heterogeneous
# 4.mutable
# 5.nesting not possible ex below


a={1,{6,7}}
print(a)