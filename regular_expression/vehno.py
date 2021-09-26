import re

n=input("Enter vehicle number")
x="[A-Z]{2}\d{2}[A-Z]{2}\d{4}"
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")