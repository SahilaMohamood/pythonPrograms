products=[
    {"p_name":"complan","mrp":230,"avl_qty":50},
    {"p_name":"horlicks","mrp":250,"avl_qty":10},
    {"p_name":"bornvitta","mrp":220,"avl_qty":0},
    {"p_name":"nutricharge","mrp":200,"avl_qty":100},
    {"p_name":"avlo","mrp":100,"avl_qty":0},
]
# print all product name in the shop

pro_name=list(map(lambda product:product["p_name"],products))
print(pro_name)

# print all product name available in the shop

availble=list(filter(lambda product:product["avl_qty"]>0,products))
print(availble)

# print out of stock products

avail=list(filter(lambda product:product["avl_qty"]==0,products))
print(avail)

# print costly product

costly=max(list(map(lambda product:product["mrp"],products)))
print(costly)