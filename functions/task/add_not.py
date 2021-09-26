# check the number is odd by using functions without argument

def odd():
    num = int(input("Enter the number"))
    if num%2!=0 :
        print("number is odd")
    elif num==0:
        print("number is zero")
    else:
        print("number is even")
odd()
