def confirmation(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("You are not eligible")
        else:
            # print("You are eligible")
            return func(a,b,c)
    return wrapper

@confirmation
def vaccine(name,age,place):
    return print("You are elligible")

# vaccine("sahila", 23,"dgiad")
vaccine("Sulthan", 9,"asdbksf")