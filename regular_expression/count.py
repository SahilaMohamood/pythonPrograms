import re

# count = 0
# matcher = re.finditer('ba','abbbaabbabababa')
# print(matcher)   # shows address
# # for match in matcher:
#     count += 1
# print("count = ",count)


count = 0
matcher = re.finditer('ba','abbbaabbabababa')
print(matcher)   # shows address
for match in matcher:
    print("match available at ",match.start())
    print("group = ",match.group())
    count += 1
print("count = ",count)