# dict = {'Name': 'zara', 'Age': 10, 'Class': 'First', 'School Name': 'Luminar', 'Location': 'kochi'}
# key = input("Enter the key to check it present or not")
# for i in dict:
#     if key==i:
#         print("Present")
#         break
# else:
#     print("NotPresent")

d = {1:10,2:20,3:30,4:40,5:50,6:60}

def is_key_present(x):
    if x in d:
        print(x,"is present in dictionary")
    else:
        print(x,"is not present in dictionary")

x = int(input("Enter key"))
is_key_present(x)