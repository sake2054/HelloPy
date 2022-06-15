p=0
o=0

for i in range(1,10):
	a =int(input())
	if(o<a):
		o = a
		p = i

print(f"{o}\n{p}")