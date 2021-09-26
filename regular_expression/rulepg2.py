import re

x = "[^abc]" # either a b or c
matcher = re.finditer(x,"abt c@dfabc2A")
for match in matcher:
    print("postion",match.start())
    print("group",match.group())