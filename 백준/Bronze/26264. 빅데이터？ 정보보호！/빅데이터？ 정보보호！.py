a = int(input())
b = input()

c = b.count('bigdata')
d = b.count('security')

if c > d :
    print('bigdata?')
elif d > c :
    print('security!')
else :
    print('bigdata? security!')