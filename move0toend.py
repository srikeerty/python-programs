'''n=int(input())
l=list(map(int,input().split()))
for i in l:

    if i==0:
        
        l.append(i)
    
        l.remove(i)
s=""
for i in l:
    s=s+str(i)+" "
print(s)
'''
l=list(map(int,input().split()))
print(l[-2])
