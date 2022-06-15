t = int(input())

i = 0
for i in range(1, t+1) :
    m = input().split()
    a = int(m[0])
    b = int(m[1])
    c = a+b
    print(f"Case #{i}: {a} + {b} = {c}")