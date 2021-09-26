k=6
for i in range(k):  #i=0,1,2,3,4,5
    for r in range (k): #k=0 1 2 3 4 5,0 1 2 3 4,0 1 2 3,0 1 2,0 1,0
        print(end=" ")
    k = k-1 # k= 5,4,3,2,1,0
    for j in range(0,i+1): # j=0,0 1,0 1 2,0 1 2 3,0 1 2 3 4,0 1 2 3 4 5
        print("*",end=" ")
    print()