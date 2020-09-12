n=list(input())
c=0
for j in range(0,len(n)):
    print(len(n))
    i=0 
    print(n[i])
    if(n[i]=='('  and n[j+1]==')'):
                c=c+1
                #print(c)
                del(n[j],n[i])
                print(n)
            
    elif(  n[i]=='{'  and n[j]=='}'):
                c=c+1
                #print(c)
                del(n[j],n[i])
                print(n)
            
    elif( n[i]=='[' and n[j]==']'):
                c=c+1
                #print(c)
                del(n[j],n[i])
                print(n)
            
else:
        c=c+1
        print(c)
                
           
                
        
