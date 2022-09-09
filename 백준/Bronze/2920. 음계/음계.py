a = list(map(int, input().split()))
r = 0
for i in range(0, 8) :
    if a[i] == i+1 :
        pass
    else :
        r = 1
if r == 0 :
    print("ascending")
else :
    for i in range(0, 8) :
        if a[i] == 8 - i :
            pass
        else :
            r = 2
    if r == 1 :
        print("descending")
    else :
        print("mixed")