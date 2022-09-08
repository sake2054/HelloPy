t = input().split()
n = int(t[0])
m = int(t[1])

if m <= 2 :
    print("NEWBIE!")
elif m <= n :
    print("OLDBIE!")
else :
    print("TLE!")