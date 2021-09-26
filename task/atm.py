acc_blns = 10000
amount = int(input("Enter the amount to withdrawal"))
if amount <= acc_blns:
    print("Successfull!\nbalance amount is",acc_blns-amount)
else:
    print("Insufficient Balance")
