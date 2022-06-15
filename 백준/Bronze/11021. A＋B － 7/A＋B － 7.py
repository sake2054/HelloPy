t = int(input())

i = 0
for i in range(1, t+1) :
    a = input().split()
    o = int(a[0]) + int(a[1])
    print(f"Case #{i}: {o}")