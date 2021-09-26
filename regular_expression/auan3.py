import re

x="a?"
r = "aaa abc aaaa dga"  #
matcher = re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
