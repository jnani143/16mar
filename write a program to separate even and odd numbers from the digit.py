l=input()
l=list(l)
n=[]
for i in l:
    n.append(int(i))
e=[]
o=[]
for i in n:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
for i in o:
    print(i,end='')
print(end=' ')
for i in e:
    print(i,end='')

    
    
    
output    
input: 1243536
Output:1353 246
