import re

f1=open("regno","r")
f2=open("py","w")
x="[L][U][M]+\d{2}[P][Y]+\d{4}$"
for num in f1:
    number = num.rstrip("\n")
    matcher = re.fullmatch(x,number)
    if matcher != None:
            f2.write(number)
            f2.write("\n")