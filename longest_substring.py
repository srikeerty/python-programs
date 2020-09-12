s=input()
l=[]
for i in range(len(s)):
    l.append(s[i])
#print(l)
'''for i in range(len(l)):
    for j in range(i+1,len(l)):
        a=l[i:j+1]
        #print(a)
        for i in range(len(a)):
            b=a[i]
            #print(b)
            for j in range(1,len(a)):
                if(b==a[j]):
                    break
        print(a)'''
k=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]!=l[j]):
            print(l[j])
            k.append(l[j])
        else:
            k==l[]
        
    print(k)

