# important
def fibno(n):
    if n<=1:
        return n
    else:
        return fibno(n-1) + fibno(n-2)

num=10

print("fibnocci series is")
for i in range(num):
    print(fibno(i))