import re

n=input("Enter ")
x="[a-zA-Z\W]{8,15}"  # x=[\D]{8,15}
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")