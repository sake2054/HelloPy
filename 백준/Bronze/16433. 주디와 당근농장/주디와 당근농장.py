n, r, c = map(int, input().split())
if ( r % 2 == 1 and c % 2 == 1 ) or ( r % 2 == 0 and c % 2 == 0 ):
    for x in range(n):
        if x % 2 == 0:
            print('v.' * (n // 2) + 'v' * (n % 2))
        else:
            print('.v' * (n // 2) + '.' * (n % 2))
else:
    for x in range(n):
        if x % 2 == 1:
            print('v.' * (n // 2) + 'v' * (n % 2))
        else:
            print('.v' * (n // 2) + '.' * (n % 2))