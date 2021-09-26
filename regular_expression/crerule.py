# use fullmatch() for validation

# import re
#
# n="hello"
# x="[a-z]+"
# match = re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("invalid")


# import re
#
# n="hello"
# x="\w+"
# match = re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("invalid")

import re

n="hello"
x="[0-9]+"
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")
