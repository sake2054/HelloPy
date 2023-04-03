import sys
n = int(sys.stdin.readline().rstrip())
s,b,l,p = 0,0,0,0
for x in range(0,n) :
    i = sys.stdin.readline().rstrip()
    if i[0] == "S":
        s += int(i[-1])
    elif i[0] == "B":
        b += int(i[-1])
    elif i[0] == "L":
        l += int(i[-1])
    elif i[0] == "P":
        p += int(i[-1])

if s == 5 or b == 5 or l == 5 or p == 5 :
    print("YES")
else:
    print("NO")