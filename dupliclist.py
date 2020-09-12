def dup(l):
    d={}
    uniqlist=[]
    duplist=[]
    
    for i in l:
        d[i]=l.count(i)
    for i in d.keys():
        if (d[i] > 1):
            
        else:
            uniqlist.append(i)
    print(d)
    return uniqlist
l=[1,2,3,1,5,6,3]
s=dup(l)
print(s)

