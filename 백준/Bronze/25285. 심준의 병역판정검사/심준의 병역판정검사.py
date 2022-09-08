t = int(input())

s = 0
while s < t:
    s += 1
    a = input().split(" ")
    i = int(a[0])
    j = int(a[1])
    k = j / ((i / 100) ** 2 )

    if i <= 140 :
        r = 6
    elif i < 146 :
        r = 5
    elif i < 159 :
        r = 4
    elif i < 161 :
        if k >= 16 and k < 35 :
            r = 3
        else :
            r = 4
    elif i < 204 :
        if k >= 20 and k < 25 :
            r = 1
        elif k >= 18.5 and k < 30 :
            r = 2
        elif k >= 16 and k < 35 :
            r = 3
        else :
            r = 4
    else :
        r = 4
    
    print(r)