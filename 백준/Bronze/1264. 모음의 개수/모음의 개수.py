while True:
    try:
        i = input()
        if i == "#" :
            break
        o1 = i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")
        o2 = i.count("A") + i.count("E") + i.count("I") + i.count("O") + i.count("U")
        print(o1+o2)
    except:
        break