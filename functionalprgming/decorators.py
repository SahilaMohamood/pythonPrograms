def revert_val(func):  # here revert_val is the decorator
    def wrapper(n1, n2):        # wrapper is common, can change , no of parameters same
        if n1 < n2:
            (n1, n2) = (n2, n1)
            return func(n1, n2)
        else:
            return func(n1, n2)

    return wrapper

@revert_val
def sub(num1,num2):
    return num1-num2
print(sub(23, 76))

@revert_val
def div(num1, num2):
    return num1 / num2

print(div(2, 10))
