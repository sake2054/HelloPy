n, m = map(int, input().split())
a = []
b = []
o = 1
for x in range(0, n):
    a.append(input())
for y in range(0, n):
    b.append(input())
for z in range(0, n):
    c = ''
    for i in range(0, len(a[z])):
        c += a[z][i] * 2
    if c != b[z]:
        o = 0
        break
if o == 1:
    print('Eyfa')
else:
    print('Not Eyfa')
