l=input()
m=list(l)
n=[]
for i in m:
    n.append(int(i))
res=[]
for i in n:
    if i not in res:
        res.append(i)
for i in res:
    print(i , end='')
output:
Input:1231233553
Output:1235
