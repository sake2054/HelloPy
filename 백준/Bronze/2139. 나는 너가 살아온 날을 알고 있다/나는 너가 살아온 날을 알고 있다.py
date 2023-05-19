import datetime

while True:
    i = list(map(int, input().split()))
    if i[0] == 0 and i[1] == 0 and i[2] == 0:
        break
    else:
        print((datetime.datetime(i[2], i[1], i[0]) - datetime.datetime(i[2], 1, 1)).days + 1)
