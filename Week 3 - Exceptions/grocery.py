def main():
    item_count = {}

    while True:
        try:
            item = input().strip().upper()

            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1


        except EOFError:
            sorted_items = sorted( item_count.items() )
            for key,value in sorted_items:
                print(f"{value} {key}")
            break



main()
