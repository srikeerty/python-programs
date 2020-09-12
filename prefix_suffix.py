n=list(input())
c=0
ind=0
'''for i in range(len(n)):
    for j in range(i+1,len(n)):
        if(n[i]==n[j]):
            if(i==0):
                ind=j
                if(j==ind):
                    c=c+1
                    ind=j+1
            else:
                if(j==ind):
                    c=c+1
                    ind=j+1
        else:
             continue
print(c)'''
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if(n[i]==n[j]):
            if(i!=0 and j>ind):
                c=c+1
                print("j",c)
                break
            else:
                ind=j
                c=c+1
                print("I",c)
                break
print(c)
            
        
    
    

