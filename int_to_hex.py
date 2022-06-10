while True:
    try:
        number = int(input("please enter a number: "))
    except ValueError:
        print("error, please enter again.")
        continue
    print(hex(number))
    break


