t = int(input())
for x in range(0, t):
    h,w,n = map(int, input().split())
    if n % h == 0:
        a = h
        b = n // h
    else:
        a = n % h
        b = n // h + 1
    print(a*100+b)