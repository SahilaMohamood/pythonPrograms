lst=[1,2,3]
pos = int(input("Enter index"))
try:
    print(lst[pos])
except Exception as e:
    print(e.args)
finally:
    print("Finally")