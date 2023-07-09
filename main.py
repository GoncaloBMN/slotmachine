def deposit():
    while 1:
        amount = input("What would you like to deposit? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0: break
            else: print("Amount must be greater than 0.")
        else: print("Please enter a valid number.")
        
    return amount

