# k = 6
# n = 6
# for i in range(k):
#     for r in range(k):
#         print(end=" ")
#     k = k+1
#     for j in range(n):
#         print("*",end=" ")
#     print()


def parallel(n):
    k = n
    for i in range(k):
        for r in range(k):
            print(end=" ")
        k = k+1
        for j in range(n):
            print("*",end="  ")
        print()
    k = n
    for i in range(k):
        for r in range(k):
            print(end=" ")
        k = k-1
        for j in range(n):
            print("*",end="  ")
        print()
parallel(3)