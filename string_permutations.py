from itertools import permutations 
s1=input()
s2=input()
x=[]
a=permutations(s1)
print(a)
for i in a:
    l=''.join(i)
    x.append(l)
print(x)
for i in x:
     if s2.find(i)>=0:
         print("TRUE")
         break
    
