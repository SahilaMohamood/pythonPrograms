lst = [1,2,3,4,5]

# square of all numbers map case
# map(function,list/iteration)
def square(num):
    return num**2
squares = list(map(square,lst)) #1,4,9,16,25
print(squares)
# cube of all numbers
cube = list(map(lambda num:num**3,lst))
print(cube)

# even number from lst filter case

# total sum of list reduce

# lowest number from list reduce
