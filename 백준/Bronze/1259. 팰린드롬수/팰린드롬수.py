while True:
    i = input()
    if i == "0":
        break
    elif i == i[::-1]:
        print("yes")
    else:
        print("no")