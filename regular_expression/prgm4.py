import re

n=input("Enter ")
x="^[A-Z]{1}[a-zA-Z0-9\W]+"
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")