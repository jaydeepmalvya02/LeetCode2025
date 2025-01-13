arr=[1,2,1,3,4,3,4]

d={}
for i in arr:
    if i in d:

        d[i]+=1
    else:
        d[i]=1
print(d)

for i in d:
    if d[i]==1:
        print(i)

