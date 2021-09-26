# linear search it search linearly by checking each elements
# def linearsearch():
#     lit=[1,2,3,4,5,6,7,8,9]
#     ele = int(input("Enter the element to search"))
#     for i in lit:
#         if i==ele:
#             print("Element present")
#             break
#     else:
#         print("Element not present")
# linearsearch()

lis = [1,2,33,3,4,5,334,2,13,24]
def linears(lis):
    ele =int(input("Enter element to search"))
    flag=0
    for i in lis:
        if i ==ele:
            flag=1
            break
    if flag == 0:
        print("not found")
    else:
        print("found")
linears(lis)