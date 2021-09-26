lst=[2,3,4,5,6,23,21,34]

# even numbers

evens = list(filter(lambda num:num%2==0,lst))
print(evens)

# odd numbers

odds = list(filter(lambda num:num%2!=0,lst))
print(odds)