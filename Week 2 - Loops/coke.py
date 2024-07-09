def main():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        if coin == 25:
            amount -= coin
        elif coin == 10:
            amount -= coin
        elif coin == 5:
            amount -= coin

    print(f"Change Owed: {abs(amount)}")



main()


