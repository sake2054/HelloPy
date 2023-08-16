a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = a[0] * 3 + a[1] * 20 + a[2] * 120
n = b[0] * 3 + b[1] * 20 + b[2] * 120
if m > n:
    print('Max')
elif m < n:
    print('Mel')
else:
    print('Draw')