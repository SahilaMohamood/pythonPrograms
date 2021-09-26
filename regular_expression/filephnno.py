# import re
#
# f=open("phnno","r")
# for n in f:
#     wr=n.split("\n")
#     for word in wr:
#         x="[+][9][1]\d{10}"
#         match = re.fullmatch(x,word)
#         if match is not None:
#             print(word)

import re
f1=open("phnno","r")
x="[+][9][1]\d{10}"
for num in f1:
    # print(num)
    number = num.rstrip("\n")
    # print(number)
    matcher = re.fullmatch(x,number)
    if matcher!=None:
        print(num)