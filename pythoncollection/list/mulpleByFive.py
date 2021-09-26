# list1=[1,2,3,4,5,6,7]
# print(list1)
# list2=[]
# for i in list1:
#     list2.append(i*5)
# print(list2)

list1=[2,3,4,5,6,7,23,43]
print(list1)
list2=[n*5 for n in list1]
print(list2)

# list compressions are used for creating new lists from other iterables.
# as list compressions return lists, they consist of brackets containing the expression
# which is executed for each element along with the for loop to iterate over each element
