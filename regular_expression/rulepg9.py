import re

x = "\W"
matcher = re.finditer(x,"abt c@dfabc2A")
for match in matcher:
    print("postion",match.start())
    print("group",match.group())