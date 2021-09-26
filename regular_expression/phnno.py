# import re
#
# n=input("Enter phn number")
# x="[0-9]{10}"
# match = re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("invalid")

# import re
#
# n=input("Enter phn number")
# x="\d{10}"
# match = re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("invalid")

import re

n=input("Enter phn number")
x="[+][9][1]\d{10}"
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")