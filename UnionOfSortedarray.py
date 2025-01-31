arr1=[1,1,2,3,4,5]
arr2=[2,3,4,4,5,6]
def Union(arr1,arr2):

    n1,n2=len(arr1),len(arr2)
    u=[]
    l=len(u)
    i=0
    j=0
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            if len(u)==0 or u[-1]!=arr1[i]:
                u.append(arr1[i])
            i+=1
        else:
            if len(u)==0 or u[-1]!=arr2[j]:
                u.append(arr2[j])
            j+=1
    while j<n2:
        if len(u)== 0 or u[-1] != arr2[j]:
            u.append(arr2[j])
        j+=1
    while i<n1:
        if len(u) == 0 or u[-1] != arr1[i]:
            u.append(arr1[i])
        i+=1
    print(u)

    # s=set()
    # for i in range(n1):
    #     s.add(arr1[i])
    # for j in range(n2):
    #     s.add(arr2[j])
    # for i in s:
    #     u.append(i)
    # print(u)
Union(arr1,arr2)