import re

x='a{2}'
r = 'aaa abc aaaa aa dga'
matcher = re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
