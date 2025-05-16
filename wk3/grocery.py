def main():

    items = {}
    count = 0
    while True:
        try:
            item = input()
            count = items.get(item)
            items[item] = count
            if item in items:
                if count == None:
                    count = 1
                    items[item] = count
                elif count >= 1:
                    items[item] = count + 1
        except EOFError:
            print()
            break
        else:
            continue

    list = dict(sorted(items.items()))
    for item in list:
        print(list[item], item.upper())


main()
