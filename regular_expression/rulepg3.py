import re

x = "[a-z]"
matcher = re.finditer(x,"abt c@dfabc2A")
for match in matcher:
    print("postion",match.start())
    print("group",match.group())