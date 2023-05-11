change = 0
amountDue = 50
user_coin = 0
while amountDue > 0:
    user_coin = int(input("Insert Coin: "))
    if user_coin == 25 or user_coin == 10 or user_coin == 5:
        amountDue -= user_coin
        if amountDue > 0:
            print("Amount Due:",amountDue)
    else:print("Amount Due:",amountDue)

change = amountDue*(-1)
print("Change Owed:",change)