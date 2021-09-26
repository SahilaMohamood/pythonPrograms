def patt(row):

    for i in range(0,row):
        num = 1
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()
patt(5)