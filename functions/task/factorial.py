# find factorial of number by using function with argument

# def fac(a):
#     i=1
#     fact = 1
#     while(i<=a):
#         fact = fact*i
#         i+=1
#     print(fact)
# fac(5)

def fac(a):
    fact = 1
    if a > 0:
        for i in range(1, a + 1):
            fact = fact * i
            i += 1
        return (fact)
    elif a == 0:
        return ("factorial of 0 is 1")
    else:
        return ("Factorial doesn't exist for negative number")
print(fac(5))
print(fac(0))
print(fac(-1))