n=list(map(int,input().split()))
c=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        #print(n[i],n[j])
        if n[i]+n[j] in n:
            #print(n[i]+n[j])
            c=c+1
print(c)
