n,a,b = map(int, input().split())
if max(n,b) > a:
    print("Bus")
elif max(n,b) < a:
    print("Subway")
elif max(n,b) == a:
    print("Anything")