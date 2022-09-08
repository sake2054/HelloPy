a,b = list(map(int, input().split()))
if a == 0 :
    e = 0
else :
    c = list(map(int, input().split()))
    d = 0
    e = 1

    for i in range(0, a):
        if c[i] + d <= b :
            d += c[i]
        else :
            e += 1
            d = c[i]
print(e)