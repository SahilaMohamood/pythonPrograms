# binary search
# 1=> sort list => find middle element => user element greater or not with middle element
# => reduce the lesser element => repeat =>when middle ele n search element same get answer

# // floadision used for ma
# king fraction into integer

a = [100,102,104,106,144,146,148,150,152,154,1,2,3,4,5,6,7,8,9,156,158,160,162,164,166,168,170,1,190,192,194,196,198]
def bsearch():
    a.sort()
    ele = int(input("Enter the element to be searched :"))
    flag = 0
    low = 0
    upp = len(a)-1
    while low <= upp:
        mid = (low + upp) // 2
        if ele > a[mid]:
            low = mid + 1
        elif ele < a[mid]:
            upp = mid - 1
        elif ele == a[mid]:
            flag = 1
            break
    if flag == 1:
        print("found")
    else:
        print("not found")

bsearch()