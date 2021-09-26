import re

n=input("Enter a string")
x="[a-zA-Z]+\d$"
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")