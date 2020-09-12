import itertools
n=list(map(int,input().split()))
r=[]
for i in range(1,len(n)+1):
    for x in itertools.permutations(n,i):
        r.append(int("".join(map(str,x))))
l=[]
for i in r:
    if i>9:
        l.append(i)
print(l)
print(r)

