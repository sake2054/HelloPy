a = []
b = 1
while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    else:
        print(f"Case {b}: Sorting... done!")
        b += 1