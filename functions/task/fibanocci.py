# fibnocci
# 0 1 1 2 3 5 8 13....
# enter fibanocci series upto 10
fib1 = 0
fib2 = 1
for i in range (1,10):
    print(fib1)     #fib1=0 1 1 2 3 5 8 13 21
    temp=fib1+fib2  #temp=1 2 3 5 8 13 21 34
    fib1=fib2       #fib1=1 1 2 3 5 8 13 21
    fib2=temp       #fib2=1 2 3 5 8 13 21 34