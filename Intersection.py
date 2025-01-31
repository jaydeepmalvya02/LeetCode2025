a=[1,2,2,3,3,4,5,6]
b=[2,3,3,5,6,6,7]
def Intersection(a,b):
    n1=len(a)
    n2=len(b)
    ans=[]
    v=[0]*n2
    i=0
    while i<n1:
        j=0
        while j<n2:
            if a[i]==b[j] and v[j]==0:
                ans.append(a[i])
                v[j] = 1
                break
            j+=1
        i+=1
    print(ans)
    # i=0
    # j=0
    # ans=[]
    # while i<len(a) and j<len(b):
    #     if a[i]==b[j]:
    #         ans.append(a[i])
    #
    #         j+=1
    #     i+=1
    # print(ans)
Intersection(a,b)