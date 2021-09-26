name = input("Enter Student Name")
course = input("Enter Course Name")
sub1 = input("Enter Subject1 Name")
mark1 = int(input("Subject1 mark"))

sub2 = input("Enter Subject2 Name")
mark2 = int(input("Subject2 mark"))

sub3 = input("Enter Subject3 Name")
mark3 = int(input("Subject3 mark"))

sub4 = input("Enter Subject4 Name")
mark4 = int(input("Subject4 mark"))

sub5 = input("Enter Subject5 Name")
mark5 = int(input("Subject5 mark"))

print(sub1,"=",mark1)
print(sub2,"=",mark2)
print(sub3,"=",mark3)
print(sub4,"=",mark4)
print(sub5,"=",mark5)

total = mark1+mark2+mark3+mark4+mark5
avg=total/5

print("Total Marks = ",total)
print("avg of marks = ",avg)