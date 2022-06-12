import sys

t=int(sys.stdin.readline().rstrip("\n"))

j=0
while True:
	j+=1
	i=sys.stdin.readline().rstrip("\n")
	i=i.split(' ')
	o=int(i[0])+int(i[1])
	sys.stdout.write(f"{o}\n")
	if j==t:
		break