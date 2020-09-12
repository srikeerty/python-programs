n=list(input())
l=[]
r=[]
h=0
w=len(n)
for i in range(len(n)):
    p=n[i]
    d=0
    a=0
    for j in range(i+1,len(n)-1):
        if(n[j]>n[j+1]):
            d=d+1
        elif(n[j]<n[j+1]):
            a=a+1 
    #print("d",d,"a",a)
    #print("w",w)
    if(d==w-2):
        min=99
        for k in range(i+1,len(n)):
            if  n[k]>p and int(n[k])-int(p)<min:
                min=int(n[k])-int(p)
                j=n[k]
                h=k
    
        n[i],n[h]=j,n[i]
        print(n)
        l=n[i+1:]
        r=n[:i+1]
        l.reverse()
        r.extend(l)
        print(r)
        break
        
    w=w-1
    if(a==w-2):
        q=len(n)-1
        e=len(n)-2
        n[q],n[e]=n[e],n[q]
        print(n)
        break

        
