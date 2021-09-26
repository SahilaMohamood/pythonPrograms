def admin_required(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("You are not allowed")
        else:
            return func(a,b)
    return wrapper

@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin

@admin_required
def delete_acc(user,acno):
    return str(acno)+" Delete"

# print(change_pin("admin",1000))
# print(change_pin("user",323))
# print(delete_acc("admin",24314))
print(delete_acc("user1",3525))