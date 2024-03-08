import sys

n = int(sys.stdin.readline().strip())
l = [sys.stdin.readline().strip() for _ in range(n)]
for x in range(n):
    sys.stdout.write("? "+l[x]+"\n")
    sys.stdout.flush()
    if sys.stdin.readline().strip() == "1":
        sys.stdout.write("! "+l[x]+"\n")
        sys.stdout.flush()
        sys.exit()
    else:
        sys.stdout.write("? "+l[x]+"\n")
        sys.stdout.flush()
        if sys.stdin.readline().strip() == "1":
            sys.stdout.write("! "+l[x]+"\n")
            sys.stdout.flush()
            sys.exit()