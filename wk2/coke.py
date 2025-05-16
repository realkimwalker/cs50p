def main():
    coins = [5, 10, 25]
    payment = 0
    price = 50
    due = 50
    coin = 0

    while payment < price:
        print("Amount Due:", due)
        coin = int(input("Insert Coin: "))
        if coin in coins:
            payment += coin
            due -= coin
        else:
            continue

    if payment >= due:
        print("Change Owed:", payment - price)


main()
