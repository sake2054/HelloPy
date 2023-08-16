import sys
n = int(input())
print("soccer " * 1499 + "soccer")
sys.stdout.flush()
l = list(map(str, input().split()))
for x in range(1500):
    if l[x] == "swimming":
        print("bowling", end=" ")
    else:
        print("swimming", end=" ")