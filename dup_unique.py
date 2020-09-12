l=[1,2,3,4,3,4,2,5]
d=[]
u=[]
for i in l:
    if(l.count(i)>1):
        d.append(i)
    else:
        u.append(i)
print(d)
print(u)
