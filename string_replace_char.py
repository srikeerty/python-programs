def replace(s1,s2):
    for i in range(len(s1)):
        
        if s1[i]==s2[0]:
            s1[i]=s2[2]
    return s1
s1=list(input())
s2= list(input())
s=replace(s1,s2)
print(s)

