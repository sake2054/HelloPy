t = input().split("/")

k = int(t[0])
d = int(t[1])
a = int(t[2])

if d == 0 or k + a < d :
    print("hasu")
else :
    print("gosu")