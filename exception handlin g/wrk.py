a=int(input("enter the age : "))
if a<=18:
    raise Exception("not eligible below 18")
else:
    print("eligible for vaccination")