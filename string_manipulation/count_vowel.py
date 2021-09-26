a=input("Enter a string")
vowel="aeiou"
count=0
for i in a:
    if i in vowel:
        count=count+1
    else:
        pass
print(count)