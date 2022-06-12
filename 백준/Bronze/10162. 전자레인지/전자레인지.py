i = int(input())

if i % 10 != 0 :
    print(-1)
else :
    a = i // 300
    b = (i - 300 * a) // 60
    c = (i - 300 * a - 60 * b) // 10
    print(f'{a} {b} {c}')