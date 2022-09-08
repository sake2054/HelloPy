b = ":cat:"
while True:
    try:
        a = input()
        if b in a :
            print("YES")
        else :
            print("NO")
    except:
        break