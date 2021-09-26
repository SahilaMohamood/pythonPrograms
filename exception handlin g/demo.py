num1 = int (input("Enter num1: "))
num2 = int(input("Enter num2: "))
# res=num1/num2
# print(res)
try:
    res = num1/num2
    print(res)
# except:
#     print("Exception Occured")
except Exception as a:      # e or a can use any variable
    print(a.args)