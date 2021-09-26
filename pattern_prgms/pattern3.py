def patt(row):
    num=1
    for i in range(0,row):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()
patt(5)