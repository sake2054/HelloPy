a = list(map(int, input().split()))
b = list(map(int, input().split()))
asum = 0
bsum = 0
awin = 0
bwin = 0

for i in range(0, 9):
    asum += a[i]
    if asum > bsum :
        awin += 1
    bsum += b[i]
    if awin > 0 :
        if asum < bsum :
            bwin += 1

if awin > 0 and bwin > 0 :
    print("Yes")
else :
    print("No")