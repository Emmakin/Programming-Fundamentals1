def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(300, 80)

if(balance >= 60):
     print("The balance is", balance, "left")
else:
    print("You balance is zero")

