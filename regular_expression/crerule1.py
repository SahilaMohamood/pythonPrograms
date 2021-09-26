# import re
#
# n="hello"
# x="[a-z]+"
# match = re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("invalid")

import re

n="56kg"
x="[0-9]{2}[k][g]"
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")
