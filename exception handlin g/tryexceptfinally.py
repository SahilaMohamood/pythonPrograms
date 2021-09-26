# finally block run in try and except
a=[1,2,3]
index=int(input("Enter index"))
try:
    print(a[index])
except:
    print("Index not Exist")
finally:
    print("In side finally")