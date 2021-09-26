import re

n=input("Enter your email")
x="[a-zA-Z0-9]+[@][a-z]+[.][c][o][m]" #x="[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}"
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")