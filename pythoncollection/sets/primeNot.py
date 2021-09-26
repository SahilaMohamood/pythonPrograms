a={1,2,3,4,5,6,7,8,9}
prime=set()
notprime=set()
for i in a:
    if i>=1:
        for b in range(2,i):
            if (i%b)==0:
                notprime.add(i)
                break
        else:
            prime.add(i)
print("prime",prime)
print("not prime",notprime)
