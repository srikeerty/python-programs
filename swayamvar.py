n=int(input())
s=input()
a=input()
c=[]
if len(s)==n and len(a)==n:
    b=list(s)
    g=list(a)
    i=0
    k=0
    j=0
    h=0
while(b[i]!='\0'):
    if (b[i]==g[j]):
        c[h]=b[i]+g[j]
        k=k+1
        h+=1
        del(b[i])
        del(g[j])
    elif b[i]!=g[j]:
        g.append(g[j])
        del(g[0])
if k==n:
    print(0)

        
            
            
    
