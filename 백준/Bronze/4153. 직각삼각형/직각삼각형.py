while True:
    i = list(map(int, input().split()))
    if i[0] == 0 and i[1] == 0 and i[2] == 0 :
        break
    else:
        if pow(i[0], 2) == pow(i[1], 2) + pow(i[2], 2):
            print("right")
        elif pow(i[1], 2) == pow(i[0], 2) + pow(i[2], 2):
            print("right")
        elif pow(i[2], 2) == pow(i[0], 2) + pow(i[1], 2):
            print("right")
        else:
            print("wrong")